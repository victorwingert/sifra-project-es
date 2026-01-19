import { useParams, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import api from "../../service/api";
import Button from "../../components/Button/Button";
import "./Relatorio.css";

export default function Relatorio() {
  const { turmaId } = useParams();
  const [discentes, setDiscentes] = useState([]);
  const [turma, setTurma] = useState({});
  const navigate = useNavigate();

  let totalFaltas = 0;
  for (const d of discentes) {
    totalFaltas += d.faltas;
  }
  const media = parseInt(totalFaltas / (discentes.length));
  React.useEffect(() => {
    async function fetchDiscentes() {
      try {
        const response = await api.get("/frequencia/discentes", {
          params: { turma_id: turmaId },
        });
        setDiscentes(response.data);

        const turmas = await api.get("/turmas");
        for(const t of turmas.data){
            if(String(t.turma_id) === String(turmaId)){
                setTurma(t);
                console.log(t)
            }
        }
      } catch (error) {
        console.error("Erro ao buscar discentes:", error);
      }
    }
    fetchDiscentes();
  }, [turmaId]);

  return (
    <div className="flex-container relatorio-container">
      <div className="relatorio-info">
        <p>
          A turma possui {discentes.length} alunos matriculados. A média de
          faltas atual é {media}.
        </p>
        <p>
          <b>Carga horária:</b> {(turma.disciplina?.carga_horaria !== undefined ? turma.disciplina.carga_horaria.toString() : "N/A")} horas
        </p>
        <p>
          <b>Faltas permitidas:</b> {(turma.disciplina?.faltas_permitidas !== undefined ? turma.disciplina.faltas_permitidas.toString() : "N/A")}
        </p>
      </div>
      <div className="table-box relatorio-table">
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Matrícula</th>
              <th>Faltas</th>
            </tr>
          </thead>
          <tbody>
            {discentes.map((row) => (
              <tr key={row.discente.matricula}>
                <td>{row.discente.usuario.nome}</td>
                <td>{row.discente.matricula}</td>
                <td>{row.faltas}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="botoes">
        <div onClick={() => navigate(-1)}>
          <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
        </div>
      </div>
    </div>
  );
}
