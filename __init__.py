import os
import json

def get_files_extensions() -> list:
    files_w_extension = []
    
    all_files_desktop = os.listdir(r"C:\Users\isaac\Desktop")
    separated_files = list(all_files_desktop)
    
    for filepaths in separated_files:
        file = os.path.splitext(filepaths)
        file_name = file[0]
        extension = file[1]
        files_w_extension.append(dict(filename=file_name,extension=extension.lower()))
    print(files_w_extension)
    return files_w_extension

def get_folder_extensions() -> dict:
    with open('config.json', 'r') as f:
        data = json.load(f)
    return data

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
                print(f"File {files['filename']}{files['extension']} already exists in {get_key}. Skipping.")
            except Exception as e:
                print(f"Error moving {files['filename']}{files['extension']}: {e}")
        else:
            print("no file extension for", files["filename"], files["extension"])

def main() -> None:
    create_folders()
    relocating_files_folders()
    
if __name__ == "__main__":
    main()