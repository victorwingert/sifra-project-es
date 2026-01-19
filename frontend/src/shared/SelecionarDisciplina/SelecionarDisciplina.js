import "./SelecionarDisciplina.css";
import Barra from "../../components/Barra/Barra";
import Button from "../../components/Button/Button";
import api from "../../service/api";
import { getUsuarioLogado } from "../../service/usuarioService";

import { useNavigate } from "react-router";
import React, { useState } from "react";

export default function SelecionarDisciplina() {
  const [usuario, setUsuario] = useState(null);
  const [turmas, setTurmas] = useState([]);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  React.useEffect(() => {
    async function carregarUsuario() {
      try {
        const data = await getUsuarioLogado();
        setUsuario(data);
      } catch (error) {
        console.error("Erro ao buscar usuário:", error);
      } finally {
        setLoading(false);
      }
    }

    carregarUsuario();
  }, []);

  React.useEffect(() => {
    if (!usuario) return; // ⬅️ ESSENCIAL

    async function fetchTurmas() {
      try {
        if (usuario.tipo_usuario === "DOCENTE") {
          const response = await api.get(`/docentes/${usuario.usuario_id}/turmas`);
          setTurmas(response.data);
                  console.log(response.data);

        }
        if (usuario.tipo_usuario === "COORDENADOR") {
          const response = await api.get(`/coordenadores/${usuario.usuario_id}/turmas`);
          setTurmas(response.data);
                  console.log(response.data);

        }
        if (usuario.tipo_usuario === "DISCENTE") {
          const response = await api.get(`/discentes/${usuario.usuario_id}/turmas`);
          setTurmas(response.data);
                  console.log(response.data);

        }
      } catch (error) {
        console.error("Erro ao buscar turmas:", error);
      }
    }
    fetchTurmas();
  }, [usuario]);

  if (loading) return <p>Carregando...</p>;

  return (
    <div className="container">
      <p className="title">Selecione a disciplina desejada: </p>
      <div className="barras">
        {turmas.map((turma) => (
          <div
            key={turma.turma_id}
            onClick={() => navigate(`./${turma.turma_id}`)}
          >
            <Barra
              label={`${turma.disciplina.codigo} - ${turma.disciplina.nome}`}
            />
          </div>
        ))}
      </div>
      <div className="botoes">
        <div onClick={() => navigate(-1)}>
          <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
        </div>
      </div>
    </div>
  );
}
