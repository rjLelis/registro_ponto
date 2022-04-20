import datetime
from dataclasses import dataclass
from enum import Enum
import typing


@dataclass
class Batida:
    hora_batida: datetime.time
    tipo: str
    comentario: str
    aprovada: bool

    def __str__(self) -> str:
        return f'{self.hora_batida} - {self.tipo}'


class DiaTrabalho:

    def __init__(self, data: datetime.date, horas_para_trabalhar: typing.Union[int, datetime.timedelta], batidas: list = None):

        if isinstance(horas_para_trabalhar, datetime.timedelta):
            self.horas_para_trabalhar = horas_para_trabalhar
        else:
            self.horas_para_trabalhar = datetime.timedelta(hours=horas_para_trabalhar)

        self.data_trabalho = data
        self.batidas = batidas or []

    def bater_ponto(self, tipo: str, comentario: str = '') -> None:
        nova_batida = Batida(hora_batida=datetime.datetime.now().time(),
                                tipo=tipo, comentario=comentario, aprovada=False)
        self.batidas.append(nova_batida)

    def ajustar_batida(self):
        pass
