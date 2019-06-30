
import common

if __name__ == "__main__":
    parser = common.get_argument_parser()
    parser.add_argument("--increment", help="volume increment step", type=int, default=5)
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    increment = parsed_args.increment
    current_volume = sonos.volume
    new_volume = min(100, current_volume + increment)
    sonos.volume = new_volume
    if new_volume != current_volume:
        common.send_notification(f"Changed volume from {current_volume} to {new_volume}")
    else:
        common.send_notification("Volume is already at maximum")
