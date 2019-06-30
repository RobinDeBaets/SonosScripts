import argparse
import subprocess

import soco
from soco.discovery import by_name

timeout = 750
title = "Sonos controller"


def send_notification(message):
    subprocess.call(["notify-send", title, message, "-t", str(timeout)])


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sonos", help="Sonos device name")
    return parser


def get_sonos(parsed_args):
    sonos_arg = parsed_args.sonos
    sonos = None
    if sonos_arg:
        sonos = by_name(sonos_arg)
    if not sonos:
        sonos = soco.discovery.any_soco()
    if not sonos:
        send_notification("Could not find Sonos device")
        exit(1)
    return sonos
