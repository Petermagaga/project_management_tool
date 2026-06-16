import {
  useForm
} from "react-hook-form";

import {
  useNavigate
} from "react-router-dom";

import {
  loginUser
} from "../../api/authApi";

import {
  useAuth
} from "../../contexts/AuthContext";


export default function Login() {

  const navigate =
    useNavigate();

  const {
    register,
    handleSubmit,
  } = useForm();

  const {
    fetchUser,
  } = useAuth();

  const onSubmit =
    async (data) => {

      try {

        const res =
          await loginUser(data);

        localStorage.setItem(
          "access",
          res.data.access
        );

        localStorage.setItem(
          "refresh",
          res.data.refresh
        );

        await fetchUser();

        navigate("/");

      } catch (error) {

        alert(
          "Invalid credentials"
        );
      }
    };


    return (

    <div className="p-10">

    <h1 className="text-3xl font-bold">

    Login

    </h1>

    <form
    onSubmit={handleSubmit(onSubmit)}
    className="space-y-4 mt-5"
    >

    <input

    placeholder="Email"

    {...register("email")}

    className="border p-2 w-full"
    />

    <input

    type="password"

    placeholder="Password"

    {...register("password")}

    className="border p-2 w-full"
    />

    <button
    className="bg-black text-white px-4 py-2"
    >

    Login

    </button>

    </form>

    </div>
    );
    }
