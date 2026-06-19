import TaskCard
from "../tasks/TaskCard";

export default function BoardColumn({

board,

tasks

}) {

return (

<div
className="
bg-gray-100
rounded-xl
w-80
p-4"
>

<h2
className="
font-bold
mb-4"
>

{board.name}

</h2>

{
tasks.map(task => (

<TaskCard

key={task.id}

task={task}

/>

))
}

</div>
);
}