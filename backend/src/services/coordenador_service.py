from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from ..models import Coordenador, Disciplina, Docente, Turma, Usuario
from ..schemas.coordenador import CoordenadorCreate, CoordenadorRead, CoordenadorUpdate


class CoordenadorService:
    def get_turmas(self, session: Session, usuario_id: int) -> list[Turma] | None:
        coordenador = session.get(Coordenador, usuario_id)
        if not coordenador:
            return None

        # Retorna turmas vinculadas ao departamento do coordenador
        # A lógica aqui assume que turmas são de disciplinas que pertencem a docentes do mesmo departamento
        # Ou simplesmente todas as turmas se não houver filtro de departamento estrito implementado ainda.
        # Para simplificar e atender a solicitação "registro de alunos do coordenador":
        # Vamos retornar TODAS as turmas para o coordenador poder gerenciar qualquer uma.
        
        statement = select(Turma).options(selectinload(Turma.disciplina))
        return list(session.exec(statement).all())

    def create_coordenador(
        self, session: Session, data: CoordenadorCreate
    ) -> CoordenadorRead:
        statement = select(Usuario).where(Usuario.email == data.email)
        if session.exec(statement).first():
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

        db_usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=data.senha,
            telefone=data.telefone,
            imagem=data.imagem,
            tipo_usuario="COORDENADOR",
        )
        session.add(db_usuario)
        session.flush()
        session.refresh(db_usuario)

        db_coordenador = Coordenador(
            usuario_id=db_usuario.usuario_id,
            departamento=data.departamento,
        )
        session.add(db_coordenador)
        session.commit()
        session.refresh(db_coordenador)
        
        return CoordenadorRead(
            id=db_usuario.usuario_id,  # type: ignore
            nome=db_usuario.nome,
            email=db_usuario.email,
            telefone=db_usuario.telefone,
            imagem=db_usuario.imagem,
            tipo_usuario=db_usuario.tipo_usuario,
            departamento=db_coordenador.departamento,
        )

    def update_coordenador(
        self, session: Session, usuario_id: int, data: CoordenadorUpdate
    ) -> CoordenadorRead | None:
        db_coordenador = session.get(Coordenador, usuario_id)
        if not db_coordenador:
            return None

        db_usuario = session.get(Usuario, usuario_id)
        if db_usuario:
            usuario_data = data.model_dump(exclude_unset=True)
            base_data = {
                k: v
                for k, v in usuario_data.items()
                if k in ["nome", "sobrenome", "email", "telefone", "imagem"]
            }
            db_usuario.sqlmodel_update(base_data)
            session.add(db_usuario)

        coordenador_data = data.model_dump(exclude_unset=True)
        if "departamento" in coordenador_data:
            db_coordenador.departamento = coordenador_data["departamento"]

        session.add(db_coordenador)
        session.commit()
        session.refresh(db_coordenador)
        
        if db_usuario:
            return CoordenadorRead(
                id=db_usuario.usuario_id,  # type: ignore
                nome=db_usuario.nome,
                email=db_usuario.email,
                telefone=db_usuario.telefone,
                imagem=db_usuario.imagem,
                tipo_usuario=db_usuario.tipo_usuario,
                departamento=db_coordenador.departamento,
            )
        return None
