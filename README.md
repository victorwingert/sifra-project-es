
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

- [Node.js](https://nodejs.org/) (versão 18+ recomendada)
- [Java JDK](https://adoptopenjdk.net/) (versão 17 ou superior)
- [Maven](https://maven.apache.org/) ou compatível com Spring Boot
- [PostgreSQL](https://www.postgresql.org/) (caso for rodar localmente)

---

## 🚀 Como executar o projeto

### 📦 Backend (Spring Boot)

1. Acesse a pasta `backend`:

```bash
cd backend
```

2. Crie um arquivo `.env` ou configure o `application.properties` com os dados do banco:

Exemplo de `application.properties`:

```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/sifra
spring.datasource.username=postgres
spring.datasource.password=senha
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

> ⚠️ Substitua os dados conforme seu banco.

3. Execute a aplicação:

```bash
./mvnw spring-boot:run
```

Ou, se estiver usando o IntelliJ/VSCode, basta rodar a classe principal: `SifraApplication.java`.

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
maria@ufexemplo.edu / senha123

- Discente:
joao@aluno.ufexemplo.edu / senha456

- Coordenador:
ana@ufexemplo.edu / senha789

- Admin:
admin@ufexemplo.edu / admin123

---

## 📦 Deploy (opcional)

- Banco de dados hospedado no [Render](https://render.com/)
- Frontend pode ser hospedado no [Vercel](https://vercel.com/) ou [Netlify](https://www.netlify.com/)
- Backend pode ser deployado no [Railway](https://railway.app/) ou [Render](https://render.com/)
