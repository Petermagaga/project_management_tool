export default function TaskCard({
  task
}) {

  return (

    <div
      className="
      bg-white
      rounded-lg
      p-3
      mb-3
      shadow-sm"
    >

      <h3
        className="
        font-semibold"
      >
        {task.title}
      </h3>

      <p
        className="
        text-sm
        text-gray-500"
      >
        {task.priority}
      </p>

    </div>
  );
}