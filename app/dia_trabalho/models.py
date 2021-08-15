import datetime
from dataclasses import dataclass
from enum import Enum
import typing


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
class Batida:
    hora_batida: datetime.time
    tipo: str
    comentario: str
    aprovada: bool


class DiaTrabalho:

    def __init__(self, data: datetime.datetime, horas_para_trabalhar: typing.Union[int, datetime.timedelta], batidas: list = None):

        if isinstance(horas_para_trabalhar, datetime.timedelta):
            self.horas_para_trabalhar = horas_para_trabalhar
        else:
            self.horas_para_trabalhar = datetime.timedelta(hours=horas_para_trabalhar)

        self.data_trabalho = data
        self.batidas = batidas or []
        self.resultado = None

    def bater_ponto(self, tipo: str, comentario: str = '') -> None:
        nova_batida = Batida(hora_batida=datetime.datetime.now().time(),
                                tipo=tipo, comentario=comentario, aprovada=False)
        self.batidas.append(nova_batida)
