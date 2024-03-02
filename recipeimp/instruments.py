class Instrument:
    def __init__(self):
        self.status = "free"


class Mixer(Instrument):
    def __init__(self, name):
        super().__init__()
        self.name = name
