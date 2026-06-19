import api from "./axios";


export const getBoardTasks = (
  boardId
) =>
  api.get(
    `tasks/board/${boardId}/`
  );

export const createTask = (
  data
) =>
  api.post(
    "tasks/create/",
    data
  );

export const updateTask = (
  taskId,
  data
) =>
  api.put(
    `tasks/${taskId}/update/`,
    data
  );

export const deleteTask = (
  taskId
) =>
  api.delete(
    `tasks/${taskId}/delete/`
  );

export const getProjectTasks =
(projectId) =>

api.get(
  `tasks/project/${projectId}/`
);

