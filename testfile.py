from spaceman import *


def test_is_word_guessed():
    assert is_word_guessed("hello", "hello") == True
    assert is_word_guessed("bod", "bot") == False
    assert is_word_guessed("wall", "wall") == True
    assert is_word_guessed("rob", "bol") == False


def test_get_guessed_word():
    assert get_guessed_word("two", ["t", "o"]) == [
        "t", "_", "o"], "works properly"
    assert get_guessed_word(
        "gosh", ["g", "s", "h"]) == ["g", "_", "s", "h"], "works properly"
    assert get_guessed_word(
        "bowl", ["b"]) == ["b", "_", "_", "_"], "works properly"
    assert get_guessed_word(
        "draw", ["d", "r", "a"]) == ["d", "r", "a", "_"], "works properly"


def test_is_guess_in_word():

    assert is_guess_in_word("i", "boiling") == True
    assert is_guess_in_word("d", "door") == True
    assert is_guess_in_word("x", "awkward") == False
    assert is_guess_in_word("q", "shame") == False
