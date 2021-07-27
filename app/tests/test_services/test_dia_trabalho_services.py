import datetime

import pytest
from app.dia_trabalho import models, services


def test_calcular_horas_trabalhadas():
    dia = models.DiaTrabalho(
        data_trabalho=datetime.date(year=2021, month=3, day=23),
        batidas=[datetime.time(hour=9), datetime.time(hour=12),
                datetime.time(hour=13), datetime.time(hour=18),],
        quantidade_horas_trabalho=9,
    )

    resultado = services.calcular_horas_trabalhadas(dia)
    esperado = datetime.timedelta(hours=8)

    assert resultado == esperado


# def test_calcular_horas_modelo_comercial_horario_normal_nao_aplicavel():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=17),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = ('00:00:00', dia_trabalho.TipoResultado.NA)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_horario_normal_nao_aplicavel():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=17),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = ('00:00:00', dia_trabalho.TipoResultado.NA)

#     assert resultado == esperado


# def test_calcular_horas_modelo_normal_nao_aplicavel():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=9),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_normal)
#     esperado = ('00:00:00', dia_trabalho.TipoResultado.NA)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_horario_comercial_atraso():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=23),
#         entrada=datetime.time(hour=8, minute=30),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = ('00:30:00', dia_trabalho.TipoResultado.ATRASO)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_horario_normal_atraso():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8, minute=30),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=17),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = ('00:30:00', dia_trabalho.TipoResultado.ATRASO)

#     assert resultado == esperado


# def test_calcular_horas_modelo_normal_atraso():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=9, minute=30),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_normal)
#     esperado = ('00:30:00', dia_trabalho.TipoResultado.ATRASO)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_horario_comercial_banco_hora():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=23),
#         entrada=datetime.time(hour=7),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = ('01:00:00', dia_trabalho.TipoResultado.BANCO_HORAS)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_horario_normal_banco_hora():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = ('01:00:00', dia_trabalho.TipoResultado.BANCO_HORAS)

#     assert resultado == esperado


# def test_calcular_horas_modelo_normal_banco_hora():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8),
#         pausa=datetime.time(hour=12),
#         retorno=datetime.time(hour=13),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_normal)
#     esperado = ('01:00:00', dia_trabalho.TipoResultado.BANCO_HORAS)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_dia_hoje():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date.today(),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = None

#     assert resultado == esperado


# def test_calcular_horas_modelo_normal_dia_hoje():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date.today(),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_normal)
#     esperado = None

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_registro_sem_par():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8),
#         pausa=datetime.time(hour=12),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = (None, dia_trabalho.TipoResultado.REGISTRO_SEM_PAR)

#     assert resultado == esperado


# def test_calcular_horas_modelo_normal_registro_sem_par():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#         entrada=datetime.time(hour=8),
#         pausa=datetime.time(hour=12),
#         saida=datetime.time(hour=18),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_normal)
#     esperado = (None, dia_trabalho.TipoResultado.REGISTRO_SEM_PAR)

#     assert resultado == esperado


# def test_calcular_horas_modelo_comercial_falta():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_comercial)
#     esperado = (None, dia_trabalho.TipoResultado.FALTA)

#     assert resultado == esperado


# def test_calcular_horas_modelo_normal_falta():
#     dia = dia_trabalho.DiaTrabalho(
#         data=datetime.date(year=2021, month=3, day=19),
#     )

#     resultado = dia_trabalho_service.calcular_horas(dia, dia_trabalho.get_modelo_normal)
#     esperado = (None, dia_trabalho.TipoResultado.FALTA)

#     assert resultado == esperado
