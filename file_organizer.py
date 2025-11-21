import os
import shutil
import time

# Define categories and extensions
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize(folder_path):
    """Organizes files in the given folder into subfolders based on type."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for category, extensions in EXTENSIONS.items():
                if ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved: {filename} -> {category}")
                    break

def main():
    folder = input("Enter the full path of the folder to organize: ").strip()
    if not os.path.exists(folder):
        print("Folder path does not exist. Exiting.")
        return
    organize(folder)
    print("Organization complete!")

if __name__ == "__main__":
    main()
