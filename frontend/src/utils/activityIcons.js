import {
  FaTasks,
  FaEdit,
  FaTrash,
  FaComment,
  FaProjectDiagram
} from "react-icons/fa";

export const activityIcon =
(type) => {

  switch(type){

    case "TASK_CREATED":
      return <FaTasks />;

    case "TASK_UPDATED":
      return <FaEdit />;

    case "TASK_MOVED":
      return <FaTasks />;

    case "TASK_DELETED":
      return <FaTrash />;

    case "COMMENT_CREATED":
      return <FaComment />;

    case "PROJECT_CREATED":
      return <FaProjectDiagram />;

    default:
      return <FaTasks />;
  }
};