from datetime import datetime

import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer

from musics.validators import ean_is_valid


def test_cd_name_of_length_51_raises_exception(db):
    cd = mixer.blend('musics.CD', name="B" * 51)
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


def test_cd_empty_name_exception(db):
    cd = mixer.blend('musics.CD', name="")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


def test_cd_contains_wrong_char(db):
    cd = mixer.blend('musics.CD', name="Pink@Floyd!")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


# ARTIST
def test_cd_artist_name_of_length_51_raises_exception(db):
    cd = mixer.blend('musics.CD', artist="B" * 51)
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


def test_cd_empty_artist_name_raises_exception(db):
    cd = mixer.blend('musics.CD', artist="")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


def test_cd_artist_name_contains_wrong_chars_raises_exception(db):
    cd = mixer.blend('musics.CD', artist="John!@\nLennon")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

#RECORD_COMPANY
def test_cd_record_company_of_length_51_raises_exceptions(db):
    cd = mixer.blend('musics.CD', record_company="B" * 51)
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


def test_cd_empty_record_company_name_raises_exceptions(db):
    cd = mixer.blend('musics.CD', record_company="" * 51)
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

def test_cd_record_company_name_contains_wrong_chars_raises_exceptions(db):
    cd = mixer.blend('musics.CD', record_company="SonyMusic@@@")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()


#GENRE
def test_cd_genre_of_length_26_raises_exceptions(db):
    cd = mixer.blend('musics.CD', genre="B" * 26)
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

def test_cd_empty_genre_raises_exceptions(db):
    cd = mixer.blend('musics.CD', genre="")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

def test_cd_genre_contains_wrong_chars_raises_exception(db):
    cd = mixer.blend('musics.CD', genre = "Rock@")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

def test_cd_genre_first_letter_is_uppser(db):
    cd = mixer.blend('musics.CD',genre="rock")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

#TODO: eancode,published_by
def test_correct_ean_code(db):
    cd = mixer.blend('musics.CD',ean_code="978020137962")
    assert ean_is_valid(cd.ean_code)

def test_cd_wrong_ean_code(db):
    cd = mixer.blend('musics.CD',ean_code="978020137963A")
    with pytest.raises(ValidationError) as err:
        cd.full_clean()

def test_cd_price_0_raises_exceptions(db):
    cd = mixer.blend('musics.CD',price=0)
    with pytest.raises(Exception) as err:
        cd.full_clean()

def test_cd_price_more_than_2_decimal_raises_exceptions(db):
    cd = mixer.blend('musics.CD',price=10.001)
    with pytest.raises(Exception) as err:
        cd.full_clean()

def test_cd_price_10001_raises_exceptions(db):
    cd = mixer.blend('musics.CD',price=10001.00)
    with pytest.raises(Exception) as err:
        cd.full_clean()

def test_cd_created_at_today_is_equal_at_actual_date(db):
    cd = mixer.blend('musics.CD')
    assert cd.created_at.day == datetime.now().day
    assert cd.created_at.month == datetime.now().month
    assert cd.created_at.year == datetime.now().year

def test_cd_created_at_is_equal_at_updated_at_at_first_time(db):
    cd = mixer.blend('musics.CD')
    assert cd.created_at == cd.updated_at

# def test_cd_updated_at_changes_when_entry_is_updated(db):
#     cd = mixer.blend('musics.CD',name="Rino")
#     name_before_update = cd.name
#     cd.name = "Rinuzzo Gaetano"
#     datetime_before_update = cd.updated_at
#     cd.save()
#     assert datetime_before_update != cd.updated_at


