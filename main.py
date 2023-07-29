# -*- coding: utf-8
# Simple autoclicker without gui
import time

import pyautogui
import random

import json


MODES = {
    "key_up": pyautogui.keyUp,
    "key_down": pyautogui.keyDown,
    "key_press": pyautogui.press
}

with open("config.json", "r") as file:
    CONFIG = json.load(file)


def unlimited(group: dict) -> None:
    """Unlimited key presses - until program is closed.

    :param group: key group dict from config file
    """
    while True:
        key_press(group)
        time.sleep(group["group_delay"])


def limited(group: dict, limit: int) -> None:
    """Limited key presses - will press keys as many times as limit

    :param group: key group dict from config file
    :param limit: how many times the key/ key group should be pressed
    """
    for _ in range(limit):
        key_press(group)
        time.sleep(group["group_delay"])


def get_delay(group: dict) -> float:
    """Get delay between keystrokes in seconds.

    :param group: key group dict from config file
    :return: delay in seconds
    """
    if "keys_delay" in group.keys():
        delay = group["keys_delay"]
    else:
        delay_min = group["keys_delay_min"]
        delay_max = group["keys_delay_max"]
        delay = round(random.uniform(delay_min, delay_max), 3)
    print(delay)
    return delay


def key_press(group: dict) -> None:
    """Will press wanted key(s) with specified delay

    :param group: key group dict from config file
    """

    for key in group["keys"]:
        MODES[group["mode"]](key)
        time.sleep(get_delay(group))


def main():
    """Main function."""
    for group_name in CONFIG.keys():
        group = CONFIG[group_name]
        count = group["count"]
        if isinstance(count, str):
            unlimited(group)
        elif isinstance(count, int):
            limited(group, limit=count)


if __name__ == "__main__":
    main()
    exit(0)
