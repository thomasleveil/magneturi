import os
import sys
from textwrap import dedent
from magneturi import from_torrent_file, from_torrent_data


def usage():
    print(dedent("""usage: magneturi [<torrent file>] [<torrent file>]...

        Generate a manget URI for the given torrent file.
        Magneturi can read the torrent file content from stdin.
        """))


def main():
    if '-h' in sys.argv or '--help' in sys.argv:
        usage()
        sys.exit(0)

    if len(sys.argv) >= 2:
        for filename in sys.argv[1:]:
            print(from_torrent_file(filename))
    else:
        if os.isatty(0):
            usage()
            sys.exit(1)
        torrent_contents = sys.stdin.buffer.read()
        print(from_torrent_data(torrent_contents))


main()