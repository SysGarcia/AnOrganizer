
# AnOrganizer: A Python Desktop File Organizer

## Project Overview
This Python project automates the organization of files on the desktop of the user 'isaac'. It categorizes files based on their extensions and relocates them to designated folders. The project comprises several functions to list files, read configuration, log activities, create folders, and relocate files.

## Features
- **File Listing**: Retrieves a list of all files from the desktop, including their names and extensions.
- **Configuration Reading**: Reads a JSON file (`config.json`) to map file extensions to folder names.
- **Logging**: Logs activities and errors with timestamps in `Logs.txt`.
- **Folder Creation**: Automatically creates folders on the desktop based on the configuration.
- **File Relocation**: Moves files to the appropriate folders based on their extensions.

## Installation
1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed.
3. Place the script in a suitable directory.

## Configuration
- **`config.json`**: This file should be in the same directory as the script. It maps file extensions to folder names.
- Example:
  ```json
  {
    "Documents": ".pdf",
    "Images": ".jpg"
  }
  ```

## Usage
Run the script using Python:
```bash
python __init__.py
```

## Functions
- `get_files_extensions()`: Lists files from the desktop.
- `get_folder_extensions()`: Reads `config.json` to get folder mappings.
- `add_to_logs(info)`: Writes log entries with timestamps.
- `create_folders()`: Creates folders based on `config.json`.
- `relocating_files_folders()`: Relocates files to the appropriate folders.
- `main()`: Main function orchestrating the process.

## Logs
- Log entries are added to `Logs.txt` in the script's directory.
- Each entry includes a UTC timestamp and the logged information.

## Limitations
- The script is configured to work specifically with the desktop of the user 'isaac' Please change all the 'isaac' entries for your own user name.
- It does not handle nested directories or subfolders on the desktop.

## License
This project is open-sourced under the [MIT License](LICENSE).

## Contribution
Contributions are welcome. Please fork the repository and submit a pull request for any enhancements.

## Disclaimer
The script modifies file locations. Ensure to have backups of important files before running the script.

---

