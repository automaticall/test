
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
        reset = self.add(a=config["a"] , b=config["b"] ) % config["q"]
        return reset