import pack01
import time


if __name__ == "__main__":
    pack01.create_files('.txt')
    time.sleep(3)
    pack01.rename(wanted_name = "video", count_nums=5, 
                  extension_old=".txt", extension_new=".csv", 
                  diapazon=[1, 6])
    
    time.sleep(5)
    pack01.remove(extension_del='.csv')

