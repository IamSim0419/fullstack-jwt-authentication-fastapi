import { createContext, useContext, useState } from "react";
import * as auth from "./authService";

interface AuthContextType {
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType>(null!);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isAuthenticated, setAuth] = useState(
    localStorage.getItem("token") ? true : false,
  );

  const login = async (email: string, password: string) => {
    await auth.login(email, password);
    setAuth(true);
  };

  const register = async (email: string, password: string) => {
    await auth.register(email, password);
    setAuth(true);
  };

  const logout = () => {
    auth.logout();
    setAuth(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
