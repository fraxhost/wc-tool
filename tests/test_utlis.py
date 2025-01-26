import src.utils as utils


def test_get_total_characters_from_content():
    # arrange
    content = 'Hello World!'
    # act
    result = utils.get_total_characters_from_content(content)
    # assert
    assert result == 12


def test_get_total_lines_from_content():
    # arrange
    content = 'Hello World!'
    # act
    result = utils.get_total_lines_from_content(content)
    # assert
    assert result == 1


def test_get_total_words_from_content():
    # arrange
    content = 'Hello World!'
    # act
    result = utils.get_total_words_from_content(content)
    # assert
    assert result == 2


def test_get_total_bytes_from_content():
    # arrange
    content = 'Hello World!'
    # act
    result = utils.get_total_bytes_from_content(content)
    # assert
    assert result == 12