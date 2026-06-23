import {
  useNotifications
} from "../../hooks/useNotifications";

export default function NotificationDropdown() {

  const {
    data: notifications = []
  } = useNotifications();

  return (

    <div
      className="
      absolute
      right-0
      top-12
      w-96
      bg-white
      shadow-xl
      rounded-lg
      z-50"
    >

      {
        notifications.map(
          notification => (

            <div

              key={notification.id}

              className="
              border-b
              p-4"
            >

              <p>
                {
                  notification.sender_email
                }
              </p>

              <p>
                {
                  notification.message
                }
              </p>

            </div>
          )
        )
      }

    </div>
  );
}