import api from "../api/user_api";

export const register = async (email: string, password: string) =>
  api.post("auth/register", { email, password });

export const login = async (email: string, password: string) => {
  const res = await api.post("auth/login", { email, password });
  localStorage.setItem("token", res.data.access_token);
};

export const logout = () => {
  localStorage.removeItem("token");
};
