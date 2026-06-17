import {
  FaHome,
  FaFolder,
  FaTasks,
  FaCog,
  FaChartBar,
} from "react-icons/fa";

import {
  NavLink,
} from "react-router-dom";


const menu = [

  {
    name: "Dashboard",
    path: "/",
    icon: <FaHome />,
  },

  {
    name: "Projects",
    path: "/projects",
    icon: <FaFolder />,
  },

  {
    name: "Tasks",
    path: "/tasks",
    icon: <FaTasks />,
  },

  {
    name: "Activity",
    path: "/activity",
    icon: <FaChartBar />,
  },

  {
    name: "Settings",
    path: "/settings",
    icon: <FaCog />,
  },
];

export default function Sidebar() {

  return (

    <div className="w-64 bg-white border-r">

      <div className="p-5">

        <h1 className="text-2xl font-bold">

          PM Tool

        </h1>

      </div>

      <nav>

        {menu.map((item) => (

          <NavLink

            key={item.path}

            to={item.path}

            className={({ isActive }) =>

              `flex items-center gap-3 px-5 py-3 hover:bg-gray-100

              ${isActive ? "bg-gray-200" : ""}`
            }

          >

            {item.icon}

            {item.name}

          </NavLink>
        ))}

      </nav>

    </div>
  );
}