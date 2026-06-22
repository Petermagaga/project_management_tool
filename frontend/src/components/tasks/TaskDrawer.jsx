import { useComments } from "../../hooks/useComments";
import { useAuth } from "../../contexts/AuthContext";

import { useForm } from "react-hook-form";
import { createComment } from "../../api/commentApi";
import { useQueryClient } from "@tanstack/react-query";


export default function TaskDrawer({

task,

open,

onClose

}) {

const { data: comments = [] } = useComments(task.id);

const queryClient = useQueryClient();

const {
  register,
  handleSubmit,
  reset
} = useForm();

const onSubmit = async (data) => {

  await createComment({
    task: task.id,
    content: data.content
  });

  reset();

  queryClient.invalidateQueries({
    queryKey: ["comments", task.id]
  });

};


if(!open) return null;


return (

<div
className="
fixed
top-0
right-0
w-[500px]
h-full
bg-white
shadow-xl
z-50
overflow-y-auto
p-6"
>

<button
onClick={onClose}
>
Close
</button>

<h1
className="
text-2xl
font-bold
mt-4"
>

{task.title}

</h1>

<p
className="
text-gray-500
mt-3"
>

{task.description}

</p>

<div className="mt-5">

<p>

Priority:
{task.priority}

</p>

<p>

Assignee:
{task.assignee_email}

</p>

<p>

Reporter:
{task.reporter_email}

</p>



</div>


<h2 className="
font-bold
mt-8
mb-3"
>
Comments
</h2>

{
  comments.map((comment) => (
    <div
      key={comment.id}
      className="
      border-b
      py-3"
    >

      <p>{comment.user_email}</p>

      <p>{comment.content}</p>

    </div>
  ))
}

<form
  onSubmit={handleSubmit(onSubmit)}
  className="mt-4"
>

  <textarea
    {...register("content")}
    className="
    border
    w-full
    p-2"
  />

  <button
    className="
    bg-black
    text-white
    px-4
    py-2
    mt-2"
  >
    Add Comment
  </button>

</form>

</div>
);
}