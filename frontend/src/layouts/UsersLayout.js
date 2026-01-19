import "./Layouts.css";

import { Outlet } from "react-router-dom";
import Header from "../components/Header/Header";
import React from "react";
import { getUsuarioLogado } from "../service/usuarioService";
import { useState } from "react";

const UsersLayout = () => {

  const [usuario, setUsuario] = useState(null);
  const [loading, setLoading] = useState(true);

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

  if (loading) return <p>Carregando...</p>;

  return (
    <>
      <Header username={usuario.nome}/>

      <div className="users-layout">
        <Outlet />
      </div>

      <footer>
        <small>&copy; 2025 - SIFRA</small>
      </footer>
    </>
  );
};

export default UsersLayout;
