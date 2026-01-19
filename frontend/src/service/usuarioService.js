import api from "./api";

export async function getUsuarioLogado() {
  const response = await api.get("/usuario/me");
  console.log(response.data);

  return response.data;
}
