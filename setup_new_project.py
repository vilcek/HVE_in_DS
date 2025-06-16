#!/usr/bin/env python3
"""
Project Setup Script

This script copies files from the project_example folder and creates a new project
with the specified folder structure.

Usage:
    python setup_project.py <folder_path>

Examples:
    python setup_project.py my_new_project
    python setup_project.py projects/my_new_project
    python setup_project.py /path/to/my_new_project
"""

import argparse
import shutil
import sys
from pathlib import Path


def setup_project(folder_path: str) -> None:
    """
    Set up a new project by copying files from project_example.
    
    Args:
        folder_path: Path to the destination folder to create (can be relative or absolute)
    """
    # Define paths
    script_dir = Path(__file__).parent
    project_example_dir = script_dir / "project_example"
    
    # Handle the destination path - can be relative or absolute
    destination_path = Path(folder_path)
    if not destination_path.is_absolute():
        destination_dir = script_dir / folder_path
    else:
        destination_dir = destination_path
    
    # Check if project_example exists
    if not project_example_dir.exists():
        print(f"Error: project_example directory not found at {project_example_dir}")
        sys.exit(1)
    
    # Check if destination already exists
    if destination_dir.exists():
        response = input(f"Directory '{destination_dir}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            sys.exit(0)
        shutil.rmtree(destination_dir)
    
    print(f"Creating project structure in '{destination_dir}'...")
    
    # Create main destination directory and any parent directories
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy requirements.txt from root directory
    requirements_src = script_dir / "requirements.txt"
    if requirements_src.exists():
        shutil.copy2(requirements_src, destination_dir / "requirements.txt")
        print("✓ Copied requirements.txt")
    else:
        print("⚠ requirements.txt not found in root directory")
    
    # Copy download_data.py from project_example
    download_data_src = project_example_dir / "download_data.py"
    if download_data_src.exists():
        shutil.copy2(download_data_src, destination_dir / "download_data.py")
        print("✓ Copied download_data.py")
    else:
        print("⚠ download_data.py not found in project_example")
    
    # Copy .github folder structure
    github_src = project_example_dir / ".github"
    github_dst = destination_dir / ".github"
    
    if github_src.exists():
        # Create .github directory structure
        github_dst.mkdir(exist_ok=True)
        (github_dst / "instructions").mkdir(exist_ok=True)
        (github_dst / "prompts").mkdir(exist_ok=True)
        
        # Copy copilot-instructions.md
        copilot_instructions_src = github_src / "copilot-instructions.md"
        if copilot_instructions_src.exists():
            shutil.copy2(copilot_instructions_src, github_dst / "copilot-instructions.md")
            print("✓ Copied .github/copilot-instructions.md")
        
        # Copy instructions files
        instructions_src = github_src / "instructions"
        if instructions_src.exists():
            notebook_guidelines_src = instructions_src / "notebook_guidelines.instructions.md"
            if notebook_guidelines_src.exists():
                shutil.copy2(notebook_guidelines_src, 
                           github_dst / "instructions" / "notebook_guidelines.instructions.md")
                print("✓ Copied .github/instructions/notebook_guidelines.instructions.md")
        
        # Copy prompts files
        prompts_src = github_src / "prompts"
        if prompts_src.exists():
            implementation_plan_src = prompts_src / "implementation_plan.prompt.md"
            plan_execution_src = prompts_src / "plan_execution.prompt.md"
            
            if implementation_plan_src.exists():
                shutil.copy2(implementation_plan_src, 
                           github_dst / "prompts" / "implementation_plan.prompt.md")
                print("✓ Copied .github/prompts/implementation_plan.prompt.md")
                
            if plan_execution_src.exists():
                shutil.copy2(plan_execution_src, 
                           github_dst / "prompts" / "plan_execution.prompt.md")
                print("✓ Copied .github/prompts/plan_execution.prompt.md")
    
    # Create empty directories
    directories_to_create = [
        "chats",
        "intermediate_data", 
        "notebooks",
        "results_data"
    ]
    
    for dir_name in directories_to_create:
        (destination_dir / dir_name).mkdir(exist_ok=True)
        print(f"✓ Created {dir_name}/ directory")
    
    # Create source_data directory and copy scenario_description.md
    source_data_dst = destination_dir / "source_data"
    source_data_dst.mkdir(exist_ok=True)
    
    scenario_desc_src = project_example_dir / "source_data" / "scenario_description.md"
    if scenario_desc_src.exists():
        shutil.copy2(scenario_desc_src, source_data_dst / "scenario_description.md")
        print("✓ Created source_data/ directory and copied scenario_description.md")
    else:
        print("✓ Created source_data/ directory")
        print("⚠ scenario_description.md not found in project_example/source_data")
    
    print(f"\n Project '{destination_dir.name}' setup complete!")
    print(f" Project location: {destination_dir.absolute()}")
    
    # Display the created structure
    print(f"\n Created structure:")
    print(f"{destination_dir.name}/")
    print("├── requirements.txt")
    print("├── download_data.py")
    print("├── .github/")
    print("│   ├── copilot-instructions.md")
    print("│   ├── instructions/")
    print("│   │   └── notebook_guidelines.instructions.md")
    print("│   └── prompts/")
    print("│       ├── implementation_plan.prompt.md")
    print("│       └── plan_execution.prompt.md")
    print("├── chats/")
    print("├── intermediate_data/")
    print("├── notebooks/")
    print("├── source_data/")
    print("│   └── scenario_description.md")
    print("└── results_data/")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Set up a new project by copying files from project_example",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python setup_new_project.py my_new_project
  python setup_new_project.py projects/my_new_project  
  python setup_new_project.py /path/to/my_new_project
        """
    )
    
    parser.add_argument(
        "folder_path",
        help="Path to the destination folder to create (can be relative or absolute)"
    )
    
    args = parser.parse_args()
    
    # Validate folder path
    if not args.folder_path or args.folder_path.strip() == "":
        print("Error: folder_path cannot be empty")
        sys.exit(1)
    
    setup_project(args.folder_path)


if __name__ == "__main__":
    main()
