import React, { useState, useEffect } from "react";
import api from "../../service/api";
import iconExcluir from "../../assets/icons/excluir.png";
import iconEditar from "../../assets/icons/editar.png";
import Button from "../../components/Button/Button";
import { useNavigate } from "react-router";
import "./GerenciarUsuarios.css";
import "./Cadastro.css"; // Reutilizando estilos de formulário

export default function GerenciarUsuarios() {
  const [usuarios, setUsuarios] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [editingUser, setEditingUser] = useState(null);
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

  const handleExcluir = async (id, tipo_usuario) => {
    const confirmar = window.confirm(
      "Tem certeza que deseja excluir este usuário?"
    );
    if (!confirmar) return;

    const endpointMap = {
      DOCENTE: "docentes",
      DISCENTE: "discentes",
      COORDENADOR: "coordenadores",
    };

    const endpoint = endpointMap[tipo_usuario];

    if (!endpoint) {
      alert("Tipo de usuário desconhecido.");
      return;
    }

    try {
      await api.delete(`/${endpoint}/${id}`);
      alert("Usuário removido com sucesso.");
      setUsuarios(usuarios.filter((u) => u.usuario_id !== id));
    } catch (error) {
      console.error("Erro ao excluir usuário:", error);
      alert("Erro ao excluir usuário.");
    }
  };

  const handleEdit = (user) => {
    setEditingUser({ ...user });
    setModalOpen(true);
  };

  const handleSaveEdit = async (e) => {
    e.preventDefault();
    if (!editingUser) return;

    const endpointMap = {
      DOCENTE: "docentes",
      DISCENTE: "discentes",
      COORDENADOR: "coordenadores",
    };

    const endpoint = endpointMap[editingUser.tipo_usuario];

    if (!endpoint) {
      alert("Tipo de usuário desconhecido.");
      return;
    }

    // Filtra apenas os campos que podem ser editados no UsuarioBase + specificos se houver
    const payload = {
        nome: editingUser.nome,
        email: editingUser.email,
        telefone: editingUser.telefone,
        imagem: editingUser.imagem,
        // Adicione outros campos se o backend suportar e o form tiver inputs
    };

    try {
      await api.patch(`/${endpoint}/${editingUser.usuario_id}`, payload);
      alert("Usuário atualizado com sucesso!");
      setModalOpen(false);
      fetchUsuarios(); // Recarrega a lista
    } catch (error) {
      console.error("Erro ao atualizar usuário:", error);
      alert("Erro ao atualizar usuário.");
    }
  };

  const handleChange = (e) => {
    setEditingUser({ ...editingUser, [e.target.name]: e.target.value });
  };

  return (
    <div className="flex-container gerenciar-container">
      <p className="title">
        <b>Gerenciamento de usuários</b>
      </p>

      {/* Modal de Edição Simplificado */}
      {modalOpen && (
        <div className="modal-overlay">
          <div className="modal-content cadastro-container" style={{maxWidth: '500px', margin: '0 auto'}}>
            <h3>Editar Usuário</h3>
            <form onSubmit={handleSaveEdit} className="form-cadastro">
                <label>Nome</label>
                <input
                    name="nome"
                    value={editingUser.nome}
                    onChange={handleChange}
                    required
                />
                <label>E-mail</label>
                <input
                    name="email"
                    value={editingUser.email}
                    onChange={handleChange}
                    required
                />
                 <label>Telefone</label>
                <input
                    name="telefone"
                    value={editingUser.telefone || ""}
                    onChange={handleChange}
                />
                
                <div style={{display: 'flex', gap: '10px', marginTop: '10px'}}>
                     <button type="submit" style={{flex: 1}}>Salvar</button>
                     <button type="button" onClick={() => setModalOpen(false)} style={{flex: 1, backgroundColor: '#ccc'}}>Cancelar</button>
                </div>
            </form>
          </div>
        </div>
      )}

      <div className="table-box gerenciar-table">
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
              <tr key={row.usuario_id}>
                <td>{row.nome}</td>
                <td>{row.email}</td>
                <td>{row.tipo_usuario}</td>
                <td>
                  <img
                    src={iconEditar}
                    width={20}
                    style={{ cursor: "pointer", marginRight: "10px", backgroundColor: "#ccc", borderRadius: "4px", padding: "2px" }}
                    alt="Editar usuário"
                    title="Editar usuário"
                    onClick={() => handleEdit(row)}
                  />
                  <img
                    src={iconExcluir}
                    width={20}
                    style={{ cursor: "pointer" }}
                    alt="Excluir usuário"
                    title="Excluir usuário"
                    onClick={() => handleExcluir(row.usuario_id, row.tipo_usuario)}
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
      
      <style>{`
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0,0,0,0.5);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        .modal-content {
            background: white;
            padding: 20px;
            border-radius: 8px;
            width: 90%;
            max-width: 500px;
        }
      `}</style>
    </div>
  );
}