import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

export default function ProtectedRoute({
  children,
}: {
  children: React.ReactNode;
}) {
  const { auth } = useAuth();
  return auth ? children : <Navigate to="/login" />;
}
