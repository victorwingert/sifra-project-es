import "./Dashboard.css";
import Card from "../../components/Card/Card";
import React, { useState } from "react";
import { useNavigate } from "react-router";
import { getUsuarioLogado } from "../../service/usuarioService";

export default function Dashboard() {
  const [usuario, setUsuario] = useState(null);
  const [cards, setCards] = useState([]);
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

  switch (usuario.tipo_usuario) {
    case "DOCENTE":
      setCards([
        { label: "Lançar frequência", icon: "check-list.png" },
        { label: "Registro de alunos", icon: "alunos.png" },
        { label: "Minhas informações", icon: "info.png" },
      ]);
      break;

    case "DISCENTE":
      setCards([
        {
          label: "Consultar frequência",
          icon: "consulta.png",
          description: "Verifique seu histórico de faltas",
        },
        { label: "Minhas informações", icon: "info.png" },
      ]);
      break;

    case "ADMIN":
      setCards([
        {
          label: "Cadastrar usuário",
          icon: "editar.png",
          description: "Adicione novos usuários ao sistema com permissões personalizadas",
        },
        {
          label: "Gerenciar usuários",
          icon: "alunos.png",
          description: "Visualize, edite ou remova usuários existentes do sistema",
        },
      ]);
      break;

    case "COORDENADOR":
      setCards([
        { label: "Gerar relatório", icon: "check-list.png" },
        { label: "Minhas informações", icon: "info.png" },
        { label: "Registro de alunos", icon: "alunos.png" },
      ]);
      break;

    default:
      setCards([]);
  }
}, [usuario]);


  // Define as rotas para cada card, de acordo com o perfil
  const getCardRoute = (label) => {
    switch (label) {
      case "Lançar frequência":
        return "./lancarFrequencia";
      case "Consultar frequência":
        return "./consulta";
      case "Minhas informações":
        return "./perfil";
      case "Registro de alunos":
        return "./registro";
      case "Gerar relatório":
        return "./relatorio";
      case "Cadastrar usuário":
        return "./cadastro";
      case "Gerenciar usuários":
        return "./gerenciamento";
      default:
        return "/";
    }
  };

  if (loading) return <p>Carregando...</p>;

  return (
    <>
      <div className="main-dashboard">
        <p className="saudacao">Olá, {usuario.nome}!</p>
        <p className="saudacao-sub">O que você gostaria de fazer hoje?</p>
        <div className="cards">
          {cards.map((info) => (
            <div
              key={info.label}
              onClick={() => navigate(getCardRoute(info.label))}
            >
              <Card
                label={info.label}
                icon={info.icon}
                description={info.description}
              />
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
