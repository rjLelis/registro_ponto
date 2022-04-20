import datetime
import operator

from more_itertools import grouper

from .models import DiaTrabalho


def calcular_horas(dia_trabalho: DiaTrabalho):
    if len(dia_trabalho) == 1:
        return datetime.timedelta(hours=0), dia_trabalho.horas_para_trabalhar
    if len(dia_trabalho.batidas) % 2 != 0:
        horas_trabalhadas = calcular_batidas_sem_par(dia_trabalho)
        return horas_trabalhadas, calcular_horas_restantes(dia_trabalho, horas_trabalhadas)

    horas_trabalhadas = calcular_horas_trabalhadas(dia_trabalho)

    return horas_trabalhadas, calcular_horas_restantes(dia_trabalho, horas_trabalhadas)


def calcular_horas_trabalhadas(dia_trabalho: DiaTrabalho) -> datetime.timedelta:

    batidas_datetime = [datetime.datetime.combine(dia_trabalho.data_trabalho, batida.hora_batida)
                            for batida in sorted(dia_trabalho.batidas, reverse=True, key=operator.attrgetter('hora_batida'))]

    horas_trabalhadas = datetime.timedelta()
    for batida in grouper(batidas_datetime, 2):
        horas_trabalhadas += (batida[0] - batida[1])

    return horas_trabalhadas


def calcular_horas_restantes(dia_trabalho: DiaTrabalho, horas_trabalhadas: datetime.timedelta) -> datetime.timedelta:
    return dia_trabalho.horas_para_trabalhar - horas_trabalhadas


def calcular_batidas_sem_par(dia_trabalho: DiaTrabalho):
    primeira_batida, ultima_batida = dia_trabalho.batidas[0], dia_trabalho.batidas[-1]
    horas_trabalhadas = (
        datetime.datetime.combine(dia_trabalho.data_trabalho, ultima_batida.hora_batida) -
        datetime.datetime.combine(dia_trabalho.data_trabalho, primeira_batida.hora_batida)
    )
    return horas_trabalhadas
