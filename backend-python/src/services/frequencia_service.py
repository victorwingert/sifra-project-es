from datetime import UTC, datetime
from typing import Any

from fastapi import HTTPException
from sqlmodel import Session, func, select

from ..models import Aula, Discente, Docente, Frequencia, Turma, Usuario
from ..schemas.discente import DiscenteSchema
from ..schemas.frequencia import FrequenciaRequestSchema


class FrequenciaService:
    def get_turmas_docente(self, session: Session, docente_id: int) -> list[Turma]:
        docente = session.get(Docente, docente_id)
        if not docente:
            return []
        return docente.turmas

    def get_turmas_discente(self, session: Session, discente_id: int) -> list[Turma]:
        discente = session.get(Discente, discente_id)
        if not discente:
            return []
        return discente.turmas

    def get_discentes_com_faltas(
        self, session: Session, turma_id: int
    ) -> list[DiscenteSchema]:
        turma = session.get(Turma, turma_id)
        if not turma:
            return []

        result: list[DiscenteSchema] = []
        for d in turma.discentes:
            # Fix: Filter absences correctly using '== False' AND by turma_id
            statement = (
                select(func.count(Frequencia.frequencia_id))  # type: ignore
                .join(Aula)
                .where(
                    Frequencia.discente_id == d.discente_id,
                    not Frequencia.presente,
                    Aula.turma_id == turma_id,
                )
            )
            faltas = session.exec(statement).one()

            usuario = session.get(Usuario, d.discente_id)
            if not usuario:
                continue

            discente_data = d.model_dump()
            discente_data["id"] = discente_data.pop("discente_id")
            discente_data["faltas"] = faltas

            discente_data["nome"] = usuario.nome
            discente_data["email"] = usuario.email
            discente_data["perfil"] = usuario.perfil
            discente_data["telefone"] = usuario.telefone
            discente_data["image"] = usuario.image

            result.append(DiscenteSchema(**discente_data))

        result.sort(key=lambda x: x.nome)
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
        for disc_dto in dto.discentes:
            discente = session.get(Discente, disc_dto.discente_id)
            if not discente:
                raise HTTPException(
                    status_code=404,
                    detail=f"Discente {disc_dto.discente_id} não encontrado",
                )

            frequencia = Frequencia(
                aula_id=aula.aula_id,  # type: ignore
                discente_id=discente.discente_id,  # type: ignore
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
