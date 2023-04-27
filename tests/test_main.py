"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from main import is_div3, is_div3_str


class Test(TestCase):
    def test_is_div3(self):
        assert not is_div3(5)
        assert is_div3(6)
        assert not is_div3(635)
        assert is_div3(963)

    def test_is_div3_str(self):
        assert is_div3_str("5") == "5 is not divisible by 3."
        assert is_div3_str("6") == "6 is divisible by 3."
        assert is_div3_str("635") == "635 is not divisible by 3."
        assert is_div3_str("963") == "963 is divisible by 3."
