import api from "./axios";

export const getProjectActivity = (
  projectId
) =>
  api.get(
    `activity/project/${projectId}/`
  );