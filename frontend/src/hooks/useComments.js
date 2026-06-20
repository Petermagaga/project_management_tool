import { useQuery }
from "@tanstack/react-query";

import {
  getTaskComments
}
from "../api/commentApi";

export const useComments =
(taskId) => {

return useQuery({

queryKey:[
"comments",
taskId
],

queryFn: async()=>{

const res =
await getTaskComments(
taskId
);

return res.data;
},

enabled: !!taskId
});
};