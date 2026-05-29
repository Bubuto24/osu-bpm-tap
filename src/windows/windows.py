from __future__ import annotations

import sys
import time

import keyboard
from keyboard import KeyboardEvent

from helpers.log import Log
from helpers.user_input import get_keycount, get_keys
from helpers.utils import calculate_bpm, is_different_event


def windows() -> None:
    print("{:-^50}\n".format("OSU TAPPING PRACTICE"))
    keycount = 0
    keys: tuple[str, str] = get_keys()
    target_keycount = get_keycount()

    start_time: float | None = None
    previous_event: KeyboardEvent | None = None

    print()
    print(f"Start tapping({','.join(keys)})")
    print("Do note that holding on a key will not be counted.")
    print()

    while keycount < target_keycount:
        event = keyboard.read_event(suppress=True)

        Log.debug("Event: %s", event)

        if event.name == "q":
            sys.exit()

        if event.name not in keys:
            previous_event = event
            continue

        if event.event_type == keyboard.KEY_UP:
            previous_event = event
            continue

        if is_different_event(previous_event, event):
            if start_time is None:
                start_time = time.time()

            keycount += 1

            Log.debug("Keycount changed to %s", keycount)

        previous_event = event

    assert start_time is not None, "Time did not start."
    bpm = calculate_bpm(start_time, time.time(), keycount)
    print(f"Your tapping bpm is {bpm:.2f}")

    print("Press Enter to continue...")
    keyboard.wait("enter", suppress=True)


windows()
