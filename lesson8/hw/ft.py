import os
import json, csv, pickle
from pathlib import Path

def scan_folder(path):
    entries = os.listdir(path)

    if not entries:
        return None

    if len(entries) > 1:
        result = []
        for entry in entries:
            entry_path = path + '/' + entry
            if os.path.isfile(entry_path):
                result.append(entry)
            else:
                result.append(
                    { entry: scan_folder(entry_path) }
                )
        return result

    
    entry = entries[0]
    entry_path = path + '/' + entry
    if os.path.isfile(entry_path):
        return entry
    else:
        return { entry: scan_folder(entry_path) }


dir = { f'{os.getcwd()}': scan_folder(os.getcwd())}
with open('folder.json', 'w') as file:

    file.write( json.dumps(dir, indent=2, sort_keys=True).replace(": null",": None"))

with open('folder.csv', 'w') as file:
    csv_write = csv.DictWriter(file, fieldnames=[''], quoting=csv.QUOTE_ALL)
    

    all_data = [dir.get(x) for x in dir.keys()]
    print(all_data)
    # csv_write.writerows(all_data)