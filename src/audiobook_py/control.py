import sys
import threading
import time

import keyboard
from rich.console import Console


def control_loop(
    pause_flag: threading.Event, reading_thread: threading.Thread
) -> None:
    """
    Keyboard listener loop for handling real-time user input.

    Supports:
    - [SPACE] to toggle pause/resume
    - [Q] to quit early
    """

    console = Console()

    console.print("[green][SPACE][/] Pause/Resume | [red][Q][/] Quit")

    while reading_thread.is_alive():
        if keyboard.is_pressed("space"):
            if pause_flag.is_set():
                pause_flag.clear()
                console.print("[yellow][Paused][/]")
            else:
                pause_flag.set()
                console.print("[yellow][Resumed][/]")

            while keyboard.is_pressed("space"):
                pass  # Do nothing, just wait for the key to be released

        elif keyboard.is_pressed("q"):
            pause_flag.set()
            sys.exit(0)

        time.sleep(0.05)
