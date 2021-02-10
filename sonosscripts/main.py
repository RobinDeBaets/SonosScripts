from sonosscripts import common
from sonosscripts.modules import modules


def run():
    parser = common.get_argument_parser()
    parsed_args = parser.parse_known_args()[0]
    command = parsed_args.command.lower()
    modules[command].run(parsed_args)


if __name__ == "__main__":
    run()
