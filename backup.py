import os            # To work with files and directories
import sys           # To read command-line arguments
import shutil        # To copy files
from datetime import datetime  # To get the current date and time

def backup_files(source_dir, destination_dir):
    # Check if the source folder exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source folder '{source_dir}' does not exist.")
        return

    # Check if the destination folder exists
    if not os.path.isdir(destination_dir):
        print(f"Error: Destination folder '{destination_dir}' does not exist.")
        return

    # Get the list of files in the source folder
    files = os.listdir(source_dir)

    # If the folder is empty, let the user know
    if not files:
        print("The source folder is empty. Nothing to back up.")
        return        #returns none by default 

    # Loop through each file in the source folder
    for file_name in files:
        source_file_path = os.path.join(source_dir, file_name)

        # Skip any folders; only back up files
        if not os.path.isfile(source_file_path):
            continue

        # Create the full path for the file in the destination folder
        dest_file_path = os.path.join(destination_dir, file_name)

        # If a file with the same name already exists in the destination,
        # add a timestamp to the new file name to avoid overwriting
        if os.path.exists(dest_file_path):
            # Split the file name into name and extension
            name, extension = os.path.splitext(file_name)

            # Create a timestamp (example '2025'06'13_00-00-00 in singleline)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

            # Create a new unique file name
            new_file_name = f"{name}_{timestamp}{extension}"
            dest_file_path = os.path.join(destination_dir, new_file_name)

        try:
            # Copy the file (including metadata like modified time)
            shutil.copy2(source_file_path, dest_file_path)
            print(f"Copied: {file_name} → {dest_file_path}")
        except Exception as e:
            print(f"Error copying '{file_name}': {e}")

def main():
    # Check if user gave the correct number of arguments in command line
    if len(sys.argv) != 3:             # for less than 2 arguement it will print messaage
        print("Usage: python backup.py <source_folder> <destination_folder>")
        return

    # Get the folder paths from the command-line arguments
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    # Run the backup process
    backup_files(source_dir, destination_dir)

# This means run the main() function only if this file is run directly
if __name__ == "__main__":
    main()