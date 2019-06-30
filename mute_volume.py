import common

if __name__ == "__main__":
    parser = common.get_argument_parser()
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    current_volume = sonos.volume
    sonos.mute ^= 1
    if sonos.mute:
        common.send_notification("Muted volume", common.get_icon(0))
    else:
        common.send_notification("Unmuted volume", common.get_icon(sonos.volume))
