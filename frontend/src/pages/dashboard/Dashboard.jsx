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

<div className="grid grid-cols-4 gap-6 mt-8">

  <div className="bg-white p-5 rounded-xl">

    <h2>Total Projects</h2>

    <p className="text-3xl font-bold">
      0
    </p>

  </div>

  <div className="bg-white p-5 rounded-xl">

    <h2>Total Tasks</h2>

    <p className="text-3xl font-bold">
      0
    </p>

  </div>

  <div className="bg-white p-5 rounded-xl">

    <h2>Completed</h2>

    <p className="text-3xl font-bold">
      0
    </p>

  </div>

  <div className="bg-white p-5 rounded-xl">

    <h2>Overdue</h2>

    <p className="text-3xl font-bold">
      0
    </p>

  </div>

</div>

    </DashboardLayout>
  );
}