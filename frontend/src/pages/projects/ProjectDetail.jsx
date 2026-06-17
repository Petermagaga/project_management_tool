import {
  useParams
} from "react-router-dom";

import DashboardLayout
from "../../layouts/DashboardLayout";

export default function ProjectDetail() {

  const {
    projectId
  } =
    useParams();

  return (

    <DashboardLayout>

      <h1
        className="
        text-3xl
        font-bold"
      >

        Project {projectId}

      </h1>

    </DashboardLayout>
  );
}