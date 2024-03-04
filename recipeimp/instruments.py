"""
Classes:
- Instrument (Parent class)
- Mixer (child class)
"""


class Instrument:
    """
    Attributes:
        status: a string indicating the status of the instrument ("free", "in use"...).
    """

    def __init__(self):
        self.status = "free"


class Mixer(Instrument):
    """
    Attributes:
        status: a string indicating the status of the instrument ("free", "in use"...).
        name : a string indicating the name of the mixer.
    """

    def __init__(self, name: str):
        super().__init__()
        self.name = name
