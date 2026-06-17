import DashboardLayout
from "../../layouts/DashboardLayout";

import {
  useProjects
}
from "../../hooks/useProjects";

import ProjectCard
from "../../components/projects/ProjectCard";

import CreateProjectModal
from "../../components/projects/CreateProjectModal";

import {
  useQueryClient
} from "@tanstack/react-query";


export default function Projects() {

  const queryClient =
    useQueryClient();

  const {
    data: projects = [],
    isLoading,
  } =
    useProjects(1);

  const refresh =
    () => {

      queryClient.invalidateQueries(
        ["projects"]
      );
    };

    return (

<DashboardLayout>

<div
className="
flex
justify-between
items-center
mb-6"
>

<h1
className="
text-3xl
font-bold"
>

Projects

</h1>

</div>

<CreateProjectModal

workspaceId={1}

onSuccess={refresh}

/>
{
isLoading ?

(
<div>
Loading...
</div>
)

:

(
<div
className="
grid
grid-cols-3
gap-6"
>

{projects.map(
(project) => (

<ProjectCard

key={project.id}

project={project}

/>
))}
</div>
)
}
</DashboardLayout>
);
}