from sonosscripts import common


def run(_):
    parser = common.get_argument_parser()
    parser.add_argument("--step", help="volume step", type=int, default=1)
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    step = parsed_args.step
    current_bass = sonos.bass
    new_bass = current_bass + step
    new_bass = min(common.max_bass, new_bass)
    new_bass = max(common.min_bass, new_bass)
    sonos.bass = new_bass
    if new_bass != current_bass:
        common.send_notification(f"Changed bass from {current_bass} to {new_bass}", common.get_icon(50),
                                 common.process_bass)
    else:
        if current_bass == common.max_bass:
            common.send_notification("Bass is already at maximum", common.get_icon(50), common.process_bass)
        else:
            common.send_notification("Bass is already at minimum", common.get_icon(50), common.process_bass)
