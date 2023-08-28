from pathlib import Path
from os import sep as sys_sep

def listing_sub_dir(path: str, dir_tree: list):
    p = Path(path)
    ldc = 0
    for item in p.iterdir():
        if item.is_dir():
            dir_tree.append({str(item).split(f'{sys_sep}')[1]: []})
            ldc += 1
        else: dir_tree.append({str(item).split(f'{sys_sep}')[1]: 'file'})
    return ldc

def main():
    # dir_tree = []
    
    # last_dir_count = listing_sub_dir(path, dir_tree)
    # while last_dir_count > 0:
      
    #   last_dir_count = listing_sub_dir(path, dir_tree)  

# print('-----------------------------------------------')
# for item in  list(p.glob('**/*')):
#     for i in item.parts:
    path = './lesson8'
    p = Path(path)

    list_dir = list(p.glob(f'**{sys_sep}*'))
    #list_dir[0].parts
    dir_tree = []
    for file_abs_path in list_dir:
        print('---------------------', file_abs_path, '------------------------')
        dir_tree_depth = len(file_abs_path.parts)
        for item in file_abs_path.parts:
            
            if dir_tree.count(item) == 0:
                print('next append')
                print(item, '---> ', dir_tree)
                if dir_tree_depth > 1:
                    dir_tree.append(f'{item}')
                    dir_tree_depth -= 1
                else:
                    dir_tree.append(f'{item}')
                    dir_tree_depth -= 1
            else: continue

           
        #    print(item) 
    print(dir_tree)





if __name__ == "__main__":
    main()
    # print(listing_sub_dir('./lesson8'))