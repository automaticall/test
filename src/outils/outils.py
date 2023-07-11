
class Outils:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Outils contains importante functions"
    
    def __len__(self):
        pass
    @staticmethod
    def add(**kwargs) -> int:
        return kwargs["a"] + kwargs["b"]
    
    def modulo(self,config):
        """ write modulo function"""
        try:
            reset = self.add(a=config["a"] , b=config["b"] ) % config["q"]
            print(reset)
            return reset
        except:
            print("error contact the dev, or make sure your enter right data")
        