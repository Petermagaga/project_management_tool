import {
  useForm
} from "react-hook-form";

import {
  useNavigate
} from "react-router-dom";

import {
  registerUser
} from "../../api/authApi";


export default function Register() {

  const navigate =
    useNavigate();

  const {
    register,
    handleSubmit,
  } = useForm();


    const onSubmit =
    async (data) => {

    try {

    await registerUser(data);

    navigate("/login");

    } catch {

    alert(
    "Registration failed"
    );
    }
    };

return (

<div className="p-10">

<h1 className="text-3xl font-bold">

Register

</h1>

<form

onSubmit={handleSubmit(onSubmit)}

className="space-y-4 mt-5"
>

<input

placeholder="Username"

{...register("username")}

className="border p-2 w-full"
/>

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

Register

</button>

</form>

</div>
);
}