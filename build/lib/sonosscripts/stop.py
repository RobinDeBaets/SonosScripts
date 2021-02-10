from sonosscripts import common


def run(parsed_args):
    sonos = common.get_sonos(parsed_args)
    sonos.stop()
