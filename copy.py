import os
import sys
import win32file
import win32con

def get_file_times(filepath):
    """Retrieve the creation, modification, and access times of a file."""
    try:
        handle = win32file.CreateFile(
            filepath,
            win32con.GENERIC_READ,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL,
            None,
        )
        created, accessed, written = win32file.GetFileTime(handle)
        win32file.CloseHandle(handle)
        return created, accessed, written
    except Exception as e:
        print(f"Error getting times for {filepath}: {e}")
        return None, None, None

def set_file_times(filepath, created, accessed, written):
    """Set the creation, modification, and access times of a file."""
    try:
        handle = win32file.CreateFile(
            filepath,
            win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL,
            None,
        )
        win32file.SetFileTime(handle, created, accessed, written)
        win32file.CloseHandle(handle)
    except Exception as e:
        print(f"Error setting times for {filepath}: {e}")

def copy_metadata(source_folder, dest_folder):
    """Copy metadata from source folder files to matching destination folder files."""
    source_files = {os.path.splitext(file)[0]: file for file in os.listdir(source_folder)}
    for root, _, files in os.walk(dest_folder):
        for file in files:
            base_name = os.path.splitext(file)[0]
            if base_name in source_files:
                source_file = os.path.join(source_folder, source_files[base_name])
                dest_file = os.path.join(root, file)

                print(f"Checking for source file: {source_file}")  # Debug line

                if os.path.exists(source_file):
                    created, accessed, written = get_file_times(source_file)
                    if created and accessed and written:
                        set_file_times(dest_file, created, accessed, written)
                        print(f"Copied metadata from '{source_file}' to '{dest_file}'")
                    else:
                        print(f"Failed to get times for source file '{source_file}'")
                else:
                    print(f"Source file '{source_file}' not found for destination file '{dest_file}'")
            else:
                print(f"No matching source file for '{file}'")

if __name__ == "__main__":
    source_folder = input("Enter the path to the source folder: ")
    dest_folder = input("Enter the path to the destination folder: ")

    if not os.path.exists(source_folder):
        print(f"The source folder '{source_folder}' does not exist.")
        sys.exit(1)

    if not os.path.exists(dest_folder):
        print(f"The destination folder '{dest_folder}' does not exist.")
        sys.exit(1)

    copy_metadata(source_folder, dest_folder)
