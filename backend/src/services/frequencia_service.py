from datetime import UTC, datetime
from typing import Any

from fastapi import HTTPException
from sqlmodel import Session, func, select

from ..models import Aula, Discente, Frequencia, Turma
from ..schemas.frequencia import DiscenteFaltas, FrequenciaRequestSchema


class FrequenciaService:
    def get_discentes_com_faltas(
        self, session: Session, turma_id: int
    ) -> list[DiscenteFaltas]:
        turma = session.get(Turma, turma_id)
        if not turma:
            return []

        result: list[DiscenteFaltas] = []
        for d in turma.discentes:
            statement = (
                select(func.count(Frequencia.frequencia_id))  # type: ignore
                .join(Aula)
                .where(
                    Frequencia.discente_id == d.usuario_id,
                    Frequencia.presente == False,  # noqa: E712
                    Aula.turma_id == turma_id,
                )
            )
            faltas = session.exec(statement).one()

            result.append(DiscenteFaltas(discente=d, faltas=faltas))

        result.sort(key=lambda x: x.discente.usuario.nome if x.discente.usuario else "")
        return result

    def lancar_frequencia(
        self, session: Session, dto: FrequenciaRequestSchema
    ) -> dict[str, Any]:
        turma = session.get(Turma, dto.turma_id)
        if not turma:
            raise HTTPException(status_code=404, detail="Turma não encontrada")

        data_aula = datetime.combine(dto.data, datetime.min.time()).replace(tzinfo=UTC)
        aula = Aula(turma_id=turma.turma_id, data=data_aula)  # type: ignore
        session.add(aula)
        session.commit()
        session.refresh(aula)

        frequencias: list[Frequencia] = []

        ids_matriculados = {d.usuario_id for d in turma.discentes}

        for disc_dto in dto.discentes:
            if disc_dto.discente_id not in ids_matriculados:
                raise HTTPException(
                    status_code=400,
                    detail=f"Discente {disc_dto.discente_id} não está matriculado nesta turma",  # noqa: E501
                )

            discente = session.get(Discente, disc_dto.discente_id)
            if not discente:
                raise HTTPException(
                    status_code=404,
                    detail=f"Discente {disc_dto.discente_id} não encontrado",
                )

            frequencia = Frequencia(
                aula_id=aula.aula_id,  # type: ignore
                discente_id=discente.usuario_id,  # type: ignore
                presente=disc_dto.presente,
            )
            frequencias.append(frequencia)
            session.add(frequencia)

        session.commit()
        return {
            "status": "success",
            "aula_id": aula.aula_id,
            "frequencias_lancadas": len(frequencias),
        }
