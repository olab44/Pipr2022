from singer import Artist, Song
import pytest


def test_create_artist():
    singer = Artist('Ed Sheeran', 1991)
    assert singer.name() == 'Ed Sheeran'
    assert singer.birth_year() == 1991
