import { useQuery }
from "@tanstack/react-query";

import {
  getProjectTasks
}
from "../api/taskApi";

export const useProjectTasks =
(projectId) => {

return useQuery({

queryKey:[
"projectTasks",
projectId
],

queryFn: async()=>{

const res =
await getProjectTasks(
projectId
);

return res.data;
},

enabled: !!projectId
});
};