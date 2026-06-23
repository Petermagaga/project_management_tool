import {
  useActivity
} from "../../hooks/useActivity";

import { activityIcon } from "../../utils/activityIcons";

export default function ActivityTimeline({
  projectId
}) {

  const {
    data: activities = [],
    isLoading
  } = useActivity(projectId);

  if (isLoading) {
    return (
      <div>
        Loading Activity...
      </div>
    );
  }

  return (

    <div
      className="
      bg-white
      rounded-xl
      p-5
      shadow-sm"
    >

      <h2
        className="
        text-xl
        font-bold
        mb-5"
      >
        Recent Activity
      </h2>

      {
        activities.map(
          activity => (

            <div

              key={activity.id}

              className="
              border-b
              py-4"
            >

            <div
            className="
            flex
            gap-3
            items-center"
            >

            {activityIcon(
                activity.action_type
            )}

            <span>
                {activity.message}
            </span>

            </div>

              <p
                className="
                text-sm
                text-gray-500"
              >
                {activity.user_email}
              </p>

              <p
                className="
                text-xs
                text-gray-400"
              >
                {new Date(
                  activity.created_at
                ).toLocaleString()}
              </p>

            </div>
          )
        )
      }

    </div>
  );
}