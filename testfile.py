from spaceman import is_word_guessed, is_guess_in_word, get_guessed_word


def test_is_word_guessed():
    letters_guessed = ["d", "o", "g"]
    secret_word = "dog"
    assert is_word_guessed(
        secret_word, letters_guessed) == True, "is_word_guessed function not working"
    letters_guessed = ["d", "o", "g"]
    assert is_word_guessed(
        secret_word, letters_guessed) == False, "Doesn't return false on incorrect guess"


def test_is_guess_in_word():
    # Test setup
    secret_word = ["d", "o", "g"]

    # Test to make sure it works
    assert is_guess_in_word(
        "o", secret_word) == True, "Guess in word not finding character"

    # Test for incorrect returning false
    assert is_guess_in_word(
        "w", secret_word) == False, "Returing other than false on incorrect test"


def test_get_guessed_word():
    # Test setup
    secret_word = ["d", "o", "g"]
    letters_guess_so_far = ["d", "g"]

    # Test to make sure it works
    assert get_guessed_word(
        secret_word, letters_guess_so_far) == "d_g", "returning correct statement"
    # Test incorrect
    assert get_guessed_word(
        secret_word, letters_guess_so_far) != "__g", "Returning incorrect string"


if __name__ == "__main__":
    # Run the test function
    # test_is_word_guessed()
    # test_is_guess_in_word()
    # test_get_guessed_word()
    running = True
    while running:
        spaceman(load_word())
        running = play_again()
