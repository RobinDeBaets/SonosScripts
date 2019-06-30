
import common

if __name__ == "__main__":
    parser = common.get_argument_parser()
    parser.add_argument("--decrement", help="volume decrement step", type=int, default=5)
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    decrement = parsed_args.decrement
    current_volume = sonos.volume
    new_volume = max(0, current_volume - decrement)
    sonos.volume = new_volume
    if new_volume != current_volume:
        common.send_notification(f"Changed volume from {current_volume} to {new_volume}")