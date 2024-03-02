class Container:
    def __init__(self):
        self.content = list()


class MixerBowl(Container):
    def __init__(self, name, volume):
        super().__init__()
        self.name = name
        self.volume = volume
