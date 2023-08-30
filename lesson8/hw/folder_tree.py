import os
import json, csv, pickle
from pathlib import Path
from os import sep as sys_sep

def listing_sub_dir(path: str, dir_tree: list):
    p = Path(path)
    pdlist = []
    if p.is_dir():
        pdlist.append(p)
    while len(pdlist) > 0:
        p = pdlist.pop()
        for item in p.iterdir():
            item_fish = {'name': str(item).split(f'{sys_sep}')[-1],
                                "parent": str(item).split(f'{sys_sep}')[-2],
                                'type': '', 
                                'size': os.path.getsize(item)}
            if item.is_dir():
                item_fish['type'] = 'folder'
                dir_tree.append(item_fish)
                pdlist.append(item)
            else:
                item_fish['type'] = 'file'
                dir_tree.append(item_fish)

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
                result.append({ entry: scan_folder(entry_path) })
        return result
    entry = entries[0]
    entry_path = path + '/' + entry
    if os.path.isfile(entry_path):
        return entry
    else:
        return { entry: scan_folder(entry_path) }
    

def main():
    dir = { f'{os.getcwd()}': scan_folder(os.getcwd())}
    with open('folder.json', 'w') as file:
        file.write( json.dumps(dir, indent=2, sort_keys=True).replace(": null",": None"))
    with open('folder.csv', 'w', newline='') as file:
        all_data = []
        csv_write = csv.DictWriter(file, fieldnames=['name', 'parent', 'type', 'size'], quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        listing_sub_dir(os.getcwd(), all_data)
        csv_write.writerows(all_data)

    with open('folder.bin', 'wb') as file:
        pickle.dump(dir, file)


if __name__ == '__main__':
    main()
    