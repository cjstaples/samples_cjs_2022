#  samples
#
#

import sys


# verify whether two strings are anagrams
def anagram_check(string1, string2):
    """Check whether two supplied strings are anagrams, adjusted for case and whitespace

    :param string1: first string value
    :type string1: str
    :param string2: second string value
    :type string2: str
    :returns: comparison of sorted strings (True if equal; False if not equal)
    :rtype: boolean
    """
    adjusted_string1 = sorted("".join(string1.split()).lower())
    adjusted_string2 = sorted("".join(string2.split()).lower())
    if adjusted_string1 == adjusted_string2:
        return True
    else:
        return False


def main():
    print("(anagram) main:")
    print()
    print(":::::::::::::::::::::::::::::::::::::::::::::::")

    str1 = "rode"
    str2 = "doer"
    check = anagram_check(str1, str2)
    print(f"SANITY: inputs {str1} and {str2}, are anagrams? : {check}")

    print(":::::::::::::::::::::::::::::::::::::::::::::::")
    print()
    print("(anagram) end::")

    return 0


# ----------------------------------------
if __name__ == "__main__":
    result = main()
    sys.exit(0)
