#  samples
#
#
from datetime import datetime
import sys


def reformat_date(in_date):
    """Change string date value from one format to another format

    :param in_date: string date value, format M/D/YYYY
    :type in_date: str
    :returns: out_date: string date value, format YYYYMMDD
    :rtype: str
    """

    dt_obj = datetime.strptime(in_date, "%m/%d/%Y")
    out_date = dt_obj.strftime("%Y%m%d")
    return out_date


def main():
    print("(date format) main:")
    print()
    print(":::::::::::::::::::::::::::::::::::")

    input_date = "1/2/1987"
    output_date = reformat_date(input_date)

    print(f"SANITY: date input  : {input_date}")
    print(f"SANITY: date output : {output_date}")

    print(":::::::::::::::::::::::::::::::::::")
    print()
    print("(date format) end::")

    return 0


# ----------------------------------------
if __name__ == "__main__":
    result = main()
    sys.exit(0)
