# Hypervelocity Engineering in Data Science (HVE_in_DS)

**Accelerating Data Science Workflows with GitHub Copilot Agent Mode**


## Project Overview

This project demonstrates how to leverage **GitHub Copilot in Agent mode** to dramatically accelerate data science workflow development. The main focus is on showcasing effective **prompt engineering** and **instruction design** that enables the AI agent to autonomously develop comprehensive data science pipelines.

> **Important**: This code was specifically designed to be used with **GitHub Copilot Agent Mode in VS Code**. The prompt engineering system, instruction files, and workflow patterns are optimized for this environment and may not work as intended with other AI coding assistants or standard Copilot chat mode.
- See the [Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) documentation for more details on how to use GitHub Copilot Agent mode with VS Code.
- See the [Customize Copilot](https://code.visualstudio.com/docs/copilot/copilot-customization) documentation for more details on how to use custom instructions and prompts in Agent mode.

### Key Focus Areas

- **Hypervelocity Engineering**: Using AI agents to accelerate development cycles
- **Prompt Engineering**: Crafting effective instructions for autonomous AI development
- **Template-Driven Development**: Reusable patterns for data science projects
- **Iterative Refinement**: How AI agents can self-correct and improve code quality

> **Note**: While we use a Remaining Useful Life (RUL) prediction problem as our example use case, the primary value lies in the **methodology and prompt patterns** that can be applied to any data science project of medium to high complexity.


## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Agent Mode Workflow](#agent-mode-workflow)
- [GitHub Copilot Instructions & Prompts](#github-copilot-instructions--prompts)
- [Example Use Case](#example-use-case)
- [Template Usage](#template-usage)
- [Troubleshooting](#-troubleshooting)
- [License](#license)


## Project Structure

```
HVE_in_DS/
├── README.md                          # This guide
├── requirements.txt                   # Python dependencies
├── download_data.py                   # Data acquisition script
├── .github/                           # GitHub Copilot prompt engineering system
│   ├── copilot-instructions.md        # Global agent coding standards
│   ├── instructions/                  # Agent behavioral guidelines
│   │   └── notebook_guidelines.instructions.md  # Notebook development rules
│   └── prompts/                       # User-initiated prompt templates
│       ├── implementation_plan.prompt.md        # Strategic planning prompt
│       └── plan_execution.prompt.md             # Task execution prompt
├── chats/                             # Placeholder for Agent conversation logs
├── intermediate_data/                 # Processed data between steps
├── notebooks/                         # Generated Jupyter notebooks
├── source_data/                       # Raw datasets and documentation
│   └── scenario_description.md        # Problem description
├── results_data/                      # Models and final outputs
└── project_example/                   # Complete working example
    ├── download_data.py               # Data acquisition script
    ├── .github/                       # Project-specific prompt engineering
    │   ├── copilot-instructions.md    # Project-specific coding standards
    │   ├── instructions/              # Implementation guidelines
    │   │   ├── implementation_plan.instructions.md  # Generated project plan
    │   │   └── notebook_guidelines.instructions.md  # Notebook development rules
    │   └── prompts/                   # Prompt templates used for this project
    │       ├── implementation_plan.prompt.md        # Planning prompt template
    │       └── plan_execution.prompt.md             # Execution prompt template
    ├── chats/                         # Example conversation logs for fixing issues
    │   ├── leakage_in_data_prep.md    # Data preparation leakage fixes
    │   ├── leakage_in_feat_eng.md     # Feature engineering leakage fixes
    │   └── many_leakage_fixes.md      # Multiple iterations of improvements
    ├── intermediate_data/             # Processed data and metadata
    │   ├── data_exploration_*.csv     # Exploration phase outputs
    │   ├── data_preparation_*.csv     # Cleaned datasets
    │   ├── feature_engineering_*.csv  # Engineered features
    │   ├── modeling_*.csv             # Model results
    │   ├── evaluation_*.csv           # Evaluation metrics
    │   └── *_metadata.json            # Processing metadata
    ├── notebooks/                     # Generated Jupyter notebooks
    │   ├── 01_data_exploration.ipynb  # Data analysis and visualization
    │   ├── 02_data_preparation.ipynb  # Data cleaning and preprocessing
    │   ├── 03_feature_engineering.ipynb # Feature creation and selection
    │   ├── 04_modeling.ipynb          # Model training and comparison
    │   └── 05_evaluation.ipynb        # Model evaluation and validation
    ├── source_data/                   # Raw C-MAPSS dataset
    │   ├── Damage Propagation Modeling.pdf # Technical documentation
    │   ├── readme.txt                 # Dataset description
    │   ├── scenario_description.md    # Problem context
    │   ├── train_FD00*.txt            # Training datasets
    │   ├── test_FD00*.txt             # Test datasets
    │   └── RUL_FD00*.txt              # Ground truth RUL values
    └── results_data/                  # Models and predictions
        └── trained_models/            # Saved model artifacts
            ├── best_model.pkl         # Best performing model
            ├── model_*.pkl            # Individual model files
            └── *_ensemble.json        # Ensemble configurations
```

## Getting Started

### Prerequisites

- **VS Code** with GitHub Copilot subscription
- **Python 3.11+**
- **Jupyter extension** for VS Code

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd HVE_in_DS
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Enable GitHub Copilot Agent mode** in VS Code:
   - Ensure you have an active Copilot subscription
   - Open the Chat View:
     - Using the keyboard shortcut, `Cmd+Shift+I` (Mac) or `Ctrl+Alt+I` (PC), opens it in Agent mode directly.
     - Alternatively, you can find a Copilot Chat icon in the title bar or use the Command Palette and search for "GitHub Copilot Chat: Open Chat View".
   - Select agent mode:
     - In the Chat view, locate the chat mode selector dropdown.
     - Select "Agent" from the available options (you might also see "Ask" and "Edit").


## Agent Mode Workflow

The project demonstrates a structured approach to using GitHub Copilot Agent mode:

### Phase 1: Strategic Planning
The agent analyzes the problem and creates a comprehensive implementation plan following CRISP-DM methodology, to develop the following notebooks:
- **Data Exploration** → `01_data_exploration.ipynb`
- **Data Preparation** → `02_data_preparation.ipynb`  
- **Feature Engineering** → `03_feature_engineering.ipynb`
- **Modeling** → `04_modeling.ipynb`
- **Evaluation** → `05_evaluation.ipynb`

### Phase 2: Iterative Implementation
The agent implements each task following the implementation plan, creating fully functional notebooks with:
- Comprehensive data analysis
- Robust data preprocessing
- Robust feature engineering and feature selection
- Multiple ML model implementations
- Thorough evaluation and visualization

### Phase 3: Quality Assurance & Refinement
With feedback from the data scientist the agent can refine its implementation, such as:
- Detecting and fixing data leakage issues
- Creating and testing new features
- Identifying and resolving code errors
- Improving documentation and comments
- Validating intermediate results
- And many more


## GitHub Copilot Instructions & Prompts

The `.github` folder contains a multi-layered prompt engineering system that enables GitHub Copilot Agent mode to autonomously develop high-quality data science workflows. This system demonstrates advanced AI collaboration patterns.

### Folder Structure

```
.github/                           # GitHub Copilot prompt engineering system
├── copilot-instructions.md        # Global agent coding standards
├── instructions/                  # Agent behavioral guidelines
│   └── notebook_guidelines.instructions.md  # Notebook development rules
└── prompts/                       # User-initiated prompt templates
    ├── implementation_plan.prompt.md        # Strategic planning prompt
    └── plan_execution.prompt.md             # Task execution prompt
```

### How the System Works

#### **1. User Prompts (`prompts/` folder)**
These are templates for **users** to initiate different phases of development:

- **`implementation_plan.prompt.md`**: Creates comprehensive project implementation plans
  - **Usage**: Use this template to create the project implementation plan
  - **Purpose**: Generates structured CRISP-DM workflows with tasks, phases, and steps
  - **Output**: Creates detailed implementation plans and empty notebook files. The plan is saved under the `instructions/` folder, with a structure that allows for it to be automatically added to the Agent's context whenever it is editing a Jupyter notebook file.

- **`plan_execution.prompt.md`**: Executes specific tasks from the plan
  - **Usage**: Use this template to implement individual notebook tasks
  - **Purpose**: Focused execution of single workflow components (e.g., data exploration)
  - **Input Variable**: `${input:taskName}` allows for reusing the prompt for task-specific implementations (e.g., `taskName: Task 1: Data Exploration`)
  - **Output**: Agent will implement the specific task in the corresponding notebook, following the plan

#### **2. Agent Instructions (`instructions/` and root level)**
These files provide **GitHub Copilot** with detailed behavioral guidelines:

- **`copilot-instructions.md`** (root level): Global coding standards
  - **Purpose**: Enforces consistent code quality across all agent outputs
  - **Scope**: Applied automatically to all agent interactions

- **`notebook_guidelines.instructions.md`**: Detailed notebook development rules
  - **Purpose**: Governs how the agent creates and structures Jupyter notebooks
  - **Scope**: Applied specifically to `.ipynb` files (`applyTo: '**/*.ipynb'`)

### Usage Workflow
The user starts the workflow by selecting a prompt from the `prompts/` folder, which guides the agent through the development phases. The agent then autonomously executes tasks based on the provided instructions and user inputs. To select a prompt, the user can:
- Run the `Chat: Run Prompt` command from the Command Palette (⇧⌘P) and select a prompt file from the Quick Pick or
- In the Chat view, type / followed by the prompt file name in the chat input field.

#### **Phase 1: Strategic Planning**
1. User selects `implementation_plan.prompt.md`
2. Agent generates comprehensive plan following CRISP-DM methodology
3. Agent creates empty notebook files with proper naming
4. Agent saves plan as `implementation_plan.instructions.md`

#### **Phase 2: Task Implementation**
1. User selects `plan_execution.prompt.md`
2. Replaces `${input:taskName}` with specific task (e.g., "Task 1: Data Exploration")
3. Agent implements the specific task following the plan
4. Agent applies all instruction guidelines automatically
5. User reviews and iterates as needed

### Customization Guidelines

#### **Adapting Prompts for New Projects**
- **Domain-Specific Context**: Update scenario descriptions and data formats
- **Workflow Modifications**: Adjust task sequences and phase structures
- **Evaluation Criteria**: Define project-specific success metrics
- **Tool Integration**: Specify required libraries and frameworks

#### **Enhancing Instructions**
- **Code Standards**: Add domain-specific coding conventions
- **Quality Checks**: Include additional validation requirements
- **Documentation**: Specify project-specific documentation standards
- **Error Handling**: Define robust exception management patterns

### Best Practices for Prompt Engineering

#### **Effective User Prompts**
- **Clear Objectives**: Define specific, measurable outcomes
- **Structured Context**: Provide comprehensive background information
- **Iterative Design**: Enable refinement and improvement cycles
- **Output Specification**: Define exact file structures and naming conventions

#### **Robust Agent Instructions**
- **Defensive Programming**: Include error handling and edge cases
- **Comprehensive Guidelines**: Cover all aspects of code quality
- **Validation Requirements**: Specify check points and quality gates
- **Consistency Enforcement**: Maintain uniform style and structure


## Example Use Case

The project uses the **C-MAPSS (Commercial Modular Aero-Propulsion System Simulation)** dataset for aircraft engine **Remaining Useful Life (RUL)** prediction:

### Problem Description
- **Objective**: Predict remaining operational cycles before engine failure
- **Data**: Multivariate time series with 26 features (operational settings + sensor readings)
- **Challenge**: Handle multiple operating conditions and fault modes
- **Evaluation**: Asymmetric scoring function (late predictions penalized more heavily)

### Dataset Characteristics
| Dataset | Train Units | Test Units | Operating Conditions | Fault Modes |
|---------|-------------|------------|---------------------|-------------|
| FD001   | 100         | 100        | 1 (sea level)       | 1 (HPC degradation) |
| FD002   | 260         | 259        | 6 (various)         | 1 (HPC degradation) |
| FD003   | 100         | 100        | 1 (sea level)       | 2 (HPC + Fan) |
| FD004   | 248         | 249        | 6 (various)         | 2 (HPC + Fan) |

*Note: This example serves primarily to demonstrate the agent's capabilities on a realistic, medium-complexity problem.*

More details about the dataset can be found at the NASA Prognostics Data Repository [website](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).


## Template Usage

### Creating a New Project

1. **Use the existing structure**:
   ```bash
   # Start fresh with the main directory structure
   mkdir my_new_project
   cp -r .github/ chats/ intermediate_data/ notebooks/ source_data/ results_data/ my_new_project/
   cp requirements.txt download_data.py my_new_project/
   ```

2. **Customize the GitHub Copilot system**:
   - **Global Instructions**: Edit `.github/copilot-instructions.md` for project-specific coding standards
   - **Notebook Guidelines**: Modify `.github/instructions/notebook_guidelines.instructions.md` for workflow requirements
   - **Planning Prompts**: Adapt `.github/prompts/implementation_plan.prompt.md` for your domain and data structure
   - **Execution Prompts**: Update `.github/prompts/plan_execution.prompt.md` with project-specific context

3. **Customize the scenario**:
   - Update `source_data/scenario_description.md` with your problem description
   - Replace datasets in `source_data/` with your own data files
   - Modify `download_data.py` for your data acquisition needs

4. **Initialize development**:
   - Set up your problem-specific requirements in the scenario description
   - Test your prompts with GitHub Copilot Agent mode
   - Begin with strategic planning using the implementation_plan prompt

### Customization Points

#### **Data Science Workflow**
- **Problem Domain**: Update scenario description and evaluation metrics
- **Data Format**: Modify loading instructions and column specifications  
- **Model Types**: Adjust algorithm selection in modeling guidelines
- **Evaluation Criteria**: Define domain-specific success metrics

#### **Prompt Engineering System**
- **Coding Standards**: Customize `.github/copilot-instructions.md` with domain-specific conventions
  - Library preferences (e.g., TensorFlow vs PyTorch for deep learning)
  - Visualization tools (e.g., matplotlib vs plotly preferences)
  - Code organization patterns specific to your domain
- **Workflow Instructions**: Adapt `.github/instructions/notebook_guidelines.instructions.md` for your methodology
  - Data validation requirements
  - Model validation protocols
  - Documentation standards
- **Prompt Templates**: Modify `.github/prompts/` files for your use case
  - Replace dataset references
  - Update file path patterns and naming conventions
  - Adjust task sequences (e.g., add data collection, remove certain modeling steps)
- **Quality Controls**: Enhance instructions with domain-specific validation
  - Regulatory compliance checks
  - Business logic validation
  - Performance benchmarks


## Troubleshooting

### Common Issues

**Agent doesn't follow instructions exactly**
- Make instructions more specific and detailed
- Add explicit examples of expected behavior
- Break complex tasks into smaller, clearer steps

**Code quality issues**
- Enhance the `copilot-instructions.md` with specific coding standards
- Add validation steps in the instruction files
- Use iterative refinement prompts

**Methodological errors**
- Include explicit checks in the instruction templates
- Add validation phases to each task
- Review and improve the guidelines based on identified issues


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
