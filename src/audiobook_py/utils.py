import pyttsx3
from rich.console import Console
from rich.table import Table


def list_voices():
    """
    Prints a styled table of available TTS voices using Rich.

    Used to help users choose a voice ID for the `--voice` argument.
    """

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    table = Table(title="Available Voices", show_edge=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Name")

    for idx, voice in enumerate(voices):
        table.add_row(str(idx), voice.name)

    Console().print(table)


def validate_voice_id(voice_id: int) -> bool:
    """
    Checks whether the provided voice ID is within the available range.
    """
    return 0 <= voice_id < len(pyttsx3.init().getProperty("voices"))
