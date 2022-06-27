from datetime import datetime

import pandas as pd
import pytest

from main import filter_data


@pytest.fixture
def raw_data():
    df = pd.DataFrame(
        {
            "nome": [
                "Fulano de tal",
                "Beltrano de Tal",
                "tal",
                "Belano de tal de tal de tal",
                "Ta",
            ],
            "endereço": ["Rua Aurora, 130", "Rua Sol, 980", None, "Rua Lua, 240", None],
            "complemento": ["apto 10", None, None, "casa 2", None],
            "telefone": ["(11) 98767-9956", "986556477886876", "12", "123", 1],
            "cod": [1, 2, 2, 3, 4],
            "data_cadastro": ["12/04/2022", "11/09/1987", None, None, None],
        }
    )

    return df


@pytest.fixture
def config():
    conf = [
        {
            "complemento": {"empty": True, "default_null": "0", "type": "str"},
            "endereço": {"empty": False, "type": "str"},
            "data_cadastro": {
                "empty": False,
                "type": "date",
                "default_null": "date_now",
                "format": "%d%m%Y",
                "separator": "/",
            },
            "telefone": {"empty": False, "type": "str", "min_len": 8},
            "nome": {"empty": False, "type": "str", "min_len": 3, "max_len": 19},
            "cod": {"empty": False, "type": "int", "unique": True},
        }
    ]

    return conf


def test_filter_endereco(raw_data, config):
    data_frame = filter_data(config, raw_data, "")
    assert not data_frame["endereço"].isnull().values.any()
    assert data_frame["endereço"].dtypes == "O"


def test_filter_complemento(raw_data, config):
    data_frame = filter_data(config, raw_data, "")
    assert not data_frame["complemento"].isnull().values.any()
    assert data_frame["complemento"].dtypes == "O"


def test_filter_data_cadastro(raw_data, config):
    data_frame = filter_data(config, raw_data, "")
    assert not data_frame["data_cadastro"].isnull().values.any()
    assert data_frame["data_cadastro"].dtypes == datetime


def test_filter_telefone(raw_data, config):
    data_frame = filter_data(config, raw_data, "")
    assert not data_frame["telefone"].isnull().values.any()
    assert data_frame["telefone"].dtypes == "O"

    counted = data_frame["telefone"].apply(lambda x: len(x))
    for caracters_num in counted:
        assert caracters_num >= 8


def test_filter_nome(raw_data, config):
    data_frame = filter_data(config, raw_data, "")
    assert not data_frame["nome"].isnull().values.any()
    assert data_frame["nome"].dtypes == "O"

    counted = data_frame["nome"].apply(lambda x: len(x))
    for caracters_num in counted:
        assert 3 <= caracters_num < 20


def test_filter_cod(raw_data, config):
    data_frame = filter_data(config, raw_data, "")
    assert not data_frame["cod"].isnull().values.any()
    assert data_frame["cod"].dtypes == int
    assert not data_frame.cod.duplicated().any()
