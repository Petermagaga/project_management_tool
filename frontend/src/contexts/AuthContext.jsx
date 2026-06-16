import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

import {
  getCurrentUser,
} from "../api/authApi";

const AuthContext =
  createContext();

export const AuthProvider = ({
  children,
}) => {

  const [user, setUser] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  const fetchUser = async () => {

    try {

      const res =
        await getCurrentUser();

      setUser(res.data);

    } catch {

      setUser(null);

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    const token =
      localStorage.getItem(
        "access"
      );

    if (token) {

      fetchUser();

    } else {

      setLoading(false);
    }

  }, []);

  const logout = () => {

    localStorage.removeItem(
      "access"
    );

    localStorage.removeItem(
      "refresh"
    );

    setUser(null);
  };

  return (

    <AuthContext.Provider
      value={{

        user,

        setUser,

        fetchUser,

        logout,

        loading,
      }}
    >

      {children}

    </AuthContext.Provider>
  );
};

export const useAuth = () =>
  useContext(AuthContext);
