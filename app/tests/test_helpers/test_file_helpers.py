from pathlib import Path

import pytest
from app.helpers import file_helpers


@pytest.fixture
def base_dir():
    return Path(__file__).resolve().parent.parent


def test_extract_dia_trabalho_from_csv_with_extension(base_dir):
    resultado = file_helpers.extract_dia_trabalho_from_csv(f'{base_dir}/fixtures/registro_ponto_fixture_with_data.csv')

    assert type(resultado) == list
    assert len(resultado) > 0


def test_extract_dia_trabalho_from_csv_without_extension(base_dir):
    resultado = file_helpers.extract_dia_trabalho_from_csv(f'{base_dir}/fixtures/registro_ponto_fixture_with_data')

    assert type(resultado) == list
    assert len(resultado) > 0


def test_extract_dia_trabalho_from_csv_empty(base_dir):
    resultado = file_helpers.extract_dia_trabalho_from_csv(f'{base_dir}/fixtures/registro_ponto_fixture_empty')

    assert type(resultado) == list
    assert len(resultado) == 0
