import csv
import datetime
import typing

from app.dia_trabalho.models import DiaTrabalho


def extract_dia_trabalho_from_csv(path: str) -> typing.List[DiaTrabalho]:
    if not path.endswith('.csv'):
        path += '.csv'
    registros = []
    with open(path, 'r') as file:
        leitor = csv.DictReader(file)
        for registro in leitor:
            data = datetime.datetime.strptime(registro['data'], '%d/%m/%y').date()
            entrada = datetime.datetime.strptime(
                    registro['entrada'], '%H:%M:%S').time() if registro['entrada'] else None
            pausa = datetime.datetime.strptime(
                    registro['pausa'], '%H:%M:%S').time() if registro['pausa'] else None
            retorno = datetime.datetime.strptime(
                    registro['retorno'], '%H:%M:%S').time() if registro['retorno'] else None
            saida = datetime.datetime.strptime(
                    registro['saida'], '%H:%M:%S').time() if registro['saida'] else None

            registros.append(DiaTrabalho(
                data, entrada, pausa, retorno, saida
            ))
    return registros
