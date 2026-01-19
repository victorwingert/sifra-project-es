from datetime import date

from pydantic import BaseModel

from ..schemas.discente import DiscenteComUsuario


class FrequenciaDiscenteSchema(BaseModel):
    discente_id: int
    presente: bool


class FrequenciaRequestSchema(BaseModel):
    turma_id: int
    data: date
    discentes: list[FrequenciaDiscenteSchema]


class DiscenteFaltas(BaseModel):
    discente: DiscenteComUsuario
    faltas: int
