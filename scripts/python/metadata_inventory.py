import os

BASE_PATH = "force-app/main/default"


METADATA_FOLDERS = [
    "classes",
    "objects",
    "flows",
    "triggers",
    "permissionsets"
]

print("Checking Salesforce metadata structure...")

for folder in METADATA_FOLDERS:
    folder_path = os.path.join(BASE_PATH, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created missing folder: {folder_path}")
    else:
        print(f" Folder exists: {folder_path}")

print("Metadata structure validation completed")
