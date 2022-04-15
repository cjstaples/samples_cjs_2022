from fn_anagrams import anagram_check
from fn_date_format import reformat_date
from fn_tf_sum import fb_sums


def test_anagram_good_3():
    assert anagram_check("abc", "cba") is True


def test_anagram_bad_3():
    assert anagram_check("abc", "ddd") is False


def test_tf_sums_1_6():
    result = fb_sums(1, 6)  # range 1-5
    assert result["divisible_by_three"] == 3  # only 3
    assert result["divisible_by_five"] == 5  # only 5
    assert result["divisible_by_three_and_five"] == 0  # none, first one is 15


def test_tf_sums_1_16():
    result = fb_sums(1, 16)  # range 1-15
    assert result["divisible_by_three"] == 45  # 45:  3,6,9,12,18
    assert result["divisible_by_five"] == 30  # 30:  5,10,15
    assert result["divisible_by_three_and_five"] == 15  # only 15


def test_tf_sums_1_1000():
    result = fb_sums(1, 1000)  # range 1-999
    assert (
        result["divisible_by_three"] == 166833
    )  # b = lambda x : sum(range(0, x, 3)), c(1000) = 166833
    assert (
        result["divisible_by_five"] == 99500
    )  # c = lambda x : sum(range(0, x, 5)), b(1000) = 99500
    assert (
        result["divisible_by_three_and_five"] == 33165
    )  # d = lambda x : sum(range(0, x, 15)), d(1000) = 33165


def test_reformat_date_1987_ny():
    input_date = "1/1/1987"
    output_date = reformat_date(input_date)
    assert output_date == "19870101"


def test_reformat_date_2021_xmas():
    input_date = "12/25/2021"
    output_date = reformat_date(input_date)
    assert output_date == "20211225"
