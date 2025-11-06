from typing import List

import pytest
from full_match import match

from skelet import TOMLSource, JSONSource
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


def test_repr():
    assert repr(SourcesCollection([TOMLSource('kek.toml')])) == "SourcesCollection([TOMLSource('kek.toml')])"
    assert repr(SourcesCollection([TOMLSource('kek.toml'), JSONSource('lol.json')])) == "SourcesCollection([TOMLSource('kek.toml'), JSONSource('lol.json')])"


def test_type_awared_get():
    assert SourcesCollection([{'key': 'kek'}]).type_awared_get('key', str) == 'kek'
    assert SourcesCollection([{}, {'key': 'kek'}]).type_awared_get('key', str) == 'kek'
    assert SourcesCollection([{}, {'key': 'kek'}, {}]).type_awared_get('key', str) == 'kek'
    assert SourcesCollection([{'key': 123}]).type_awared_get('key', int) == 123
    assert SourcesCollection([{'key': [123, 456]}]).type_awared_get('key', List[int]) == [123, 456]
    assert SourcesCollection([{'key': [123, 456]}]).type_awared_get('key', List) == [123, 456]
    assert SourcesCollection([{'key': [123, 456]}]).type_awared_get('key', list) == [123, 456]

    assert SourcesCollection([{}, {'key': 'kek'}, {}]).type_awared_get('key2', str, default='lol') == 'lol'

    with pytest.raises(TypeError, match=match('The value of the "key" field did not pass the type check.')):
        SourcesCollection([{'key': 123}]).type_awared_get('key', str)

    with pytest.raises(TypeError, match=match('The value of the "key" field did not pass the type check.')):
        SourcesCollection([{'key': '123'}]).type_awared_get('key', int)

    with pytest.raises(TypeError, match=match('The value of the "key" field did not pass the type check.')):
        SourcesCollection([{'key': [123, 456]}]).type_awared_get('key', List[str])

    with pytest.raises(TypeError, match=match('The value of the "key" field did not pass the type check.')):
        SourcesCollection([{'key': ['123', '456']}]).type_awared_get('key', List[int])

    with pytest.raises(KeyError):
        SourcesCollection([{'key': 'kek'}]).type_awared_get('key2', str)

    with pytest.raises(KeyError):
        SourcesCollection([{'key': 'kek'}, {}]).type_awared_get('key2', str)

    with pytest.raises(KeyError):
        SourcesCollection([{}, {'key': 'kek'}, {}]).type_awared_get('key2', str)
