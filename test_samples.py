from fn_anagrams import anagram_check
from fn_date_format import reformat_date
from fn_json_find_value import find_items
from fn_sums_threefive import fb_sums


def test_anagram_3_chars_matches():
    assert anagram_check("abc", "cba") is True


def test_anagram_3_chars_no_match():
    assert anagram_check("abc", "ddd") is False


def test_anagram_27_chars_matches():
    assert (
        anagram_check("hydroxydeoxycorticosterones", "hydroxydesoxycorticosterone")
        is True
    )


def test_anagram_14_chars_matches_case_insensitive():
    assert anagram_check("undefinability", "UNIDENTIFIABLY") is True


def test_anagram_14_chars_matches_whitespace_insensitive():
    assert anagram_check("A dream within a dream", "What am I a mind reader") is True


def test_anagram_superset_no_match():
    assert anagram_check("abc", "abcabc") is False


def test_sums_of_threes_and_fives_between_0_6():
    result = fb_sums(0, 6)  # effective range 1-5
    assert result["divisible_by_three"] == 3  # only 3
    assert result["divisible_by_five"] == 5  # only 5
    assert result["divisible_by_three_and_five"] == 0  # none, first one is 15


def test_sums_of_threes_and_fives_between_0_16():
    result = fb_sums(0, 16)  # effective range 1-15
    assert result["divisible_by_three"] == 45  # 45:  3,6,9,12,18
    assert result["divisible_by_five"] == 30  # 30:  5,10,15
    assert result["divisible_by_three_and_five"] == 15  # only 15


def test_sums_of_threes_and_fives_between_0_1000():
    result = fb_sums(0, 1000)  # effective range 1-999
    assert (
        result["divisible_by_three"] == 166833
    )  # b = lambda x : sum(range(0, x, 3)), c(1000) = 166833
    assert (
        result["divisible_by_five"] == 99500
    )  # c = lambda x : sum(range(0, x, 5)), b(1000) = 99500
    assert (
        result["divisible_by_three_and_five"] == 33165
    )  # d = lambda x : sum(range(0, x, 15)), d(1000) = 33165


def test_sums_of_threes_and_fives_between_5_50():
    result = fb_sums(5, 50)  # effective range 6-49
    assert result["divisible_by_three"] == 405  # 405:  6,9,12 .. 48
    assert result["divisible_by_five"] == 220  # 220:  10,15,20 .. 45
    assert result["divisible_by_three_and_five"] == 90  # 90:  15,30,45


def test_reformat_date_1987_july4th_not_padded():
    input_date = "7/4/1987"
    output_date = reformat_date(input_date)
    assert output_date == "19870704"


def test_reformat_date_1999_nyd_padded():
    input_date = "01/01/1999"
    output_date = reformat_date(input_date)
    assert output_date == "19990101"


def test_reformat_date_2021_xmas():
    input_date = "12/25/2021"
    output_date = reformat_date(input_date)
    assert output_date == "20211225"


def test_find_json_value_display_name_centage():  # Centage found x5
    search_item = "Centage"
    search_result = find_items(search_item)
    assert len(search_result) == 5


def test_find_json_value_id_e4b0():  # e4b0 found x7
    search_item = "e4b0"
    search_result = find_items(search_item)
    assert len(search_result) == 7


def test_find_json_value_both_literal_one():  # '1' found in both attributes, x5
    search_item = "1"
    search_result = find_items(search_item)
    assert len(search_result) == 5


def test_find_json_value_verify_blank_is_tolerated():  # none expected to be found
    search_item = ""
    search_result = find_items(search_item)
    assert len(search_result) == 0


def test_find_json_value_copy_verify_handles_duplicates():  # Copy x3, but should return 2 items
    search_item = "Copy"
    search_result = find_items(search_item)
    assert len(search_result) == 2


def test_find_json_value_verify_unicorn_not_present():  # none expected to be found
    search_item = "Unix0rn"
    search_result = find_items(search_item)
    assert len(search_result) == 0
