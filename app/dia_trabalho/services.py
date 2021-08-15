import datetime
import operator

from more_itertools import grouper

from .models import DiaTrabalho


def calcular_horas_trabalhadas(dia_trabalho: DiaTrabalho) -> datetime.timedelta:

    batidas_datetime = [datetime.datetime.combine(dia_trabalho.data_trabalho, batida.hora_batida)
                            for batida in sorted(dia_trabalho.batidas, reverse=True, key=operator.attrgetter('hora_batida'))]

    horas_trabalhadas = datetime.timedelta()
    for batida in grouper(batidas_datetime, 2):
        horas_trabalhadas += (batida[0] - batida[1])

    return horas_trabalhadas


def calcular_horas_restantes(dia_trabalho: DiaTrabalho) -> datetime.timedelta:
    horas_trabalhadas = calcular_horas_trabalhadas(dia_trabalho)
    return dia_trabalho.horas_para_trabalhar - horas_trabalhadas
