import psutil as psutil

import common

spotify_name = "spotify"


def send_notification(sonos):
    if not is_spotify_running():
        track = sonos.get_current_track_info()
        common.send_notification(f"{track['artist']} - {track['album']}", common.get_icon(sonos.volume),
                                 common.process_track,
                                 title=track['title'])


def is_spotify_running():
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            if p.name() == spotify_name:
                return True
        except:
            continue
