import common

if __name__ == "__main__":
    parser = common.get_argument_parser()
    parsed_args = parser.parse_args()
    sonos = common.get_sonos(parsed_args)
    sonos.stop()
