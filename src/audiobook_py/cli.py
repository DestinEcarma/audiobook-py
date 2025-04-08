import argparse
from pathlib import Path

from rich_argparse import RichHelpFormatter

DESCRIPTION = "Read a text file or PDF file aloud using pyttsx3."

PATH_HELP = "Path to the text or PDF file."
VOICES_HELP = "List available voices."
RATE_HELP = "Speech rate (words per minute)."
VOICE_HELP = "Voice ID, use --voices to list available voices."
VOLUME_HELP = "Volume level (0.0 to 1.0)."


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments using argparse.
    """

    parser = argparse.ArgumentParser(
        description=DESCRIPTION, formatter_class=RichHelpFormatter
    )

    parser.add_argument("path", type=Path, nargs="?", help=PATH_HELP)
    parser.add_argument("--voices", action="store_true", help=VOICES_HELP)
    parser.add_argument("-r", "--rate", type=int, default=150, help=RATE_HELP)
    parser.add_argument("-v", "--voice", type=int, help=VOICE_HELP)
    parser.add_argument("--volume", type=float, default=1.0, help=VOLUME_HELP)

    return parser.parse_args()
