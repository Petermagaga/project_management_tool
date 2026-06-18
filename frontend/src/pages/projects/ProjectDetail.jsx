import {
  useParams
} from "react-router-dom";

import DashboardLayout
from "../../layouts/DashboardLayout";

import {
  useBoards
}
from "../../hooks/useBoards";

import BoardColumn
from "../../components/boards/BoardColumn";

export default function ProjectDetail() {

  const {
    projectId
  } =
    useParams();

  const {

    data: boards = [],

    isLoading,

  } =
    useBoards(
      projectId
    );



    return (

<DashboardLayout>

<h1
className="
text-3xl
font-bold
mb-6"
>

Project Board

</h1>

{
isLoading

?

<div>
Loading...
</div>

:

(
<div
className="
flex
gap-5
overflow-x-auto"
>

{
boards.map(
(board) => (

<BoardColumn

key={board.id}

board={board}

/>
))
}

</div>
)
}
</DashboardLayout>
);
}