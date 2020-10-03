import pytest
from dateutil import tz
import datefinder
from datetime import datetime


def test_french_string():
    t = "29/06/2020 à 10h00"
    matches = [i for i in datefinder.find_dates(t)]
    d = datetime(2020, 6, 29, 10, 0, 0, 0)
    assert d in matches
