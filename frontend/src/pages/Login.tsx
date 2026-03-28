import { useState } from "react";
import { api } from "../api/user_api";
import { saveToken } from "../auth";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const submit = async () => {
    const res = await api.post("/auth/login", {
      email,
      password,
    });

    saveToken(res.data.access_token);
    alert("Login successful!");
  };
  return (
    <div className="h-screen flex items-center justify-center">
      <div className="p-6 bg-white shadow rounded w-80">
        <input
          className="border p-2 w-full mb-3"
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="border p-2 w-full mb-3"
          placeholder="Password"
          type="password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          className="bg-black text-white w-full p-2 rounded cursor-pointer "
          onClick={submit}
        >
          Login
        </button>
      </div>
    </div>
  );
}
