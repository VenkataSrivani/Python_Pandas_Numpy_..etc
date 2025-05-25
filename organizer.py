# This is a sample Python script which helps organize files into folders based on their file type

# Importing required libraries
import os         # for file and directory operations
import shutil     # to move files from one directory to another
import logging    # for recording script activities in a log file

# Set up logging configuration to track script activities
logging.basicConfig(filename='organizer.log',  # Log file name
                    level=logging.INFO,        # Log level
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define file types and their corresponding folder names
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.sql', '.html', '.java', '.csv', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Others': []  # Default folder for uncategorized file types
}

# Function to create a new folder if it doesn't already exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.info(f"Created folder: {folder_path}")

# Function to get the folder name based on file extension
def get_file_type(extension):
    for folder, ext_list in FILE_TYPES.items():
        if extension.lower() in ext_list:
            return folder
    return 'Others'  # This should be outside the loop to avoid returning 'Others' too early

# Main function to organize files in the given directory
def organize_files(directory):
    try:
        # Loop through each item in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)  # Get full path

            # Only proceed if it's a file (not a folder)
            if os.path.isfile(file_path):
                _, extension = os.path.splitext(filename)  # Split file name and extension
                folder_name = get_file_type(extension)     # Get folder name based on extension

                target_folder = os.path.join(directory, folder_name)  # Target folder path
                create_folder(target_folder)                          # Create the folder if needed

                target_path = os.path.join(target_folder, filename)   # New location for the file

                shutil.move(file_path, target_path)                   # Move the file
                logging.info(f"Moved '{filename}' to '{folder_name}'")  # Log the move

    except Exception as e:
        # Log any error that occurs during the process
        logging.error(f"Error occurred: {str(e)}")

# Entry point: Ask the user for a folder path and start organizing
if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ").strip()

    # Check if the directory exists before proceeding
    if os.path.exists(target_directory):
        organize_files(target_directory)
        print("Files have been organized.")
    else:
        print("Invalid directory path.")
