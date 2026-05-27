from __future__ import annotations

from keyboard import KeyboardEvent

from .log import Log


def is_different_event(
    previous_event: KeyboardEvent | None, current_event: KeyboardEvent
) -> bool:
    """
    Checks if the user is not holding a key down

    :param previous_event: Previous key input event
    :param current_event: Current key input event
    :return: True if the events are different, otherwise False
    """
    if previous_event is None:
        return True

    Log.debug("PREVIOUS EVENT NAME: %s", previous_event.name)
    Log.debug("CURRENT EVENT NAME: %s", current_event.name)
    Log.debug("PREVIOUS EVENT TYPE: %s", previous_event.event_type)
    Log.debug("CURRENT EVENT TYPE: %s", current_event.event_type)

    return not (
        previous_event.name == current_event.name
        and previous_event.event_type == current_event.event_type
    )


def calculate_bpm(start_time: float, end_time: float, keycount: int) -> float:
    """
    Calculate tapping bpm

    :param start_time: Time started
    :param end_time: Time ended
    :param keycount: Number of times tapped
    :return: Bpm
    """
    duration = end_time - start_time
    bpm = (keycount / duration) * 15
    return bpm
