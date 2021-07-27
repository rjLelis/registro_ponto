import datetime
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


class Batida:
    data_hora_batida: datetime.time
    tipo: str
    comentario: str
    aprovada: bool


@dataclass
class DiaTrabalho:
    data_trabalho: datetime.date
    batidas: typing.List[Batida]
    quantidade_horas_trabalho: int
    # resultado: typing.Optional[datetime.time]


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
