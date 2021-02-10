from sonosscripts import common


def run(parsed_args):
    sonos = common.get_sonos(parsed_args)
    current_status = sonos.get_current_transport_info()["current_transport_state"]
    if current_status == "PLAYING":
        sonos.pause()
    elif current_status in ["STOPPED", "PAUSED_PLAYBACK"]:
        sonos.play()
