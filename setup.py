
from setuptools import setup

setup(
    name="SonosScripts",
    version="0.1",
    packages=["sonosscripts"],
    entry_points={
        "console_scripts": [
            "sonosscripts=sonosscripts.main:run"
        ],
    }, install_requires=[
        "soco",
        "notify2",
        "dbus-python",
        "psutil"
    ]
)