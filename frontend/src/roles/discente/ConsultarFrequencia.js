import { useParams, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import api from "../../service/api";
import Button from "../../components/Button/Button";
import { getUsuarioLogado } from "../../service/usuarioService";

export default function ConsultarFrequencia() {
  const [usuario, setUsuario] = useState(null);
  const { turmaId } = useParams();
  const [discente, setDiscente] = useState({});
  const [turma, setTurma] = useState({});
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

    async function fetchDiscentes() {
      try {
        const response = await api.get("/frequencia/discentes", {
          params: { turma_id: turmaId },
        });
        const discenteEncontrado = response.data.find(
          (d) => d.nome === usuario.nome,
        );
        if (discenteEncontrado) {
          setDiscente(discenteEncontrado);
        }

        const turmas = await api.get("/turmas");
        for (const t of turmas.data) {
          if (String(t.id) === String(turmaId)) {
            setTurma(t);
            console.log(t);
          }
        }
      } catch (error) {
        console.error("Erro ao buscar discente:", error);
      }
    }
    fetchDiscentes();
  }, [turmaId, usuario]);
  
  if (loading) return <p>Carregando...</p>;

  return (
    <div className="flex-container">
      <p style={{ fontWeight: 600 }}>
        Você possui {discente.faltas} falta(s) nesta disciplina. O total de
        faltas permitido é{" "}
        {(turma?.disciplina?.faltasPermitidas ?? "N/A").toString()}.
      </p>
      <div className="table-box">
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Matrícula</th>
              <th>Faltas</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{discente.nome}</td>
              <td>{discente.matricula}</td>
              <td>{discente.faltas}</td>
            </tr>
          </tbody>
        </table>
      </div>{" "}
      <div className="botoes">
        <div onClick={() => navigate(-1)}>
          <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
        </div>
      </div>
    </div>
  );
}
