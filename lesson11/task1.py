from time import time


class MyStr(str):
    def __new__(cls, value, name):
        
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.time_create = time()
        return instance

    def __repr__(self) -> str:
        return f'MyStr({self.value=}, {self.name=})'


if __name__ == '__main__':
    st = MyStr(value='just do it', name='JohnDou')
    print(repr(st))
    print(st.time_create)