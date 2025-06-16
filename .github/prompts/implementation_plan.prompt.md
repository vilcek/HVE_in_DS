---
mode: 'agent'
description: 'Create a comprehensive plan for implementing data exploration, preparation, feature engineering, modeling, and evaluation'
---
Your goal is to generate a detailed, step-by-step plan for performing data exploration, preparation, feature engineering, modeling, and evaluation, focusing on the C-MAPSS dataset for aircraft engine fault simulation.

## Scenario
The files [`scenario_description.md`](../../source_data/scenario_description.md) and [`readme.txt`](../../source_data/readme.txt) provide you the context around the problem to be solved and the available data.

## Data
Data is provided in the [`source_data`](../../source_data/) folder.
**IMPORTANT**:
- You will focus only on the `FD001` dataset for this plan.
- The target variable is `RUL` (Remaining Useful Life).
- The target column is not present in training data. You will calculate it based on the time in cycles.
- The target column is also not present in the test data, but it is saved in a separate file named `RUL_FD001.txt`.
- The correct separator for the data files is `\s+`, and the files do not have headers.
- You will create a consistent set of column names to be used across all notebooks.

## Plan Structure
You will structure the plan into **tasks**, **phases**, and **steps**
When designing your plan, you will take into account the guidelines for plan implementation described in the file [`notebook_guidelines.instructions.md`](../instructions/notebook_guidelines.instructions.md).

### Plan Tasks
You will focus on the following tasks, following a `CRISP-DM`-like workflow:
- Data Exploration (file name: `01_data_exploration.ipynb`)
- Data Preparation (file name: `02_data_preparation.ipynb`)
- Feature Engineering (file name: `03_feature_engineering.ipynb`)
- Modeling (file name: `04_modeling.ipynb`)
- Evaluation (file name: `05_evaluation.ipynb`) 
You will design each task to be independently implemented in a single Jupyter notebook.
You will name each notebook file according to the list above.

### Task Phases
You will structure each task in multiple phases, which you will determine as needed based on the data and scenario information.
For each task, you will specify the last phase with steps designed to save all necesary data for the next task.

### Phase Steps
You will structure each phase in multiple steps, based on the needs of that phase.

### Plan File
At the very top of the plan, you will insert a Front Matter containing: `applyTo: '**/*.ipynb'`.
You will save the plan as a markdown file named `implementation_plan.instructions.md` under the folder `.github/instructions`.

### Notebook files
After you finish writing the plan, you will create the empty notebook files under the [`notebooks`](../../notebooks/) folder.