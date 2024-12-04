---
title: Task List
marimo-version: 0.9.29
---

```{.python.marimo hide_code="true"}
mo.md("# Task List").left()
```

```{.python.marimo}
@dataclass
class Task:
    name: str
    done: bool = False
```

```{.python.marimo}
get_tasks, set_tasks = mo.state([])
mutation_signal, set_mutation_signal = mo.state(False)
```

```{.python.marimo}
mutation_signal

task_entry_box = mo.ui.text(placeholder="a task ...")
```

```{.python.marimo}
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
```

```{.python.marimo}
mo.hstack(
    [task_entry_box, add_task_button, clear_tasks_button], justify="start"
)
```

```{.python.marimo}
task_list = mo.ui.array(
    [mo.ui.checkbox(value=task.done, label=task.name) for task in get_tasks()],
    label="tasks",
    on_change=lambda v: set_tasks(
        [Task(task.name, done=v[i]) for i, task in enumerate(get_tasks())]
    ),
)
```

```{.python.marimo}
mo.as_html(task_list) if task_list.value else mo.md("No tasks! 🎉")
```

```{.python.marimo}
import marimo as mo
```

```{.python.marimo}
from dataclasses import dataclass
```