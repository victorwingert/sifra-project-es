import React, { useState } from "react";
import { useNavigate } from "react-router";
import api from "../../service/api";
import "./Cadastro.css";

export default function CadastroUsuario() {
  const navigate = useNavigate();
  const [perfil, setPerfil] = useState("DOCENTE");
  const [form, setForm] = useState({
    nome: "",
    email: "",
    telefone: "",
    senha: "",
    imagem: "",
    departamento: "", // para docente e coordenador
    matricula: "", // para discente
    curso: "", // para discente
    semestre_ingresso: "", // para discente
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handlePerfilChange = (e) => {
    setPerfil(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    let payload = {
      nome: form.nome,
      email: form.email,
      telefone: form.telefone,
      senha: form.senha,
      imagem: form.imagem,
    };

    if (perfil === "DOCENTE" || perfil === "COORDENADOR") {
      payload.departamento = form.departamento;
    }

    if (perfil === "DISCENTE") {
      payload.matricula = form.matricula;
      payload.curso = form.curso;
      payload.semestre_ingresso = form.semestre_ingresso;
    }

    try {
      if(perfil === "DOCENTE"){
        await api.post(`/docentes/`, payload);
      }
      if(perfil === "COORDENADOR"){
        await api.post(`/coordenadores/`, payload);
      }
      if(perfil === "DISCENTE"){
        await api.post(`/discentes/`, payload);
      }
      alert(`Usuário ${perfil} cadastrado com sucesso.`);
      navigate(-1);
    } catch (error) {
      console.error("Erro ao cadastrar:", error);
      alert("Erro ao cadastrar usuário.");
    }
  };

  return (
    <div className="cadastro-container">
      <h2>Cadastro de Usuário</h2>
      <form onSubmit={handleSubmit} className="form-cadastro">
        <label>Tipo de usuário:</label>
        <select value={perfil} onChange={handlePerfilChange}>
          <option value="DOCENTE">DOCENTE</option>
          <option value="DISCENTE">DISCENTE</option>
          <option value="COORDENADOR">COORDENADOR</option>
        </select>

        <input
          name="nome"
          placeholder="Nome"
          value={form.nome}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <input
          name="telefone"
          placeholder="Telefone"
          value={form.telefone}
          onChange={handleChange}
        />
        <input
          name="senha"
          type="password"
          placeholder="Senha"
          value={form.senha}
          onChange={handleChange}
          required
        />

        {(perfil === "DOCENTE" || perfil === "COORDENADOR") && (
          <input
            name="departamento"
            placeholder="Departamento"
            value={form.departamento}
            onChange={handleChange}
          />
        )}

        {perfil === "DISCENTE" && (
          <>
            <input
              name="matricula"
              placeholder="Matrícula"
              value={form.matricula}
              onChange={handleChange}
            />
            <input
              name="curso"
              placeholder="Curso"
              value={form.curso}
              onChange={handleChange}
            />
            <input
              name="semestre_ingresso"
              placeholder="Semestre de Ingresso"
              value={form.semestre_ingresso}
              onChange={handleChange}
            />
          </>
        )}

        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
}
