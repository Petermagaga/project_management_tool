import {
  useForm
} from "react-hook-form";

import {
  createTask
} from "../../api/taskApi";

export default function CreateTaskModal({

  boardId,

  projectId,

  onSuccess

}) {

  const {

    register,

    handleSubmit,

    reset

  } =
    useForm();


const onSubmit =
async (data) => {

try {

await createTask({

title:
data.title,

priority:
data.priority,

board:
boardId,

project:
projectId,
});

reset();

onSuccess();

} catch {

alert(
"Failed"
);
}
};

return (

<form

onSubmit={handleSubmit(onSubmit)}

className="
bg-white
p-3
rounded-lg
mb-3"
>

<input

placeholder="Task Title"

{...register("title")}

className="
border
w-full
p-2
mb-2"
/>

<select

{...register(
"priority"
)}

className="
border
w-full
p-2
mb-2"
>

<option>
LOW
</option>

<option>
MEDIUM
</option>

<option>
HIGH
</option>

</select>

<button
className="
bg-black
text-white
px-3
py-2"
>

Add Task

</button>

</form>
);
}