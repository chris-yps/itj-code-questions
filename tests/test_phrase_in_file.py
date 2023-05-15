import pytest
import questions.phrase_in_file as PhraseInFile

class TestPhraseInFile:
    def test_return_type(self):
        file_path = "./tests/mocks/myfile.txt"
        phrase = "i look for this"
        assert type(PhraseInFile.phrase_finder(phrase, file_path)) == bool

    def test_return_true(self):
        file_path = "./tests/mocks/myfile.txt"
        phrase = "i look for this"
        assert PhraseInFile.phrase_finder(phrase, file_path) == True

    def test_return_false(self):
        file_path = "./tests/mocks/myfile.txt"
        phrase = "this is not there"
        assert PhraseInFile.phrase_finder(phrase, file_path) == False

    def test_empty_file(self):
        file_path = "./tests/mocks/empty_file.txt"
        phrase = "this is not there"
        assert PhraseInFile.phrase_finder(phrase, file_path) == False
