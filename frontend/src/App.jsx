import {
  Routes,
  Route
}
from "react-router-dom";

import ProjectDetail
from "./pages/projects/ProjectDetail";

import Login
from "./pages/auth/Login";

import Register
from "./pages/auth/Register";

import Dashboard
from "./pages/dashboard/Dashboard";

import ProtectedRoute
from "./routes/ProtectedRoute";
import Projects
from "./pages/projects/Projects";

function App() {

  return (

    <Routes>

      <Route
        path="/login"
        element={<Login />}
      />

      <Route
        path="/register"
        element={<Register />}
      />

      <Route
        path="/"
        element={
          <ProtectedRoute>

            <Dashboard />

          </ProtectedRoute>
        }
      />

    

    <Route
      path="/projects"
      element={
        <ProtectedRoute>
          <Projects />
        </ProtectedRoute>
      }
    />



<Route

path="/projects/:projectId"

element={

<ProtectedRoute>

<ProjectDetail />

</ProtectedRoute>

}

/>


</Routes>
  );
}

export default App;