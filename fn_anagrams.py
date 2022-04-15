#  samples
#
#

import sys


# verify whether two strings are anagrams
def anagram_check(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


def main():
    print('(anagram) main:')
    print()
    print(f":::::::::::::::::::::::::::::::::::::::::::::::")

    str1 = "rode"
    str2 = "doer"
    check = anagram_check(str1, str2)
    print(f"SANITY: inputs {str1} and {str2}, are anagrams? : {check}")

    print(f":::::::::::::::::::::::::::::::::::::::::::::::")
    print()
    print('(anagram) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
