import api from "./axios";

export const getTaskComments = (
  taskId
) =>
  api.get(
    `comments/task/${taskId}/`
  );

export const createComment = (
  data
) =>
  api.post(
    "comments/create/",
    data
  );

export const updateComment = (
  commentId,
  data
) =>
  api.put(
    `comments/${commentId}/update/`,
    data
  );

export const deleteComment = (
  commentId
) =>
  api.delete(
    `comments/${commentId}/delete/`
  );