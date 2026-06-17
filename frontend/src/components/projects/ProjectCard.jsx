import {
  FaFolder
} from "react-icons/fa";

import {
  useNavigate
} from "react-router-dom";

export default function ProjectCard({
  project
}) {

  const navigate =
    useNavigate();

  return (

    <div

      onClick={() =>
        navigate(
          `/projects/${project.id}`
        )
      }

      className="
      bg-white
      rounded-xl
      p-5
      shadow-sm
      cursor-pointer
      hover:shadow-md
      transition"
    >

      <FaFolder
        size={30}
      />

      <h2
        className="
        mt-4
        text-xl
        font-semibold"
      >

        {project.name}

      </h2>

      <p
        className="
        text-gray-500
        mt-2"
      >

        {project.description}

      </p>

    </div>
  );
}