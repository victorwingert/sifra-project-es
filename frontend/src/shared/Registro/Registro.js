import { useParams, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import Button from "../../components/Button/Button";
import api from "../../service/api";

export default function Registro() {
  const { turmaId } = useParams();
  const [discentes, setDiscentes] = useState([]);
  const navigate = useNavigate();

  React.useEffect(() => {
    async function fetchDiscentes() {
      try {
          const response = await api.get("/frequencia/discentes");
          setDiscentes(response.data);
      } catch (error) {
        console.error("Erro ao buscar discentes:", error);
      }
    }
    fetchDiscentes();
  }, [turmaId]);

  return (
    <div className="flex-container">
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
            {discentes.map((row) => (
              <tr key={row.matricula}>
                <td>{row.nome}</td>
                <td>{row.matricula}</td>
                <td>{row.faltas}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>      <div className="botoes">
        <div onClick={() => navigate(-1)}>
          <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
        </div>
      </div>
    </div>
  );
}
