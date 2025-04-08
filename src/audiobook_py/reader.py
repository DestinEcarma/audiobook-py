import argparse
import re
import threading
from pathlib import Path

import pyttsx3


def tts(
    content: str, engine: pyttsx3.Engine, pause_flag: threading.Event
) -> None:
    """
    A text to speech function that reads the content aloud.
    """
    sentences = re.split(r"([.,!?])", content)

    for i in range(0, len(sentences), 2):
        pause_flag.wait()

        sentence = sentences[i].strip()

        if i + 1 < len(sentences):
            sentence += sentences[i + 1]

        if not sentence:
            continue

        print(sentence)

        engine.say(sentence)
        engine.runAndWait()


def read_text_file(
    path: Path, engine: pyttsx3.Engine, pause_flag: threading.Event
) -> None:
    """
    Read a text file and convert its content to speech.
    """
    with open(path, "rb") as file:
        for line in file:
            content = line.decode("utf-8").strip()

            if not content:
                continue

            tts(content, engine, pause_flag)


def read_file(args: argparse.Namespace, pause_flag: threading.Event) -> None:
    """
    Main function to read a text file or PDF file and convert its content to
    speech.
    """
    engine = pyttsx3.init()

    engine.setProperty("rate", args.rate)
    engine.setProperty("volume", args.volume)

    if args.voice is not None:
        engine.setProperty(
            "voice", engine.getProperty("voices")[args.voice].id
        )

    if args.path.suffix.lower() == ".pdf":
        # TODO: Implement PDF reading
        pass
    else:
        read_text_file(args.path, engine, pause_flag)
