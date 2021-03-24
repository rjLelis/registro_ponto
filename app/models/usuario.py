from dataclasses import dataclass

from models.dia_trabalho import DiaTrabalho, TipoHorario


@dataclass
class Usuario:
    nome: str
    email: str
    empresa: str
    modelo_horario: TipoHorario
    registros_trabalho: list[DiaTrabalho]
