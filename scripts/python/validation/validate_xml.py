import xml.etree.ElementTree as ET
import sys
import os

BASE_PATH = "force-app/main/default/objects"
NAMESPACE = {"sf": "http://soap.sforce.com/2006/04/metadata"}

if not os.path.exists(BASE_PATH):
    print("Objects folder not found")
    sys.exit(1)

for file in os.listdir(BASE_PATH):
    if file.endswith(".object-meta.xml"):
        full_path = os.path.join(BASE_PATH, file)
        try:
            tree = ET.parse(full_path)
            root = tree.getroot()
        except Exception:
            print(f"Invalid XML: {file}")
            sys.exit(1)

        # Validate required tags
        label = root.find("sf:label", NAMESPACE)
        sharing = root.find("sf:sharingModel", NAMESPACE)

        if label is None or sharing is None:
            print(f"Required tag missing in {file}")
            sys.exit(1)

print("XML metadata validation passed")
