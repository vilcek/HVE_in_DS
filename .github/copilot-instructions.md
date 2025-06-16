## Code & Style Conventions

### When editing a Jupyter notebook
- You will ALWAYS use the `edit_notebook_file` tool to add cells to the notebook with XML structure that VS Code can render correctly.
- You will NEVER create code in your responses. Every code you propose should be added and edited as Python cells directly in the notebook.

### When writing code cells
- You will ALWAYS use f‑strings, pathlib.Path, and vectorised pandas operations wherever possible.
- You will ALWAYS keep each code cell focused (≈ 10–20 lines) and comment liberally.
- You will ALWAYS use seaborn for static visuals and plotly for interactive (wrap in if interactive: guard if needed).
- You will ALWAYS use a variable defined at top (e.g., DATA_PATH) instead of hard-coding file paths.
- You will ALWAYS set the same random_state for any random or sampling operation.