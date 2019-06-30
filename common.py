import argparse
import subprocess

import soco
from soco import SoCo
from soco.discovery import by_name

timeout = 750
title = "Sonos controller"

low_volume_icon = "notification-audio-volume-low.svg"
medium_volume_icon = "notification-audio-volume-medium.svg"
high_volume_icon = "notification-audio-volume-high.svg"
muted_volume_icon = "notification-audio-volume-muted.svg"

min_volume = 0
max_volume = 100

min_bass = -10
max_bass = 10

def get_icon(volume):
    if volume == 0:
        return muted_volume_icon
    if volume <= 25:
        return low_volume_icon
    if volume <= 50:
        return medium_volume_icon
    return high_volume_icon


def send_notification(message, icon):
    subprocess.call(["notify-send", title, message, "-t", str(timeout), "-i", icon])


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
        sonos = soco.discovery.any_soco()
    if not sonos:
        send_notification("Could not find Sonos device")
        exit(1)
    return sonos
