import argparse
import sys
import os
import sqlparse

options = {"keyword_case": "upper", "comma_first": True}


def reformat(sql_file):
    with open(sql_file, "r") as f:
        original = f.read()
    new = sqlparse.format(original, **options)
    with open(sql_file, "w") as f:
        f.write(new)
    if new == original:
        return 0
    else:
        return 1


def check_sql(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Yaml filenames to check.")

    retval = 0
    for filename in args.filenames:
        ret_for_file = reformat(filename)
        if ret_for_file:
            print("Fixing {}".format(filename))
        retval = max(retval, ret_for_file)
    return retval


if __name__ == "__main__":
    sys.exit(check_sql())
