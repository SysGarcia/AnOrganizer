from datetime import datetime
import os
import json

def get_files_extensions() -> list:
    """
    Retrieves a list of files from the Desktop, including their names and extensions.
    Each item in the list is a dictionary with 'filename' and 'extension' as keys.
    It scans specifically the Desktop directory of the user 'isaac'.
    """
    files_w_extension = []
    all_files_desktop = os.listdir(r"C:\Users\isaac\Desktop")  # Lists all files on the Desktop.
    separated_files = list(all_files_desktop)
    
    for filepaths in separated_files:
        file = os.path.splitext(filepaths)  # Splits the filename and extension.
        file_name = file[0]
        extension = file[1]
        files_w_extension.append(dict(filename=file_name,extension=extension.lower()))  # Stores filename and extension in a list.
    return files_w_extension

def get_folder_extensions() -> dict:
    """
    Attempts to read a JSON configuration file to map file extensions to folder names.
    If the file 'config.json' is not found, it logs an error and stops the program.
    """
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        add_to_logs("Error[StoppedProgram]: 'config.json' not found in the current directory.\n")
        exit()
        
def add_to_logs(info):
    """
    Writes a log entry to 'Logs.txt' with a timestamp.
    Each entry includes the UTC time and the provided information.
    In case of an error during logging, it prints an error message.
    """
    try: 
        log_file_path = os.path.join(os.path.dirname(__file__), 'Logs.txt')
        with open(log_file_path, 'a+') as f:
            timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            f.write(f"{timestamp} - {info}")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def create_folders() -> None:
    """
    Creates folders on the Desktop based on the configuration from 'config.json'.
    The folders are named according to the keys in the configuration file.
    """
    folder_extensions = get_folder_extensions()
    for folders in folder_extensions:
        foldername_create = r"C:\\Users\\isaac\\Desktop\\{}".format(folders)
        if not os.path.exists(foldername_create):
            os.makedirs(foldername_create)
            
def relocating_files_folders():
    """
    Relocates files from the Desktop to the appropriate folders based on their extensions.
    It uses the mappings from 'config.json' to determine the destination folders.
    The script file itself is skipped to avoid relocating the script during execution.
    Logs are written in case of errors or unhandled file extensions.
    """
    script_name = os.path.basename(__file__) 
    files_to_see = get_files_extensions()
    folder_extension = get_folder_extensions()

    for files in files_to_see:
        if files["filename"] + files["extension"] == script_name:
            continue  # Skips the script file itself.

        if files["extension"] in folder_extension.values():
            get_key = list(folder_extension.keys())[list(folder_extension.values()).index(files["extension"])]

            source = r"C:\\Users\\isaac\\Desktop\\" + files["filename"] + files["extension"]
            destination = r"C:\\Users\\isaac\\Desktop\\" + get_key + "\\" + files["filename"] + files["extension"]
            try:
                if files["filename"]+files["extension"] not in folder_extension.keys():
                    os.rename(source, destination)  # Moves the file to the appropriate folder.
                # If the file is a folder itself, do nothing.
            except FileExistsError:
                add_to_logs(f"File {files['filename']}{files['extension']} already exists in {get_key}. Skipping.\n")
            except Exception as e:
                add_to_logs(f"Error moving {files['filename']}{files['extension']}: {e}\n")
        else:
            add_to_logs("No file extension for "+ files["filename"]+ files["extension"]+" if you want this extension, modify the config file!\n")
         
def main() -> None:
    """
    The main function that orchestrates the folder creation and file relocation.
    It first creates folders as per 'config.json' and then relocates files accordingly.
    """
    create_folders()
    relocating_files_folders()

if __name__ == "__main__":
    main()
