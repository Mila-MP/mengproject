"""
Classes:
- Container (Parent class)
- MixerBowl (Child class)
"""


class Container:
    """
    Attributes:
        content: a list of Component and/or Sample objects indicating the content of the container.
    """

    def __init__(self):
        self.content = list()


class MixerBowl(Container):
    """
    Attributes:
        content: a list of Component and/or Sample objects indicating the content of the container.
        name: a string indicating the name of the container.
        volume: a float indicating the volume of the container in mL.
    """

    def __init__(self, name: str, volume: float):
        super().__init__()
        self.name = name
        self.volume = volume
