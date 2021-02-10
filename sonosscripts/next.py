from sonosscripts import common, change_track_common


def run(parsed_args):
    sonos = common.get_sonos(parsed_args)
    sonos.next()
    change_track_common.send_notification(sonos)
