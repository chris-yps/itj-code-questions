import pytest
import questions.divisible_list as DivisibleList

class TestDivisibleList:
    def test_return_type(self):
        assert type(DivisibleList.divisible_list(1, 100)) == list

    def test_empty_result(self):
        assert DivisibleList.divisible_list(6, 7) == []
