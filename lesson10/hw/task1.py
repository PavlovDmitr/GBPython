from traitlets import Callable
from task_last import Animal, Dog, Fish, Kotopes


class Factory(object):

    @staticmethod
    def get(*args, **kwargs) -> object:
        if type(kwargs['class_']) != str:
            raise ValueError("class_name must be a string!")
        
        raw_subclasses_ = Animal.__subclasses__()
        classes: dict[str, Callable[..., object]] = {c.__name__:c for c in raw_subclasses_}
        class_ = classes.get(kwargs.pop('class_', None), None)
        # args = args[1:]
        print(kwargs)
        if class_ is not None:
            return class_(kwargs)

        raise ValueError
    

if __name__ == "__main__":
    class_ = Factory.get(class_ = 'Dog', name = 'Бобик',
                        age = 3, color =  "рыжий",
                        breed = "спаниель", is_domestic = True)
    print(class_)