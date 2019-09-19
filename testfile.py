from spaceman import is_word_guessed, get_guessed_word, is_guess_in_word

# Tests different inputs/outputs for is_word_guessed function


def test_is_word_guessed():

    # Tests if the words match each other

    assert is_word_guessed("hello", "hello") == True
    assert is_word_guessed("bod", "bot") == False
    assert is_word_guessed("wall", "wall") == True
    assert is_word_guessed("rob", "bol") == False

# Tests different inputs/outputs for get_guessed_word function


def test_get_guessed_word():

    # Tests what outputs will displat with the given letters

    assert get_guessed_word("two", ["t", "o"]) == [
        "t", "_", "o"], "works properly"
    assert get_guessed_word(
        "gosh", ["g", "s", "h"]) == ["g", "_", "s", "h"], "works properly"
    assert get_guessed_word(
        "bowl", ["b"]) == ["b", "_", "_", "_"], "works properly"
    assert get_guessed_word(
        "draw", ["d", "r", "a"]) == ["d", "r", "a", "_"], "works properly"

# Tests different inputs/outputs for is_guess_in_word function


def test_is_guess_in_word():

    # tests if the character shows up in the word

    assert is_guess_in_word("i", "boiling") == True
    assert is_guess_in_word("d", "door") == True
    assert is_guess_in_word("x", "awkward") == False
    assert is_guess_in_word("q", "shame") == False
