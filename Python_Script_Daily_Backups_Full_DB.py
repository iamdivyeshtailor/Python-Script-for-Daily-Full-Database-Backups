import os
import subprocess
import datetime
import shutil

# Define the projects and their MongoDB URIs
projects = {
    "communitycare_staging": "mongodb+srv://tokyo:Gt5oQwYI8WlZ7lYC@cluster0.tn0psgd.mongodb.net/",
    "communitycare_production": "mongodb+srv://breadoflife:GMacsSpeLh0ctERK@bread-of-life.ogrxal7.mongodb.net/",
    "proofmetrix_staging": "mongodb+srv://jensikamaldhari:X068kSvQA9h97t5e@cluster0.qpnwn8m.mongodb.net",
    "proofmetrix_production": "mongodb+srv://doadmin:O14kcK398702eWVT@proofmetrix-2359b83d.mongo.ondigitalocean.com",
    "boilerplate": "mongodb+srv://boliderplaate_user:94puQ5vMAfHK0KRj@cluster0.scdcs.mongodb.net",
    #"qrcode_staging": ""
}

# Get the current date and time
current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Base backup directory
base_backup_dir = "/root/All_MERN_DBs-Backups/"

def backup_project(project_name, uri):
    # Define the backup directory for the current project
    backup_dir = os.path.join(base_backup_dir, project_name, current_date)

    # Create the backup directory
    os.makedirs(backup_dir, exist_ok=True)

    # Perform the MongoDB backup using mongodump
    result = subprocess.run(["mongodump", "--uri", uri, "-o", backup_dir], capture_output=True, text=True)

    # Check if the backup was successful
    if result.returncode == 0:
        print(f"MongoDB backup for {project_name} completed successfully.")
        # Remove backups older than one week
        remove_old_backups(os.path.join(base_backup_dir, project_name))
    else:
        print(f"Error: MongoDB backup for {project_name} failed.")
        print(result.stderr)

def remove_old_backups(project_backup_dir):
    # Get the current time
    now = datetime.datetime.now()
    # Iterate through the backup directories
    for dirname in os.listdir(project_backup_dir):
        dirpath = os.path.join(project_backup_dir, dirname)
        # Check if it's a directory and older than one week
        if os.path.isdir(dirpath):
            dir_time = datetime.datetime.strptime(dirname, "%Y-%m-%d_%H-%M-%S")
            if (now - dir_time).days > 7:
                shutil.rmtree(dirpath)
                print(f"Removed old backup: {dirpath}")

def main():
    for project_name, uri in projects.items():
        backup_project(project_name, uri)

if __name__ == "__main__":
    main()
