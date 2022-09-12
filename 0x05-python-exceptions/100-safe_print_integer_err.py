#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_inf()[1]), file=sys.stderr)
        return (False)
