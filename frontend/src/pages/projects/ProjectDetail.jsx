import { useState } from "react";
import { useParams } from "react-router-dom";

import DashboardLayout from "../../layouts/DashboardLayout";

import { useBoards } from "../../hooks/useBoards";
import { useProjectTasks } from "../../hooks/useProjectTasks";
import TaskDrawer from "../../components/tasks/TaskDrawer";
import BoardColumn from "../../components/boards/BoardColumn";

import { DragDropContext } from "@hello-pangea/dnd";

import { updateTask } from "../../api/taskApi";

import { useQueryClient } from "@tanstack/react-query";

export default function ProjectDetail() {
  const { projectId } = useParams();

  const {
    data: boards = [],
    isLoading,
  } = useBoards(projectId);

  const {
    data: tasks = [],
  } = useProjectTasks(projectId);

  const queryClient = useQueryClient();

  const [
  selectedTask,
  setSelectedTask
  ] =
  useState(null);

  const onDragEnd = async (result) => {
    if (!result.destination) return;

    const taskId = Number(result.draggableId);

    const destinationBoardId = Number(
      result.destination.droppableId
    );

    try {
      await updateTask(taskId, {
        board: destinationBoardId,
      });

      queryClient.invalidateQueries({
        queryKey: ["projectTasks"],
      });
    } catch {
      alert("Failed to move task");
    }
  };

  // Group tasks by board
  const tasksByBoard = {};

  boards.forEach((board) => {
    tasksByBoard[board.id] = [];
  });

  tasks.forEach((task) => {
    if (tasksByBoard[task.board]) {
      tasksByBoard[task.board].push(task);
    }
  });

  return (
    <DashboardLayout>
      <h1 className="text-3xl font-bold mb-6">
        Project Board
      </h1>

      {isLoading ? (
        <div>Loading...</div>
      ) : (
        <DragDropContext onDragEnd={onDragEnd}>
          <div className="flex gap-5 overflow-x-auto">
            {boards.map((board) => (
              <BoardColumn
                key={board.id}
                board={board}
                tasks={tasksByBoard[board.id] || []}
                setSelectedTask={setSelectedTask}
              />
            ))}
          </div>
        </DragDropContext>

    
      )}

        <TaskDrawer
        task={selectedTask}
        open={!!selectedTask}
        onClose={() =>setSelectedTask(null)}
        />

    </DashboardLayout>
  );
}