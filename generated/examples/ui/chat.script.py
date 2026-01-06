
__generated_with = "0.18.4"

# %%
import marimo as mo

# %%
def simple_echo_model(messages, config):
    return f"You said: {messages[-1].content}"

chatbot = mo.ui.chat(
    simple_echo_model,
    prompts=["Hello", "How are you?"],
    show_configuration_controls=True
)
chatbot

# %%
chatbot.value