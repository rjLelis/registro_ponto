import datetime

from more_itertools import grouper

from .models import DiaTrabalho

def calcular_horas_trabalhadas(dia_trabalho: DiaTrabalho) -> datetime.timedelta:

    if dia_trabalho.data_trabalho == datetime.date.today():
        return
    elif not dia_trabalho.batidas:
        return None
    elif len(dia_trabalho.batidas) % 2 != 0:
        return None

    batidas_datetime = [datetime.datetime.combine(dia_trabalho.data_trabalho, batida)
                            for batida in dia_trabalho.batidas[::-1]]
    horas_trabalhadas: datetime.timedelta = None
    for batida in grouper(batidas_datetime, 2):
        if horas_trabalhadas:
            horas_trabalhadas += (batida[0] - batida[1])
            continue
        horas_trabalhadas = (batida[0] - batida[1])

    return horas_trabalhadas
