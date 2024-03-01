class Instrument:
    def __init__(self, name):
        self.name = name
        self.status = "free"


class Mixer(Instrument):
    def __init__(self, name):
        super().__init__(name)
