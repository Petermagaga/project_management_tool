import { useQuery } from "@tanstack/react-query";

import {
  getNotifications,
  getUnreadCount
} from "../api/notificationApi";

export const useNotifications = () =>
  useQuery({
    queryKey: ["notifications"],
    queryFn: async () => {
      const res =
        await getNotifications();
      return res.data;
    }
  });

export const useUnreadCount = () =>
  useQuery({
    queryKey: ["unreadCount"],
    queryFn: async () => {
      const res =
        await getUnreadCount();
      return res.data.unread_count;
    }
  });