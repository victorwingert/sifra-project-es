import axios from "axios";

const api = axios.create({
  baseURL: "http://5.78.68.22:5070/api/v1",
});

api.interceptors.request.use((config) => {
  if (!config.url.includes("/auth/token")) {
    const usuario = localStorage.getItem("usuarioLogado");

    if (usuario) {
      const { access_token } = JSON.parse(usuario);
      if (access_token) {
        config.headers.Authorization = `Bearer ${access_token}`;
      }
    }
  }

  return config;
});

export default api;
