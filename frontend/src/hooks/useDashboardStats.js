import { useProjects }
from "./useProjects";

import {
  useProjectTasks
}
from "./useProjectTasks";

export const useDashboardStats =
(
workspaceId,
projectId
) => {

const {
data: projects=[]
}
=
useProjects(
workspaceId
);

const {
data: tasks=[]
}
=
useProjectTasks(
projectId
);

return {

totalProjects:
projects.length,

totalTasks:
tasks.length,

completedTasks:
tasks.filter(

t =>
t.board_name ===
"Done"

).length,

};
};