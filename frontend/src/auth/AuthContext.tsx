import { createContext, useContext, useState } from "react";
import * as service from "./auth.service";

interface AuthContextType {
  auth: boolean;
  login: (email: string, pass: string) => Promise<void>;
  register: typeof service.register;
  logout: () => void;
}

// Initialize with an empty object cast as the type so useContext never returns 'null'
const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [auth, setAuth] = useState(!!localStorage.getItem("token"));

  const login = async (email: string, pass: string) => {
    await service.login(email, pass);
    setAuth(true);
  };

  const logout = () => {
    service.logout();
    setAuth(false);
  };

  return (
    <AuthContext.Provider
      value={{ auth, login, logout, register: service.register }}
    >
      {children}
    </AuthContext.Provider>
  );
};

// eslint-disable-next-line react-refresh/only-export-components
export const useAuth = () => useContext(AuthContext);
