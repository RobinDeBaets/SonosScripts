from sonosscripts import common
from sonosscripts.common import round_nearest


def run(_):
    parser = common.get_argument_parser()
    parser.add_argument("--step", help="volume step", type=int, default=5)
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    step = parsed_args.step
    current_volume = sonos.volume
    new_volume = current_volume + step
    new_volume = round_nearest(new_volume, step)
    new_volume = min(common.max_volume, new_volume)
    new_volume = max(common.min_volume, new_volume)
    sonos.volume = new_volume
    if new_volume != current_volume:
        common.send_notification(f"Changed volume from {current_volume} to {new_volume}", common.get_icon(new_volume),
                                 common.process_volume)
    else:
        if new_volume == common.max_volume:
            common.send_notification("Volume is already at maximum", common.get_icon(new_volume), common.process_volume)
        else:
            common.send_notification("Volume is already at minimum", common.get_icon(new_volume), common.process_volume)
