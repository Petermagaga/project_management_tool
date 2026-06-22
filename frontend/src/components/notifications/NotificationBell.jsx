import {
  FaBell
} from "react-icons/fa";

import {
  useUnreadCount
} from "../../hooks/useNotifications";

export default function NotificationBell() {

  const {
    data: count = 0
  } = useUnreadCount();

  return (

    <div
      className="
      relative
      cursor-pointer"
    >

      <FaBell size={22} />

      {
        count > 0 && (

          <span
            className="
            absolute
            -top-2
            -right-2
            bg-red-500
            text-white
            text-xs
            rounded-full
            px-2"
          >

            {count}

          </span>
        )
      }

    </div>
  );
}