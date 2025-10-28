import pytest

from skelet.sources.collection import SourcesCollection


def test_there_is_no_that_key():
    with pytest.raises(KeyError):
        SourcesCollection([{}, {}, {}])['key']


def test_there_is_no_that_key_and_use_get_method():
    assert SourcesCollection([{}, {}, {}]).get('key') is None
    assert SourcesCollection([{}, {}, {}]).get('key', 'value') == 'value'


@pytest.mark.parametrize(
    ['sources'],
    [
        ([{'key': 'value'}, {}, {}],),
        ([{}, {'key': 'value'}, {}],),
        ([{}, {}, {'key': 'value'}],),
    ],
)
def test_there_is_key_in_one_source(sources):
    assert SourcesCollection(sources)['key'] == 'value'
    assert SourcesCollection(sources).get('key') == 'value'
    assert SourcesCollection(sources).get('key', 'another_value') == 'value'


@pytest.mark.parametrize(
    ['sources'],
    [
        ([{'key': 'value'}, {}, {}, {'key': 'second_value'}],),
        ([{}, {'key': 'value'}, {}, {'key': 'second_value'}],),
        ([{}, {}, {'key': 'value'}, {'key': 'second_value'}],),
    ],
)
def test_shading_sources(sources):
    assert SourcesCollection(sources)['key'] == 'value'
    assert SourcesCollection(sources).get('key') == 'value'
    assert SourcesCollection(sources).get('key', 'another_value') == 'value'


def test_simple_proxy():
    assert SourcesCollection([{'lol': 'kek'}])['lol'] == 'kek'

    with pytest.raises(KeyError):
        SourcesCollection([{'lol': 'kek'}])['kek']
