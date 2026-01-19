import React, { useState, useEffect } from "react";
import api from "../../service/api";
import icon from "../../assets/icons/excluir.png";
import Button from "../../components/Button/Button";
import { useNavigate } from "react-router";

export default function GerenciarUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchUsuarios();
  }, []);

  const fetchUsuarios = async () => {
    try {
      const response = await api.get("/usuario");
      setUsuarios(response.data);
    } catch (error) {
      console.error("Erro ao buscar usuários:", error);
    }
  };

  const handleExcluir = async (id, perfil) => {
    const confirmar = window.confirm(
      "Tem certeza que deseja excluir este usuário?",
    );
    if (!confirmar) return;

    try {
      if (perfil === "docente") {
        await api.post(`/docentes/${id}`);
      }
      if (perfil === "discente") {
        await api.post(`/discentes/${id}`);
      }
      if (perfil === "coordenador") {
        await api.post(`/coordenadores/${id}`);
      }
      alert("Usuário removido com sucesso.");
      // Atualiza a lista removendo o usuário
      setUsuarios(usuarios.filter((u) => u.id !== id));
    } catch (error) {
      console.error("Erro ao excluir usuário:", error);
      alert("Erro ao excluir usuário.");
    }
  };

  return (
    <div className="flex-container">
      <p className="title">
        <b>Gerenciamento de usuários</b>
      </p>
      <div className="table-box">
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>E-mail</th>
              <th>Cargo</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {usuarios.map((row) => (
              <tr key={row.id}>
                <td>{row.nome}</td>
                <td>{row.email}</td>
                <td>{row.perfil}</td>
                <td>
                  <img
                    src={icon}
                    width={20}
                    style={{ cursor: "pointer" }}
                    alt="Excluir usuário"
                    title="Excluir usuário"
                    onClick={() => handleExcluir(row.id, row.perfil)}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div onClick={() => navigate(-1)}>
        <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
      </div>
    </div>
  );
}
