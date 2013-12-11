import dateutil.parser as dparser
import argparse
import sys
import re

re_time = re.compile("\d\d\d\d")


def pairs(itr_):
    while True:
        a = next(itr_)
        b = next(itr_)
        yield (a, b)


def add(current, starttime, endtime):
    both = [starttime, endtime]
    for i, arg in enumerate(both):
        assert len(arg) == 4
        both[i] = dparser.parse(
            "0001-01-01T%s:%s" % (
                arg[:2], arg[2:]
            )
        )
    current += (both[1] - both[0]).total_seconds() / 3600.0
    print("> %.2f" % current)
    return current


def main():
    try:
        parser = argparse.ArgumentParser(
            description=(
    """Time delta in hours with simple input:

    $> timedelta 1440 1500
    -> 0.33"""
            ),
        )

        parser.add_argument(
            "starttime",
            nargs="?",
            help="start time for delta",
        )

        parser.add_argument(
            "endtime",
            nargs="?",
            help="end time for delta",
        )

        parser.add_argument(
            "-t",
            "--test",
            help="Enable test mode (raise exceptions)",
            action="store_true"
        )

        parser.add_argument(
            "-s",
            "--stdin",
            help="Stdin mode will sum up all time-deltas you enter",
            action="store_true"
        )

        args = parser.parse_args()

        if args.stdin:
            current = 0
            for a, b in pairs(sys.stdin):
                try:
                    starttime = re_time.findall(a)[0]
                    endtime   = re_time.findall(b)[0]
                    if starttime and endtime:
                        current = add(
                            current,
                            starttime,
                            endtime
                        )
                except Exception:
                    print("Format not recognized")

        else:
            add(0, args.starttime, args.endtime)

    except Exception:
        parser.print_help()
        if args.test:
            raise
