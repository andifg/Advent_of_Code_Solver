"""Main module."""
import logging

from adventofcode.logic.task.taskmanager import TaskManager

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Main function to start programm"""
    taskmanager = TaskManager()
    taskmanager.solve_all_task()
