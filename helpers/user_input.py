import keyboard


def get_keys() -> tuple[str, str]:
    """
    Retrieve hotkeys from user

    :return: Tuple of keys
    """
    key1 = _prompt_for_key("First key: ")
    while True:
        key2 = _prompt_for_key("Second key: ")
        if key2 != key1:
            return key1, key2
        print("Second key cannot be the same as first hotkey.")


def get_keycount() -> int:
    """
    Prompts the user for the number of times to tap

    :return: Number of times to tap
    """
    MIN_LIMIT = 20
    MAX_LIMIT = 1000
    while True:
        user_input = input(
            "How many times do you want to tap for? "
            f"({MIN_LIMIT} - {MAX_LIMIT}): "
        ).strip()
        if user_input.isdigit() and MIN_LIMIT <= int(user_input) <= MAX_LIMIT:
            return int(user_input)
        print(f"Please enter a number from {MIN_LIMIT} to {MAX_LIMIT}.")


# Private functions
def _prompt_for_key(message: str) -> str:
    """
    Gets the key from user input

    :param message: Message to display for user prompt
    :return: The key name
    """
    while True:
        user_input = input(message).lower().strip()
        # Edge case: empty input means enter
        if user_input == "":
            user_input = "enter"
        if _validate_key(user_input):
            return user_input
        print("Invalid key.")


def _validate_key(key: str) -> bool:
    """
    Check whether a key name is recognized by the keyboard library.

    :param key: Name of the key
    :return: True if the key is valid, otherwise False.
    """

    return bool(keyboard.key_to_scan_codes(key, error_if_missing=False))
