from datetime import time, datetime

from word_clock import WordClock


def test_converter():
    assert WordClock()


def test_when_requested_10_o_clock_then_converter_gives_requested_time():
    test_time = time(hour=10)
    assert WordClock().get_time(test_time) == "Ten o'clock"


def test_when_requested_11_o_clock_then_converter_gives_requested_time():
    test_time = time(hour=11)
    assert WordClock().get_time(test_time) == "Eleven o'clock"


def test_when_requested_11_34_then_converter_gives_requested_time():
    test_time = time(hour=11, minute=34)
    assert WordClock().get_time(test_time) == "Eleven thirty-four"


def test_when_requested_11_00_31_then_converter_drops_seconds():
    test_time = time(hour=11, minute=00, second=31)
    assert WordClock().get_time(test_time) == "Eleven o'clock"


def test_when_requested_11_10_31_then_converter_gives_requested_hours_minutes_and_ish_as_seconds():
    test_time = time(hour=11, minute=10, second=31)
    assert WordClock().get_time(test_time) == "Eleven ten ish"


def test_when_no_specific_time_is_requested_converter_gives_current_time():
    now = datetime.now()
    assert WordClock().get_time() == WordClock().get_time(now.time())
