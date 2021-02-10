# SonosScripts

A lightweight CLI wrapper for [SoCo](https://github.com/SoCo/SoCo);

**LICENSE**: [WTFPL](https://en.wikipedia.org/wiki/WTFPL)

## Setup:

```
git clone https://github.com/RobinDeBaets/SonosScripts
cd SonosScripts
python3 setup.py install --user
```

## Usage

All commands can take the following options as well:
- `--sonos`: target specific Sonos device by name
- `--sonos_ip`: target specific Sonos device by IP

If not given, it will look for the first available Sonos device on your current network.

```
sonosscripts change_bass --step X   # Increase or decrease bass by given amount
sonosscripts change_volume --step X # Increase or decrease volume by given amount
sonosscripts next
sonosscripts stop
sonosscripts previous
sonosscripts play_pause
sonosscripts mute_volume
```

You can use these scripts in combination with custom keyboard shortcuts on your PC to easily modify your 
Sonos volume, bass and track.

### Development environment

```
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -e . 
```
