"""
Import all the neccesities.
"""

from datetime import datetime
import os
import json

def get_files_extensions() -> list:
    """
    This function is used to get all the files names and extension on the User's Desktop.
    As you can see, it returns a list object which as the files name, with the extension.
    The extension has .lower() to cause less trouble (just in case)
    """
    files_w_extension = []
    
    all_files_desktop = os.listdir(r"C:\Users\isaac\Desktop")
    separated_files = list(all_files_desktop)
    
    for filepaths in separated_files:
        file = os.path.splitext(filepaths)
        file_name = file[0]
        extension = file[1]
        files_w_extension.append(dict(filename=file_name,extension=extension.lower()))
    return files_w_extension

def get_folder_extensions() -> dict:
    """
    This function searches the config.json file and returns all the data from the inside as a dict type.
    Error handling is added just in case the File doesn't exist. (This is why json is imported at the start.
    """
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        add_to_logs("Error[StoppedProgram]: Don't run it on VSC unless it is on the terminal where the program and the config.json file are.\n")
        exit()
        
def add_to_logs(info):
    """
    This function ...
    """
    try: 
        log_file_path = os.path.join(os.path.dirname(__file__), 'Logs.txt')
        with open(log_file_path, 'a+') as f:
            timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            f.write(f"{timestamp} - {info}")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def create_folders() -> None:
    folder_extensions = get_folder_extensions()
    for folders in folder_extensions:
        foldername_create = r"C:\\Users\\isaac\\Desktop\\{}".format(folders)
        if not os.path.exists(foldername_create):
            os.makedirs(foldername_create)
            
def relocating_files_folders():
    script_name = os.path.basename(__file__) 
    files_to_see = get_files_extensions()
    folder_extension = get_folder_extensions()

    for files in files_to_see:
        if files["filename"] + files["extension"] == script_name:
            continue

        if files["extension"] in folder_extension.values():
            get_key = list(folder_extension.keys())[list(folder_extension.values()).index(files["extension"])]

            source = r"C:\\Users\\isaac\\Desktop\\" + files["filename"] + files["extension"]
            destination = r"C:\\Users\\isaac\\Desktop\\" + get_key + "\\" + files["filename"] + files["extension"]
            try:
                if files["filename"]+files["extension"] in folder_extension.keys():
                    pass
                else:
                    os.rename(source, destination)
            except FileExistsError:
                add_to_logs(f"File {files['filename']}{files['extension']} already exists in {get_key}. Skipping.\n")
            except Exception as e:
                add_to_logs(f"Error moving {files['filename']}{files['extension']}: {e}\n")
        else:
            add_to_logs("no file extension for"+ files["filename"]+ files["extension"]+" if you want this extension, modify the config file!\n")
         
def main() -> None:
    create_folders()
    relocating_files_folders()

if __name__ == "__main__":
    main()
