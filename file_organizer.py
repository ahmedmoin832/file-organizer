
import os
import shutil


EXTENSION_MAP = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Scripts",
    ".js": "Scripts",
}


def organize_folder(target_directory):
   

    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory.")
        return

   
    all_items = os.listdir(target_directory)

    moved_count = 0
    skipped_count = 0

   
    for item_name in all_items:
        item_path = os.path.join(target_directory, item_name)

        
        if os.path.isdir(item_path):
            continue

      
        _, extension = os.path.splitext(item_name)
        extension = extension.lower() 

       
        target_folder_name = EXTENSION_MAP.get(extension, "Others")
        destination_folder = os.path.join(target_directory, target_folder_name)

        try:
            
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, item_name)

            
            shutil.move(item_path, destination_path)

            print(f"Moved: {item_name}  ->  {target_folder_name}/")
            moved_count += 1

        except PermissionError:
            print(f"Skipped (permission denied): {item_name}")
            skipped_count += 1
        except shutil.Error as e:
            print(f"Skipped (could not move): {item_name} -> {e}")
            skipped_count += 1
        except Exception as e:
            
            print(f"Skipped (unexpected error): {item_name} -> {e}")
            skipped_count += 1

    print("\n--- Summary ---")
    print(f"Files moved: {moved_count}")
    print(f"Files skipped: {skipped_count}")


if __name__ == "__main__":

    folder_to_organize = input("Enter the full path of the folder to organize: ").strip()
    organize_folder(folder_to_organize)
