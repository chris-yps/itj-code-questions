import pytest
import types
import questions.square_generator as SquareGenerator

class TestSquareGenerator:
    def test_yield_type(self):
        generator = SquareGenerator.create_generator(20)
        assert type(generator) == types.GeneratorType
