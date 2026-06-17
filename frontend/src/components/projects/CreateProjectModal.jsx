import {
  useForm
} from "react-hook-form";

import {
  createProject
} from "../../api/projectApi";


export default function CreateProjectModal({

  workspaceId,

  onSuccess,

}) {

  const {

    register,

    handleSubmit,

    reset,

  } = useForm();

  const onSubmit =
async (data) => {

  try {

    await createProject({

      ...data,

      workspace:
        workspaceId,

    });

    reset();

    onSuccess();

  } catch {

    alert(
      "Failed to create project"
    );
  }
};

return (

<form

onSubmit={handleSubmit(onSubmit)}

className="
bg-white
p-5
rounded-xl
mb-6"
>

<input

placeholder="Project Name"

{...register("name")}

className="
border
w-full
p-2
mb-3"
/>

<textarea

placeholder="Description"

{...register(
  "description"
)}

className="
border
w-full
p-2
mb-3"
/>

<button

className="
bg-black
text-white
px-4
py-2"
>

Create Project

</button>

</form>
);
}