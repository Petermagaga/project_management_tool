import {
  FaBell,
} from "react-icons/fa";

import {
  useAuth
} from "../../contexts/AuthContext";


export default function Topbar() {

  const {
    user,
  } = useAuth();

  return (

    <header
      className="
      h-16
      bg-white
      border-b
      flex
      items-center
      justify-between
      px-6"
    >

      <input

        placeholder="Search..."

        className="
        border
        rounded-lg
        px-3
        py-2
        w-80"
      />

      <div
        className="
        flex
        items-center
        gap-5"
      >

        <FaBell
          size={20}
        />

        <div>

          <p
            className="
            font-medium"
          >
            {user?.username}
          </p>

          <p
            className="
            text-sm
            text-gray-500"
          >
            {user?.email}
          </p>

        </div>

      </div>

    </header>
  );
}