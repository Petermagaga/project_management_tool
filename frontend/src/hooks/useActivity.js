import { useQuery }
from "@tanstack/react-query";

import {
  getProjectActivity
}
from "../api/activityApi";

export const useActivity =
(projectId) => {

return useQuery({

queryKey:[
"activity",
projectId
],

queryFn: async()=>{

const res =
await getProjectActivity(
projectId
);

return res.data;
},

enabled: !!projectId
});
};