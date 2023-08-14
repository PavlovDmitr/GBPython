_table = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]



def check_8_queens(combination: list) -> bool:
    
    
    for item in combination:
        for i in range(7):
            if (i == item[0] and 1 in _table[item[0]]) or _table[item[0]][item[1]] == 2:
                return False
            elif i == item[0]: 
                for j in range(7): 
                    _table[i][j] = 1
                    
            else: 
                _table[i][item[1]] = 1
                switch = 4
                x = 1
                y = 1
                while switch > 0:
                    if item[0] + x <= 7 and item[1] + y <= 7: 
                        _table[item[0] + x][item[1] + y] = 2
                    if item[0] + x >= 7 or item[1] + y >= 7:
                        switch -= 1
                        
                    if item[0] + x <= 7 and item[1] - y >= 0: 
                        _table[item[0] + x][item[1] - y] = 2
                    if item[0] + x >= 7 or item[1] - y <= 0:
                        switch -= 1
                        
                    if item[0] - x >= 0 and item[1] + y <= 7: 
                        _table[item[0] - x][item[1] + y] = 2
                    if item[0] - x <= 0 or item[1] + y >= 7:
                        switch -= 1
                        
                    if item[0] - x >= 0 and item[1] - y >= 0: 
                        _table[item[0] - x][item[1] - y] = 2
                    if item[0] - x <= 0 or item[1] - y <= 0:
                        switch -= 1
                        
                    x += 1
                    y += 1
                    pass


                    
                

    return True

