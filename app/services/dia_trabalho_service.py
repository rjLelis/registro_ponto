import datetime
import time
import typing

from app.models.dia_trabalho import DiaTrabalho, TipoResultado


def calcular_horas(dia_trabalho: DiaTrabalho, _get_modelo_trabalho: typing.Callable) -> typing.Optional[tuple[typing.Union[None, str], TipoResultado]]:

    if dia_trabalho.data == datetime.date.today():
        return
    elif all(horario is None for horario in [dia_trabalho.entrada, dia_trabalho.pausa, dia_trabalho.retorno, dia_trabalho.saida]):
        return (None, TipoResultado.FALTA)
    elif any([horario is None for horario in [dia_trabalho.entrada, dia_trabalho.pausa, dia_trabalho.retorno, dia_trabalho.saida]]):
        return (None, TipoResultado.REGISTRO_SEM_PAR)

    entrada = datetime.datetime.combine(dia_trabalho.data, dia_trabalho.entrada)
    pausa = datetime.datetime.combine(dia_trabalho.data, dia_trabalho.pausa)
    retorno = datetime.datetime.combine(dia_trabalho.data, dia_trabalho.retorno)
    saida = datetime.datetime.combine(dia_trabalho.data, dia_trabalho.saida)

    diff = ((saida - entrada) - (retorno - pausa))
    print(diff.seconds)

    resultado = diff.seconds - _get_modelo_trabalho(dia_trabalho)

    print(resultado)
    tipo_resultado = TipoResultado.handle_resultado(resultado)

    if resultado < 0:
        resultado = abs(resultado)

    tempo_resultado = time.gmtime(resultado)

    return time.strftime('%H:%M:%S', tempo_resultado), tipo_resultado
