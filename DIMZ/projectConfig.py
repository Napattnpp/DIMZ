import os
import shutil
import sys
import json

CURRENT_DIR = os.getcwd();

# Config file path
CONFIG_FILE = os.path.join(CURRENT_DIR, "projectConfig.json")

def delete_folder(folder):
    """Deletes a folder if it exists."""
    folder_path = os.path.join(CURRENT_DIR, folder)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted: {folder_path}")
    else:
        print(f"Folder not found: {folder_path}")

def load_config():
    """Loads deletion rules from the config file."""
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: Config file '{CONFIG_FILE}' not found.")
        sys.exit(1)

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def apply_config(config_name):
    """Applies the deletion rules based on the selected config."""
    config = load_config()

    if config_name not in config:
        print(f"Error: Config '{config_name}' not found in {CONFIG_FILE}.")
        sys.exit(1)

    for folder in config[config_name]:
        delete_folder(folder)

# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_name>")
        sys.exit(1)

    config_name = sys.argv[1]
    apply_config(config_name)

