# 🎧 Audiobook Py

Audiobook Py is a simple audiobook player for the terminal. It is designed to be easy to use and lightweight, making it ideal for listening to text files or PDFs. The script uses the `pyttsx3` library for text-to-speech conversion.

## 🧪 Usage

Basic usage:

```sh
audiobook-py path/to/file.txt
```

With custom voice and rate:

```sh
audiobook-py file.txt --voice 1 --rate 180
```

### List Available Voices

```sh
audiobook-py --voices
```

### Show Help For More Information

```sh
audiobook-py --help
```

## ⚙️ Installation

To install Audiobook Py, first clone the repository:

```sh
git clone https://github.com/DestinEcarma/audiobook-py.git
cd audiobook-py
```

The project uses `rye` for package management, I highly recommend using it for installing the dependencies.

```sh
rye sync
```

If you don't have `rye` installed, you can install the dependencies manually. The required dependencies are:

```sh
keyboard pyttsx3 rich rich-argparse
```

### Optional

Install the package as a binary executable using `pyinstaller`:

```sh
rye run install
```

This will generate a standalone binary in the dist/ directory. To make the binary executable available globally, you can move it to a directory in your system's `PATH`.

**Linux/macOS:**

```sh
sudo mv dist/audiobook-py /usr/bin/
```

**Windows:**

- Move the `dist/audiobook-py.exe` file to a directory of your choice (e.g. `C:\tools\`).
- Add the directory to your **System Environment Variables $\to$ PATH**.
