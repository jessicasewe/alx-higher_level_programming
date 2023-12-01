#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    # Check if the command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
