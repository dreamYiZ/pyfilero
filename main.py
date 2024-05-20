import os
import shutil
import sys

def move_files_to_root_dir(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if dirpath != root_dir:
            for file_name in filenames:
                new_name = file_name
                while os.path.exists(os.path.join(root_dir, new_name)):
                    base, ext = os.path.splitext(new_name)
                    new_name = base + '_1' + ext
                shutil.move(os.path.join(dirpath, file_name), os.path.join(root_dir, new_name))

def remove_empty_folders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if dirpath != root_dir and not os.listdir(dirpath):
            os.rmdir(dirpath)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    root_dir = sys.argv[1]

    move_files_to_root_dir(root_dir)
    remove_empty_folders(root_dir)

if __name__ == "__main__":
    main()
