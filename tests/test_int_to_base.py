import pytest
import questions.int_to_base as IntToBase

class TestIntToBase:
    def test_return_type(self):
        assert type(IntToBase.number_to_base(5, 3)) == str

    def test_base_2(self):
        assert IntToBase.number_to_base(5, 2) == "101"

    def test_base_3(self):
        assert IntToBase.number_to_base(5, 3) == "12"
