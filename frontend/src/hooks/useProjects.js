
import api from "../api/axios";

export const getWorkspaceProjects = (workspaceId) =>
  api.get(`projects/workspace/${workspaceId}/`);

export const getProject = (projectId) =>
  api.get(`projects/${projectId}/`);

export const createProject = (data) =>
  api.post("projects/create/", data);

export const updateProject = (
  projectId,
  data
) =>
  api.put(
    `projects/${projectId}/update/`,
    data
  );

export const deleteProject = (
  projectId
) =>
  api.delete(
    `projects/${projectId}/delete/`
  );