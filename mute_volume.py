
import common

if __name__ == "__main__":
    parser = common.get_argument_parser()
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    current_volume = sonos.volume
    new_volume = 0
    sonos.volume = new_volume
    if new_volume != current_volume:
        common.send_notification("Muted volume")
    else:
        common.send_notification("Volume is already muted")
