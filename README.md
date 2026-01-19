
# SIFRA - Sistema Integrado de Frequência e Assiduidade

Este projeto é um sistema de controle de frequência escolar desenvolvido com:

- **Frontend**: React.js
- **Backend**: Python (FastAPI)
- **Banco de dados**: PostgreSQL

---

## 👨‍💻 Desenvolvedores

- Victor Wingert
- Pedro Sevenini
- João Paulo
- Igor Rocha
- Pedro Leão

---

## 🛠️ Requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

### **Geral**
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) (Recomendado para execução simplificada)
- [PostgreSQL](https://www.postgresql.org/) (Caso opte por rodar o banco localmente fora do Docker)

### **Backend**
- [Python 3.13+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) (Gerenciador de pacotes e ambientes Python ultrarrápido)

### **Frontend**
- [Node.js](https://nodejs.org/) (versão 18+ recomendada)
- [npm](https://www.npmjs.com/) ou [yarn](https://yarnpkg.com/)

---

## 🚀 Como executar o projeto

### 🐳 Via Docker (Mais simples)

Na raiz do projeto, execute:
```bash
docker-compose up --build
```

---

### 📦 Backend (FastAPI + uv)

1. Acesse a pasta `backend`:
```bash
cd backend
```

2. Instale as dependências e crie o ambiente virtual com o `uv`:
```bash
uv sync
```

3. Configure as variáveis de ambiente criando um arquivo `.env` (use o `.env.example` como base):
```bash
cp .env.example .env
```

4. Execute a aplicação em modo de desenvolvimento:
```bash
uv run fastapi dev src/main.py
```
O backend estará disponível em: [http://localhost:8000](http://localhost:8000)

---

### 💻 Frontend (React)

1. Acesse a pasta `frontend`:
```bash
cd frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Inicie o servidor de desenvolvimento:
```bash
npm start
```
O frontend estará disponível em: [http://localhost:3000](http://localhost:3000)

---

## 🌐 Integração Frontend ↔ Backend

Certifique-se de que o backend esteja rodando em `http://localhost:8080` (ou configure o CORS e endpoints conforme o deploy).

Caso necessário, edite o arquivo `frontend/service/api.js` para ajustar a base URL da API:

```js
const api = axios.create({
  baseURL: "http://localhost:8080", // ou URL do servidor
});
```

---

## 🧪 Teste rápido

1. Acesse [http://localhost:3000](http://localhost:3000)
2. Faça login com um usuário válido (verifique se há usuários cadastrados no banco).
3. Utilize as funcionalidades: cadastrar turmas, lançar frequência, etc.

---

## 🛠️ Usuários cadastrados

- Docente:
fabricio@sifra.edu.br / hash123

- Discente:
igor.rocha@estudante.edu.br / hash123

- Coordenador:
helena@sifra.edu.br / hash123

- Admin:
admin@sifra.edu.br / admin123

---

## 📦 Deploy (opcional)

- Banco de dados hospedado no [Render](https://render.com/)
- Frontend pode ser hospedado no [Vercel](https://vercel.com/) ou [Netlify](https://www.netlify.com/)
- Backend pode ser deployado no [Railway](https://railway.app/) ou [Render](https://render.com/)
