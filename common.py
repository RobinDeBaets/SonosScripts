import argparse
import os

import soco
from soco import SoCo
from soco.discovery import by_name

import notify_send

notification_timeout = 10000
notification_title = "Sonos controller"

low_volume_icon = "notification-audio-volume-low"
medium_volume_icon = "notification-audio-volume-medium"
high_volume_icon = "notification-audio-volume-high"
muted_volume_icon = "notification-audio-volume-muted"

min_volume = 0
max_volume = 100

min_bass = -10
max_bass = 10

process_volume = 6455
process_bass = 7626
process_track = 7149

tmp_ip_file = "/tmp/sonos_ip"


def get_icon(volume):
    if volume == 0:
        return muted_volume_icon
    if volume <= 25:
        return low_volume_icon
    if volume <= 50:
        return medium_volume_icon
    return high_volume_icon


def send_notification(message, icon, notification_id, title=notification_title):
    notify_send.send_notification(title, message, notification_id=notification_id, icon=icon,
                                  timeout=notification_timeout)


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sonos", help="Sonos device name")
    parser.add_argument("--sonos_ip", help="Sonos IP")
    return parser


def get_sonos(parsed_args):
    sonos_arg = parsed_args.sonos
    sonos_ip = parsed_args.sonos_ip
    sonos = None
    if sonos_ip:
        sonos = SoCo(sonos_ip)
    if sonos_arg:
        sonos = by_name(sonos_arg)
    if not sonos:
        # Try reading IP from temp file
        tmp_sonos_ip = get_tmp_sonos_ip()
        if tmp_sonos_ip:
            sonos = SoCo(tmp_sonos_ip)
        if not sonos:
            # File didn't exist or IP in file was incorrect
            sonos = soco.discovery.any_soco()
            if sonos:
                set_tmp_sonos_ip(sonos.ip_address)
    if not sonos:
        send_notification("Could not find Sonos device", muted_volume_icon, process_volume)
        exit(1)
    return sonos


def get_tmp_sonos_ip():
    if os.path.exists(tmp_ip_file):
        with open(tmp_ip_file) as file:
            return file.read()


def set_tmp_sonos_ip(tmp_ip):
    with open(tmp_ip_file, "w+") as f:
        f.seek(0)
        f.write(tmp_ip)
        f.truncate()
