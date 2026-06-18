import api from "./axios";

export const getProjectBoards = (
  projectId
) =>
  api.get(
    `boards/project/${projectId}/`
  );

export const getBoard = (
  boardId
) =>
  api.get(
    `boards/${boardId}/`
  );

export const createBoard = (
  data
) =>
  api.post(
    "boards/create/",
    data
  );