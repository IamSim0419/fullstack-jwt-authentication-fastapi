import http from "../api/http";

// Register function that sends a POST request to the backend
export const register = (email: string, password: string) =>
  http.post("auth/register", { email, password });

// Login function that sends a POST request to the backend and stores the token
export const login = async (email: string, password: string) => {
  const res = await http.post("/auth/login", { email, password });
  localStorage.setItem("token", res.data.access_token);
};

export const logout = () => {
  localStorage.removeItem("token");
};
