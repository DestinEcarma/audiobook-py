import sys

import audiobook_py

if __name__ == "__main__":
    try:
        sys.exit(audiobook_py.main())
    except KeyboardInterrupt:
        sys.exit(0)
