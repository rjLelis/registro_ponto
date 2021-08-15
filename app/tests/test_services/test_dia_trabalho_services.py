import datetime
import random

import pytest
from app.dia_trabalho import models, services


def test_calcular_horas_trabalhadas():
    dia = models.DiaTrabalho(
        data=datetime.date(year=2021, month=3, day=23),
        batidas=[models.Batida(datetime.time(hour=9), 'entrada', '', True),
                models.Batida(datetime.time(hour=12), 'almoço', '', True),
                models.Batida(datetime.time(hour=13), 'volta', '', True),
                models.Batida(datetime.time(hour=18), 'saida', '', True),],
        quantidade_horas_trabalho=8,
    )

    resultado = services.calcular_horas_trabalhadas(dia)
    esperado = datetime.timedelta(hours=8)

    assert resultado == esperado


def test_calcular_horas_trabalhadas_batidas_fora_de_ordem():

    batidas = random.sample([models.Batida(datetime.time(hour=9), 'entrada', '', True),
                            models.Batida(datetime.time(hour=12), 'almoço', '', True),
                            models.Batida(datetime.time(hour=13), 'volta', '', True),
                            models.Batida(datetime.time(hour=18), 'saida', '', True),], 4)
    dia = models.DiaTrabalho(
        data=datetime.date(year=2021, month=3, day=23),
        batidas=batidas,
        quantidade_horas_trabalho=8,
    )

    resultado = services.calcular_horas_trabalhadas(dia)
    esperado = datetime.timedelta(hours=8)

    assert resultado == esperado


def test_calcular_horas_trabalhadas_pausa_nao_compensada():
    dia = models.DiaTrabalho(
        data=datetime.date(year=2021, month=3, day=23),
        batidas=[models.Batida(datetime.time(hour=9), 'entrada', '', True),
                models.Batida(datetime.time(hour=12), 'almoço', '', True),
                models.Batida(datetime.time(hour=13), 'volta', '', True),
                models.Batida(datetime.time(hour=16), 'pausa', '', True),
                models.Batida(datetime.time(hour=16, minute=30), 'volta', '', True),
                models.Batida(datetime.time(hour=18), 'saida', '', True),],
        quantidade_horas_trabalho=8,
    )

    resultado = services.calcular_horas_trabalhadas(dia)
    esperado = datetime.timedelta(hours=7, minutes=30)

    assert resultado == esperado


def test_calcular_horas_trabalhadas_pausa_compensada():
    dia = models.DiaTrabalho(
        data=datetime.date(year=2021, month=3, day=23),
        batidas=[models.Batida(datetime.time(hour=9), 'entrada', '', True),
                models.Batida(datetime.time(hour=12), 'almoço', '', True),
                models.Batida(datetime.time(hour=13), 'volta', '', True),
                models.Batida(datetime.time(hour=16), 'pausa', '', True),
                models.Batida(datetime.time(hour=16, minute=30), 'volta', '', True),
                models.Batida(datetime.time(hour=18, minute=30), 'saida', '', True),],
        quantidade_horas_trabalho=8,
    )

    resultado = services.calcular_horas_trabalhadas(dia)
    esperado = datetime.timedelta(hours=8)

    assert resultado == esperado
