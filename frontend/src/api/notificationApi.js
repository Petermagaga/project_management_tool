import api from "./axios";

export const getNotifications = () =>
  api.get(
    "activity/notifications/"
  );

export const getUnreadCount = () =>
  api.get(
    "activity/notifications/count/"
  );

export const markAsRead = (
  notificationId
) =>
  api.put(
    `activity/notifications/${notificationId}/read/`
  );