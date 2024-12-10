
__generated_with = "0.9.33"

# %%
import marimo as mo

# %%
mo.md("# Task List").left()

# %%
get_tasks, set_tasks = mo.state([])
mutation_signal, set_mutation_signal = mo.state(False)

# %%
mutation_signal

task_entry_box = mo.ui.text(placeholder="a task ...")

# %%
from dataclasses import dataclass

# %%
@dataclass
class Task:
    name: str
    done: bool = False

# %%
def add_task():
    if task_entry_box.value:
        set_tasks(lambda v: v + [Task(task_entry_box.value)])
    set_mutation_signal(True)


add_task_button = mo.ui.button(
    label="add task",
    on_change=lambda _: add_task(),
)

clear_tasks_button = mo.ui.button(
    label="clear completed tasks",
    on_change=lambda _: set_tasks(
        lambda v: [task for task in v if not task.done]
    ),
)

# %%
mo.hstack(
    [task_entry_box, add_task_button, clear_tasks_button], justify="start"
)

# %%
task_list = mo.ui.array(
    [mo.ui.checkbox(value=task.done, label=task.name) for task in get_tasks()],
    label="tasks",
    on_change=lambda v: set_tasks(
        [Task(task.name, done=v[i]) for i, task in enumerate(get_tasks())]
    ),
)

# %%
mo.as_html(task_list) if task_list.value else mo.md("No tasks! 🎉")