import datetime

import pytest

from app.dia_trabalho.models import DiaTrabalho


def test_bater_ponto():
    dia_trabalho = DiaTrabalho(datetime.date.today(), datetime.timedelta(hours=8))
    dia_trabalho.bater_ponto('entrada')

    assert len(dia_trabalho.batidas) > 0
    assert dia_trabalho.batidas[0].hora_batida.hour == datetime.datetime.now().time().hour
