import { useQuery } from "@tanstack/react-query";

import {
  getWorkspaceProjects,
} from "../api/projectApi";

export const useProjects = (
  workspaceId
) => {

  return useQuery({

    queryKey: [
      "projects",
      workspaceId,
    ],

    queryFn: async () => {

      const res =
        await getWorkspaceProjects(
          workspaceId
        );

      return res.data;
    },

    enabled: !!workspaceId,
  });
};