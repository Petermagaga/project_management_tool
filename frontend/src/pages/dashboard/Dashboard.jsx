import DashboardLayout
from "../../layouts/DashboardLayout";

import {
  useAuth
}
from "../../contexts/AuthContext";


export default function Dashboard() {

  const {
    user,
  } = useAuth();

  return (

    <DashboardLayout>

      <h1
        className="
        text-3xl
        font-bold"
      >

        Welcome,
        {user?.first_name ||
         user?.username}

      </h1>

      <p
        className="
        text-gray-500
        mt-2"
      >

        Project overview dashboard

      </p>

    </DashboardLayout>
  );
}