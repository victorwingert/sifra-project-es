import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "../../components/Button/Button";
import "./Perfil.css";
import api from "../../service/api";
import { getUsuarioLogado } from "../../service/usuarioService";

export default function Perfil() {
  const [usuario, setUsuario] = useState(null);
  const [nome, setNome] = useState(null);
  const [email, setEmail] = useState(null);
  const [telefone, setTelefone] = useState(null);
  const [image, setImage] = useState(null);
  const [cargo, setCargo] = useState(null);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  React.useEffect(() => {
    async function carregarUsuario() {
      try {
        const data = await getUsuarioLogado();
        setUsuario(data);
        setNome(data.nome);
        setEmail(data.email);
        setTelefone(data.telefone);
        setImage(data.imagem);
        setCargo(data.tipo_usuario);
      } catch (error) {
        console.error("Erro ao buscar usuário:", error);
      } finally {
        setLoading(false);
      }
    }

    carregarUsuario();
  }, []);


  if (loading) return <p>Carregando...</p>;

  return (
    <div className="flex-container">
      <div className="perfil">
        <div className="bottom">
          <input
            className="editable-input"
            type="text"
            name="nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            readOnly={true}
            disabled={true}
          />
        </div>
      </div>
      <form className="perfil-form">
        <div>
          <label>E-mail</label>
          <input
            type="text"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            readOnly={true}
            disabled={true}
          />
        </div>
        <div>
          <label>Telefone</label>
          <input
            type="text"
            name="telefone"
            value={telefone}
            onChange={(e) => setTelefone(e.target.value)}
            readOnly={true}
            disabled={true}
          />
        </div>
        <div>
          <label>Cargo</label>
          <input
            type="text"
            name="cargo"
            defaultValue={cargo}
            readOnly={true}
            disabled={true}
          />
        </div>
      </form>
      <div className="botoes">
        <div onClick={() => navigate(-1)}>
          <Button value={"Voltar"} backgroundColor={"#000"} color={"#fff"} />
        </div>
      </div>
    </div>
  );
}
