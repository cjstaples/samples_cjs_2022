#  samples
#
#
from datetime import datetime
import sys


def reformat_date(in_date):

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
