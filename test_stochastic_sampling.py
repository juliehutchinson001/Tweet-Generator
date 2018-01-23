from stochastic_sampling import get_random_word
from histogram_dictionary import Histogram
import pytest

def test_relative_probabilities():
    histogram = Histogram('one fish two fish three fish four fish')
    random_words = ''
    for _ in range(100):
        random_words += get_random_word(histogram.histogram) + ' '
    
    test_histogram = Histogram(random_words.strip())
    assert len(test_histogram.histogram) == 5
    assert sum(test_histogram.histogram.values()) == 100
    assert test_histogram.histogram['fish'] >= 40
    assert test_histogram.histogram['fish'] <= 75
    assert test_histogram.histogram['one'] <= 20
    assert test_histogram.histogram['two'] <= 20
    assert test_histogram.histogram['three'] <= 20
    assert test_histogram.histogram['four'] <= 20
    assert test_histogram.histogram['four'] > 2

def test_with_types_that_dont_exist():
    histogram = Histogram('one fish two fish three fish four fish')
    assert get_random_word(histogram.histogram) != 'hello'
    assert get_random_word(histogram.histogram) != 'fis'

def test_correct_type():
    histogram = Histogram('one fish two fish three fish four fish')
    assert type(get_random_word(histogram.histogram)) == str

def test_random_word_is_none_with_empty_histogram():
    assert get_random_word({}) == None