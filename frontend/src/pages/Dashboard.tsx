import { useAuth } from "../auth/AuthContext";

export default function Dashboard() {
  const { logout } = useAuth();

  return (
    <div className="p-6">
      <div className="flex justify-between items-center">
        <h1 className="text-xl font-bold">Dashboard</h1>
        <button
          onClick={logout}
          className="mt-4 bg-red-500 text-white px-4 py-2 hover:bg-red-600 rounded cursor-pointer"
        >
          Logout
        </button>
      </div>

      <h1 className="text-2xl mt-4 font-medium">Welcome to your dashboard!</h1>
    </div>
  );
}
