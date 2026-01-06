---
title: Chat.Py
marimo-version: 0.18.4
width: medium
---

```python {.marimo}
import marimo as mo
```

```python {.marimo}
def simple_echo_model(messages, config):
    return f"You said: {messages[-1].content}"

chatbot = mo.ui.chat(
    simple_echo_model,
    prompts=["Hello", "How are you?"],
    show_configuration_controls=True
)
chatbot
```

```python {.marimo}
chatbot.value
```