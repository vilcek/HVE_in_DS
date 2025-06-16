#!/usr/bin/env python3
"""
Download and extract NASA Turbofan Engine Degradation Simulation dataset.

This script downloads the NASA CMAPSSData dataset from the PHM Data Challenge
and extracts it to the source_data directory.
"""

import requests
import zipfile
import shutil
from pathlib import Path
import sys
from typing import Optional


def download_file(url: str, filepath: Path, chunk_size: int = 8192) -> bool:
    """
    Download a file from URL to local filepath with progress indication.
    
    Args:
        url: URL to download from
        filepath: Local path to save the file
        chunk_size: Size of chunks to download at a time
        
    Returns:
        True if successful, False otherwise
    """
    try:
        print(f"Downloading {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # Show progress
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\rProgress: {percent:.1f}%", end='', flush=True)
        
        print("\nDownload completed successfully!")
        return True
        
    except requests.RequestException as e:
        print(f"\nError downloading file: {e}")
        return False
    except Exception as e:
        print(f"\nUnexpected error during download: {e}")
        return False


def extract_zip(zip_path: Path, extract_to: Path) -> bool:
    """
    Extract a ZIP file to the specified directory.
    
    Args:
        zip_path: Path to the ZIP file
        extract_to: Directory to extract files to
        
    Returns:
        True if successful, False otherwise
    """
    try:
        print(f"Extracting {zip_path.name} to {extract_to}")
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            
        print("Extraction completed successfully!")
        return True
        
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid ZIP file")
        return False
    except Exception as e:
        print(f"Error extracting ZIP file: {e}")
        return False


def extract_nested_zip(source_data_dir: Path) -> bool:
    """
    Handle nested ZIP structure - extract CMAPSSData.zip from the extracted folder.
    
    Args:
        source_data_dir: Directory containing the extracted files
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Look for the nested folder and ZIP file
        nested_folder = source_data_dir / "6. Turbofan Engine Degradation Simulation Data Set"
        nested_zip = nested_folder / "CMAPSSData.zip"
        
        if nested_zip.exists():
            print(f"Found nested ZIP file: {nested_zip}")
            print(f"Extracting {nested_zip.name} to {source_data_dir}")
            
            # Extract the nested ZIP directly to source_data_dir
            with zipfile.ZipFile(nested_zip, 'r') as zip_ref:
                zip_ref.extractall(source_data_dir)
            
            print("Nested ZIP extraction completed successfully!")
            
            # Clean up: remove the nested folder structure
            import shutil
            print(f"Cleaning up nested folder: {nested_folder}")
            shutil.rmtree(nested_folder)
            
            return True
        else:
            print("No nested ZIP file found, proceeding with existing structure")
            return True
            
    except Exception as e:
        print(f"Error handling nested ZIP structure: {e}")
        return False


def main():
    """Main function to download and extract the dataset."""
    # Define paths
    script_dir = Path(__file__).parent
    source_data_dir = script_dir / "source_data"
    zip_filename = "NASA_Turbofan_Engine_Degradation_Dataset.zip"
    zip_path = source_data_dir / zip_filename
    
    # URL for the dataset
    dataset_url = "https://phm-datasets.s3.amazonaws.com/NASA/6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip"
    
    # Create source_data directory if it doesn't exist
    source_data_dir.mkdir(exist_ok=True)
    print(f"Using source data directory: {source_data_dir}")
    
    # Check if ZIP file already exists
    if zip_path.exists():
        print(f"ZIP file already exists at {zip_path}")
        user_input = input("Do you want to re-download it? (y/N): ").strip().lower()
        if user_input not in ['y', 'yes']:
            print("Skipping download...")
        else:
            # Remove existing file
            zip_path.unlink()
    
    # Download the file if it doesn't exist
    if not zip_path.exists():
        success = download_file(dataset_url, zip_path)
        if not success:
            print("Failed to download the dataset. Exiting.")
            sys.exit(1)
    
    # Extract the ZIP file
    success = extract_zip(zip_path, source_data_dir)
    if not success:
        print("Failed to extract the dataset. Exiting.")
        sys.exit(1)
    
    # Handle nested ZIP structure
    success = extract_nested_zip(source_data_dir)
    if not success:
        print("Failed to handle nested ZIP structure. Exiting.")
        sys.exit(1)
    
    # Clean up: optionally remove the ZIP file
    user_input = input(f"\nDo you want to delete the ZIP file {zip_filename}? (y/N): ").strip().lower()
    if user_input in ['y', 'yes']:
        zip_path.unlink()
        print("ZIP file deleted.")
    else:
        print("ZIP file kept.")
    
    print("\nDataset download and extraction completed successfully!")
    print(f"Data files are available in: {source_data_dir}")
    
    # List extracted files
    print("\nExtracted files:")
    for file in sorted(source_data_dir.iterdir()):
        if file.is_file():
            print(f"  - {file.name}")


if __name__ == "__main__":
    main()
