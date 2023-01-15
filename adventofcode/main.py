"""Main module."""
import logging

from adventofcode.logic.taskmanager import TaskManager

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Main function to start programm"""
    taskmanager = TaskManager()
    taskmanager.solve_single_task("01-01")
