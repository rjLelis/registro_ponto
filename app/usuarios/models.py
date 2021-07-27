from dataclasses import dataclass
import typing



@dataclass
class Usuario:
    nome: str
    email: str
    empresa: str
    modelo_horario: typing.Any
