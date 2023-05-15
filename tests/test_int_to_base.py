import pytest
import questions.int_to_base as IntToBase

class TestIntToBase:
    def test_return_type(self):
        assert type(IntToBase.number_to_base(5, 3)) == str
