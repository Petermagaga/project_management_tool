import TaskCard
from "../tasks/TaskCard";

import {
  useTasks
}
from "../../hooks/useTasks";


export default function BoardColumn({
  board
}) {

  const {

    data: tasks = [],

    isLoading,

  } =
    useTasks(board.id);

    return (

<div
className="
bg-gray-100
rounded-xl
p-4
w-80
min-h-[500px]"
>

<h2
className="
font-bold
text-lg
mb-4"
>

{board.name}

</h2>
{
isLoading

?

<div>
Loading...
</div>

:

tasks.map(
(task) => (

<TaskCard

key={task.id}

task={task}

/>
))
}
</div>
);
}