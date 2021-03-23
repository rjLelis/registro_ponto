import datetime
import time
import typing
from enum import Enum

NORMAL_WORK_DAY_IN_SECONDS = 32400
FRIDAY_WORK_DAY_IN_SECONDS = 28800


class TipoResultado(Enum):
    ATRASO = 'Atraso'
    BANCO_HORAS = 'Banco de horas'
    NA = 'Não Aplicável'

    @classmethod
    def handle_resultado(cls, horas_trabalhadas_em_segundos):
        if horas_trabalhadas_em_segundos > 0:
            return cls.BANCO_HORAS
        elif horas_trabalhadas_em_segundos < 0:
            return cls.ATRASO
        return cls.NA

class DiaTrabalho:

    def __init__(self, data: datetime.date,
            entrada: typing.Optional[datetime.time],
            pausa: typing.Optional[datetime.time],
            retorno: typing.Optional[datetime.time],
            saida: typing.Optional[datetime.time]):

        self.data = data
        self.entrada = entrada
        self.pausa = pausa
        self.retorno = retorno
        self.saida = saida
        self.dia_trabalho_segundos = FRIDAY_WORK_DAY_IN_SECONDS if self.data.strftime('%A').upper() == 'FRIDAY' else NORMAL_WORK_DAY_IN_SECONDS

    def calcular_diferenca(self):
        entrada = datetime.datetime.combine(self.data, self.entrada)
        pausa = datetime.datetime.combine(self.data, self.pausa)
        retorno = datetime.datetime.combine(self.data, self.retorno)
        saida = datetime.datetime.combine(self.data, self.saida)

        diff = ((saida - entrada) - (retorno - pausa))

        resultado = self.dia_trabalho_segundos - diff.seconds

        tipo_resultado = TipoResultado.handle_resultado(resultado)

        if resultado < 0:
            resultado = abs(resultado)

        tempo_resultado = time.gmtime(resultado)

        return time.strftime('%H:%M:%S', tempo_resultado), tipo_resultado
