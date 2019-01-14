import argparse
import sys
import sqlparse

options = {
    "keyword_case": "upper",
    "comma_first": True,
    "strip_comments": False,
    "reindent": True,
    "indent_tabs": False,
    "indent_width": 2,
}


def reformat(sql_file):
    with open(sql_file, "r") as f:
        original = f.read()
    new = sqlparse.format(original, **options)
    if new == original:
        return 0
    else:
        with open(sql_file, "w") as f:
            f.write(new)
        return 1


def check_sql(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="sql filenames to check.")
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        ret_for_file = reformat(filename)
        if ret_for_file:
            print("Fixing {}".format(filename))
        retval = max(retval, ret_for_file)
    return retval


if __name__ == "__main__":
    sys.exit(check_sql())
