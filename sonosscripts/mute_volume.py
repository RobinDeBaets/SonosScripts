from sonosscripts import common


def run(parsed_args):
    sonos = common.get_sonos(parsed_args)
    sonos.mute ^= 1
    if sonos.mute:
        common.send_notification("Muted volume", common.get_icon(0), common.process_volume)
    else:
        common.send_notification("Unmuted volume", common.get_icon(sonos.volume), common.process_volume)
