import Login from "./pages/Login";

function App() {
  return (
    <>
      <main>
        <h1 className="text-2xl font-bold bg-black text-white">
          Welcome to My App
        </h1>
        <p>This is a simple JWT authentication app.</p>
        <Login />
      </main>
    </>
  );
}

export default App;
