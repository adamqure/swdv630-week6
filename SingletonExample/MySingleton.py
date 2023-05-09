import uuid

class MySingleton(object):
    __instance = None
    id = uuid.uuid4()


    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(MySingleton, cls).__new__(cls)
        return cls.__instance
    

def main():
    s1Instance = MySingleton()
    s2Instance = MySingleton()

    print(s1Instance.id == s2Instance.id)

main()
