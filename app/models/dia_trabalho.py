import datetime
import time
import typing
from dataclasses import dataclass
from enum import Enum

COMERCIAL_WORK_DAY_IN_SECONDS = 32400
NORMAL_WORK_DAY_IN_SECONDS = 28800


class TipoResultado(Enum):
    ATRASO = 'Atraso'
    BANCO_HORAS = 'Banco de horas'
    NA = 'Não Aplicável'
    REGISTRO_SEM_PAR = 'Registro de ponto de par'
    FALTA = 'Falta'

    @classmethod
    def handle_resultado(cls, horas_trabalhadas_em_segundos: int) -> 'TipoResultado':
        if horas_trabalhadas_em_segundos > 0:
            return cls.BANCO_HORAS
        elif horas_trabalhadas_em_segundos < 0:
            return cls.ATRASO
        return cls.NA


@dataclass
class DiaTrabalho:
    data: datetime.date
    entrada: typing.Optional[datetime.time] = None
    pausa: typing.Optional[datetime.time] = None
    retorno: typing.Optional[datetime.time] = None
    saida: typing.Optional[datetime.time] = None
    tipo_resultado: typing.Optional[TipoResultado] = None
    resultado: typing.Optional[str] = None


def get_modelo_comercial(dia_trabalho: DiaTrabalho) -> int:
    return NORMAL_WORK_DAY_IN_SECONDS if dia_trabalho.data.strftime('%A').upper() == 'FRIDAY' else COMERCIAL_WORK_DAY_IN_SECONDS


def get_modelo_normal(dia_trabalho: DiaTrabalho) -> int:
    return NORMAL_WORK_DAY_IN_SECONDS


class TipoHorario:
    COMERCIAL = 'comercial'
    NORMAL = 'normal'

    @classmethod
    def get_horario_por_modelo(cls, modelo: 'TipoHorario') -> typing.Callable:
        return {
            cls.COMERCIAL: get_modelo_comercial,
            cls.NORMAL: get_modelo_normal,
        }.get(modelo)
