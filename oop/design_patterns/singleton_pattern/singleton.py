
class SingletonMeta(type):

    singleton_instance = None

    def __call__(cls, *args, **kwds):
        if cls.singleton_instance == None:
            instance = super().__call__(*args, **kwds)
            cls.singleton_instance = instance
        return cls.singleton_instance


class Singleton(metaclass=SingletonMeta):
    def some_logic(self):
        print("we have a Singleton")


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("yes")
    else:
        print("no")
