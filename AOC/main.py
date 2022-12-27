import logging

logging.basicConfig(level=logging.INFO)
from AOC.tasks.tasks import TaskManager


def main():
    taskmanager = TaskManager()
    taskmanager.solve_single_task("01-01")
