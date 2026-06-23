import {
PieChart,Pie,Cell,Tooltip,ResponsiveContainer} from "recharts";

export default function TaskStatusChart({

tasks

}) {

const data = [

{
name:"Backlog",
value:
tasks.filter(
t=>t.status==="Backlog"
).length
},

{
name:"In Progress",
value:
tasks.filter(
t=>t.status==="In Progress"
).length
},

{
name:"Done",
value:
tasks.filter(
t=>t.status==="Done"
).length
},

];

return (

<div
className="
bg-white
rounded-xl
p-5"
>

<h2
className="
font-bold
mb-4"
>

Task Distribution

</h2>

<ResponsiveContainer
width="100%"
height={300}
>

<PieChart>

<Pie

data={data}

dataKey="value"

outerRadius={100}

/>

<Tooltip />

</PieChart>

</ResponsiveContainer>

</div>
);
}