import {
  useQuery
} from "@tanstack/react-query";

import {
  getProjectBoards
} from "../api/boardApi";

export const useBoards = (
  projectId
) => {

  return useQuery({

    queryKey: [
      "boards",
      projectId
    ],

    queryFn: async () => {

      const res =
        await getProjectBoards(
          projectId
        );

      return res.data;
    },

    enabled:
      !!projectId,
  });
};