#  samples
#
#

import sys


def check_three(val):
    if val % 3 == 0:
        return True
    else:
        return False


def check_five(val):
    if val % 5 == 0:
        return True
    else:
        return False


# add integers in supplied range
# return a dict containing all the sums
def fb_sums(begin, end):
    by_three = 0
    by_five = 0
    by_both = 0

    for i in range(begin, end):
        # both true, add to by_both
        if check_three(i) & check_five(i):
            by_both = by_both + i
        # only three true, add to by_three
        if check_three(i):
            by_three = by_three + i
        # only five true, add to by_five
        if check_five(i):
            by_five = by_five + i

    sums = {'divisible_by_three': by_three, 'divisible_by_five': by_five, 'divisible_by_three_and_five': by_both}
    return sums


def main():
    print('(fb sums) main:')
    print()
    print(f":::::::::::::::::::::::::::::::::::::::::::::::")

    range_begin = 1
    range_end = 1000
    sums = fb_sums(range_begin, range_end)
    print(f"SANITY: range inclusive of values {range_begin} - {range_end-1}")
    for val in sums:
        print(f"{val} : {sums[val]}")

    print(f":::::::::::::::::::::::::::::::::::::::::::::::")
    print()
    print('(fb sums) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
