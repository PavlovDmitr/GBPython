from traitlets import Callable
from task_last import Animal, Dog, Fish, Kotopes


class AnimalFactory(object):

    @staticmethod
    def get(*args, **kwargs) -> object:
        if type(kwargs['class_name']) != str:
            raise ValueError("class_name must be a string!")
        
        raw_subclasses_ = Animal.__subclasses__()
        classes: dict[str, Callable[..., object]] = {c.__name__:c for c in raw_subclasses_}
        class_ = classes.get(kwargs.get('class_name', None), None)
        # args = args[1:]
        # print(kwargs)
        if class_ is not None:
            return class_()

        raise ValueError
    

if __name__ == "__main__":
    class_factory = AnimalFactory()
    class_dog = class_factory.get(class_name = "Dog")
    print(class_dog)
    poppy = class_dog.__new__(Dog, name = 'Poppy',
                            age = 12, breed = 'Злая',
                            color = 'red' 
                            )  #name = 'Poppy', age = 12, breed = 'Злая', color = 'red'
    
    print(poppy)