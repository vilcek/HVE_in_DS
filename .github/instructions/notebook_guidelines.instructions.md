---
applyTo: '**/*.ipynb'
---
Guidelines for implementing the plan as Jupyter notebooks

## Objective
Create a fully‑featured **Jupyter notebook** that implements ONE PHASE of the plan, based on the scenario description.

## Notebook Development Instructions
- The plan you are following is organized into **tasks**, **phases**, and **steps**.
- You will ALWAYS implement one task of the plan at a time, as a single Jupyter notebook.
- You will ALWAYS use the `intermediate_data` folder to store the intermediate data needed for the next task in the plan, and use the naming convention `<task_name><file_name>.<file_extension>`. For each intermediate data you save, you will ALWAYS create a corresponding Markdown file, using the same file name as the data file, with a description of the data, and how to load it properly.
- When loading data from the `intermediate_data` folder, you will ALWAYS use the correct object types, column names and types, and data formats as specified in the corresponding data documentation file.
- You will ALWAYS use the `results_data` folder to store the trained models and any transformation needed to use the models with the test data.
- You will ALWAYS add Markdown cells to the notebook, use exactly the same content (numbering, name, description) for each phase and step in the plan, before adding the corresponding code cells.
- You will ALWAYS add all the code needed to complete the correspond step in the plan in a single cell, unless multiple code cells for a single step are needed for better readability.

## Context
- The scenario description is located in the file [`scenario_description.md`](../../source_data/scenario_description.md).
- Training data, testing data, and test labels, are located in the folder [`CMAPSSData`](../../source_data).
- There is a `readme.txt` file in the same folder, which contains descriptions of the datasets and column information.
- The implementation plan for the notebooks is located in the folder [`.github/instructions/implementation_plan.instructions.md`](../../.github/instructions/implementation_plan.instructions.md).
