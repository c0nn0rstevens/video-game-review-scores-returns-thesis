import pytest
from src.data_sources.igdb.authentication import AuthIGDB


def test_env_variable_import():
    auth = AuthIGDB()
    assert auth.client_id != None
    assert auth.client_secret != None
