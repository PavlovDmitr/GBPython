# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.(Может помочь метод translate из модуля string)


TEXT = '''Python standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.

In addition to the standard library, there is an active collection of hundreds of thousands of components (from individual programs and modules to packages and entire application development frameworks), available from'''


def main():
    result = {}
    result_top = []
    result_top_count = 10
    text = TEXT.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('\n', ' ').split(' ')
    for item in text:
        if result.get(item):
           result[item] += 1
        else: result[item] = 1

    res = list((result).values())
    res.sort(reverse=True)
    res_dict = dict(sorted(result.items(), key=lambda item:item[1], reverse= True))
    print(res[:result_top_count])
    
    for item in res_dict.keys():
        if result_top_count > 0: 
            result_top.append(item)
            result_top_count -= 1
    print(result_top)
    

if __name__ == "__main__":
    main()