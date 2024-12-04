
__generated_with = "0.9.30"

# %%
import marimo as mo

# %%
graph = mo.ui.code_editor(
    value="""sequenceDiagram
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
    Alice-)John: See you later!""",
    language="mermaid",
    label="Mermaid editor",
)
graph

# %%
mo.mermaid(
    """
graph TD
    A[Enter Chart Definition] --> B(Preview)
    B --> C{decide}
    C --> D[Keep]
    C --> E[Edit Definition]
    E --> B
    D --> F[Save Image and Code]
    F --> B
"""
).center()

# %%
mo.md(
    f"""
    You can render mermaid directly inside `mo.md`. Using

    `mo.mermaid()`

    {mo.mermaid(graph.value)}
    """
)