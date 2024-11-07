from typing import NewType

class Bun:
    @staticmethod
    def add_frank(frank: str):
        ...


def dispense_bun() -> Bun:
    return Bun()

def dispense_frank() -> str:
    return "Frank"

def dispense_ketchup():
    ...

def dispense_mustard():
    ...

class HotDog:
    def add_condiments(self, *args):
        ...

ReadyToServeHotDog = NewType('ReadyToServeHotDog', HotDog)

def disense_hot_dog_to_customer(h: HotDog):
    ...

def serve_to_customer(hd: ReadyToServeHotDog):
    ...

def dispense_hotdog():
    bun = dispense_bun()
    frank = dispense_frank()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    hot_dog.add_condiments(ketchup, mustard)
    dispense_hot_dog_to_customer(hot_dog)

def make_snack():
    return serve_to_customer(ReadToServeHotDog(HotDog))

make_snack()
