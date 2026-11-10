"""Tests for tools/profile/fetch.py streak calculation."""

import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from fetch import streaks


def test_streaks_empty():
    today = datetime.date(2026, 11, 9)
    current, longest = streaks({}, today)
    assert current == 0
    assert longest == 0


def test_streaks_current_three_days():
    today = datetime.date(2026, 11, 9)
    days = {today - datetime.timedelta(days=i): 1 for i in range(3)}
    current, longest = streaks(days, today)
    assert current == 3
    assert longest == 3


def test_streaks_with_gap():
    today = datetime.date(2026, 11, 9)
    days = {
        today: 1,
        today - datetime.timedelta(days=1): 1,
        today - datetime.timedelta(days=2): 0,  # gap breaks streak
        today - datetime.timedelta(days=3): 1,
        today - datetime.timedelta(days=4): 1,
        today - datetime.timedelta(days=5): 1,
    }
    current, longest = streaks(days, today)
    assert current == 2
    assert longest == 3


def test_streaks_zero_today():
    today = datetime.date(2026, 11, 9)
    days = {today: 0, today - datetime.timedelta(days=1): 1}
    current, longest = streaks(days, today)
    assert current == 1  # streak ended yesterday
    assert longest == 1
