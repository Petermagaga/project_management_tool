import TaskCard
from "../tasks/TaskCard";

import { Droppable } from "@hello-pangea/dnd";


export default function BoardColumn({

  board,

  tasks,
  setSelectedTask

}) {

  return (

    <Droppable

      droppableId={
        String(board.id)
      }

    >

      {(provided) => (

        <div

          ref={
            provided.innerRef
          }

          {...provided.droppableProps}

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
            mb-4"
          >
            {board.name}
          </h2>

          {tasks.map(

            (
              task,
              index
            ) => (

              <TaskCard

                key={task.id}

                task={task}

                index={index}
                setSelectedTask={setSelectedTask}

              />
            )
          )}

          {
            provided.placeholder
          }

        </div>
      )}

    </Droppable>
  );
}