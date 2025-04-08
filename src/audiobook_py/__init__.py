import threading

from rich.console import Console

from audiobook_py.cli import parse_args
from audiobook_py.control import control_loop
from audiobook_py.reader import read_file
from audiobook_py.utils import list_voices, validate_voice_id


def main() -> None:
    """
    Main entry point for the audiobook-py CLI application.

    Parses arguments, validates inputs, starts the reading thread,
    and handles pause/resume control.
    """

    args = parse_args()

    if args.voices:
        list_voices()
        return 0

    if not args.path:
        Console().print("[bold red]No path provided.[/]")
        return 1

    if not args.path.exists():
        Console().print(f"[red]File not found:[/] {args.path}")
        return 1

    if args.voice is not None:
        if not validate_voice_id(args.voice):
            Console().print(
                f"[bold red]Invalid voice ID:[/] [cyan]{args.voice}[/]\n"
                f"[bold yellow]Hint:[/] Use [cyan]--voices[/]"
                f"to list available voices."
            )
            return 1

    pause_flag = threading.Event()
    pause_flag.set()

    thread = threading.Thread(
        target=read_file, args=(args, pause_flag), daemon=True
    )
    thread.start()
    control_loop(pause_flag, thread)
