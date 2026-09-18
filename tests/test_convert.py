import pytest
from delta_kelvin.convert import convert


def test_interval_to_point_raises():
    with pytest.raises(ValueError):
        convert(3.0, "interval", "point")


def test_point_to_kelvin():
    assert convert(0.0, "point", "kelvin") == 273.15
