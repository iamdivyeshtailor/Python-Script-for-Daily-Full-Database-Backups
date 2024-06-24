# Python Script for Daily Full Database Backups

This repository contains a Python script designed to take full backups of a database daily. Follow the steps below to clone the repo, set execution permissions, schedule a cron job, and manage backup storage locations.

## Steps to Setup

### Step 1: Clone this repository
Clone the repository to your local machine using the following command:
```bash
git clone <repository-url>
```
Replace <repository-url> with the actual URL of your GitHub repository.

### Step 2: Set Execution Permissions
Ensure that the Python script has the correct execution permissions:
```bash
chmod +x Python_Script_Daily_Backups_Full_DB.py
```

### Step 3: Schedule the Cron Job
Set up a cron job to run the script at a specific time. For example, to run the script every night at 12 AM, add the following line to your crontab:
```bash
0 0 * * * /path/to/Python_Script_Daily_Backups_Full_DB
```
You can edit your crontab with the following command:
```bash
crontab -e
```
### Step 4: Locate Database Backups
By default, database backups are stored in the /root/All_MERN_DBs-Backups/ directory. You can change this path by opening the Python script and modifying the base_backup_dir variable.
```bash
base_backup_dir = '/new/backup/path'
```
### Additional Information
Ensure you have the necessary permissions to execute the script and write to the backup directory.
You may need to install certain dependencies for the script to run properly. Refer to the script documentation for more details.
Feel free to open an issue if you encounter any problems or have questions about the setup process.
