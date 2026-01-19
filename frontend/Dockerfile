# Estágio 1: Build da aplicação React
FROM node:18-alpine AS build

WORKDIR /app

# Copia os arquivos de dependências primeiro para aproveitar o cache do Docker
COPY package*.json ./
RUN npm install

# Copia o restante do código e gera o build de produção
COPY . .
RUN npm run build

# Estágio 2: Servindo a aplicação com Nginx
FROM nginx:stable-alpine

# Copia os arquivos compilados do estágio anterior para a pasta do Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expõe a porta 80 (padrão do Nginx)
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
