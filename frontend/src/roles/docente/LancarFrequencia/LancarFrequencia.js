import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../../../service/api";
import "./LancarFrequencia.css";
import Button from "../../../components/Button/Button";

export default function LancarFrequencia() {
  const { turmaId } = useParams();
  const [discentes, setDiscentes] = useState([]);
  const [presencas, setPresencas] = useState({});
  const [data, setData] = useState("");
  const navigate = useNavigate();

  React.useEffect(() => {
    async function fetchDiscentes() {
      try {
        const response = await api.get("/frequencia/discentes", {
          params: { turma_id: turmaId },
        });
        setDiscentes(response.data);
        console.log(response.data);
        // Inicializa todos como "presente"
        setPresencas({});
        const presencasIniciais = {};
        response.data.forEach((d) => {
          presencasIniciais[d.discente.usuario.usuario_id] = true;
        });
        setPresencas(presencasIniciais);
      } catch (error) {
        console.error("Erro ao buscar discentes:", error);
      }
    }
    fetchDiscentes();
  }, [turmaId]);

  const handleCheckboxChange = (id) => {
    if (id == null) return; // 🔒 trava total contra undefined/null

    setPresencas((prev) => ({
      ...prev,
      [id]: !prev[id],
    }));
  };

  const handleFinalizar = async () => {
    try {
      const payload = {
        turma_id: parseInt(turmaId),
        data: data, // já está no formato correto
        discentes: Object.entries(presencas)
          .filter(([id]) => !isNaN(parseInt(id))) // 🛡️
          .map(([id, presente]) => ({
            discente_id: parseInt(id),
            presente,
          })),
      };

      console.log("Payload enviado:", payload);

      await api.post("/frequencia/lancar", payload);
      alert("Frequência lançada com sucesso!");
      navigate(-2);
    } catch (error) {
      console.error("Erro ao lançar frequência:", error);
      alert("Erro ao lançar frequência");
    }
  };

  return (
    <div className="flex-container">
      <form className="flex-form">
        <label>Data</label>
        <input
          type="date"
          name="data"
          className="campo"
          placeholder="dd/mm/aaaa"
          onChange={(e) => setData(e.target.value)}
        />
      </form>
      <div className="table-box">
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Matrícula</th>
              <th>Faltas</th>
              <th>Presente</th>
            </tr>
          </thead>
          <tbody>
            {discentes.map((row) => (
              <tr key={row.discente.matricula}>
                <td>{row.discente.usuario.nome}</td>
                <td>{row.discente.matricula}</td>
                <td>{row.faltas}</td>
                <td>
                  <input
                    type="checkbox"
                    checked={presencas[row.discente.usuario.usuario_id] ?? true}
                    onChange={() =>
                      handleCheckboxChange(row.discente.usuario.usuario_id)
                    }
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="botoes">
        <div onClick={() => navigate(-1)}>
          <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
        </div>
        <div onClick={handleFinalizar}>
          <Button
            value={"Finalizar"}
            backgroundColor={"#20BF55"}
            color={"#000"}
          />
        </div>
      </div>
    </div>
  );
}
