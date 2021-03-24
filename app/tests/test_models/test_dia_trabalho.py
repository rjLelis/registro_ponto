import datetime

import pytest
from app.models import dia_trabalho


def test_horas_trabalhadas_maior_que_zero():
    resultado = dia_trabalho.TipoResultado.handle_resultado(123)
    esperado = dia_trabalho.TipoResultado.BANCO_HORAS

    assert resultado == esperado


def test_horas_trabalhadas_menor_que_zero():
    resultado = dia_trabalho.TipoResultado.handle_resultado(-123)
    esperado = dia_trabalho.TipoResultado.ATRASO

    assert resultado == esperado


def test_tipo_resultado_nao_aplicavel():
    resultado = dia_trabalho.TipoResultado.handle_resultado(0)
    esperado = dia_trabalho.TipoResultado.NA

    assert resultado == esperado


def test_get_modelo_comercial_horas_normais():
    dia = dia_trabalho.DiaTrabalho(
        data=datetime.datetime(year=2021, month=3, day=26),
    )

    resultado = dia_trabalho.get_modelo_comercial(dia)
    esperado = dia_trabalho.NORMAL_WORK_DAY_IN_SECONDS

    assert resultado == esperado


def test_get_modelo_comercial_horas_comerciais():
    dia = dia_trabalho.DiaTrabalho(
        data=datetime.datetime(year=2021, month=3, day=24),
    )

    resultado = dia_trabalho.get_modelo_comercial(dia)
    esperado = dia_trabalho.COMERCIAL_WORK_DAY_IN_SECONDS

    assert resultado == esperado


def test_get_modelo_normal():
    dia = dia_trabalho.DiaTrabalho(
        data=datetime.datetime(year=2021, month=3, day=24),
    )

    resultado = dia_trabalho.get_modelo_normal(dia)
    esperado = dia_trabalho.NORMAL_WORK_DAY_IN_SECONDS

    assert resultado == esperado


def test_get_horario_por_modelo_comercial():
    resultado = dia_trabalho.TipoHorario.get_horario_por_modelo(dia_trabalho.TipoHorario.COMERCIAL).__name__
    esperado = 'get_modelo_comercial'

    assert resultado == esperado


def test_get_horario_por_modelo_comercial():
    resultado = dia_trabalho.TipoHorario.get_horario_por_modelo(dia_trabalho.TipoHorario.NORMAL).__name__
    esperado = 'get_modelo_normal'

    assert resultado == esperado
