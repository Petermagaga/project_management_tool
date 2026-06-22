import { Draggable } from "@hello-pangea/dnd";

export default function TaskCard({
  task,
  index,
  setSelectedTask
}) {
  return (
    <Draggable
      draggableId={String(task.id)}
      index={index}
    >
      {(provided) => (
        <div
          ref={provided.innerRef}
          {...provided.draggableProps}
          {...provided.dragHandleProps}
          onClick={() => setSelectedTask(task)}
          className="
            bg-white
            rounded-lg
            p-3
            mb-3
            shadow-sm"
        >
          <h3 className="font-semibold">
            {task.title}
          </h3>

          <p className="text-sm text-gray-500">
            {task.priority}
          </p>

        </div>
      )}
    </Draggable>
  );
}