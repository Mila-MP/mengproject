"""
Classes:
- Container (Parent class)
- MixerBowl (Child class)
"""

from . import samples as samp


class Container:
    """
    Attributes:
        content: a list of Component and/or Sample objects
        indicating the content of the container.
    """

    def __init__(self):
        self.content = []

    def get_content(self):
        """Returns the content of the container"""
        return self.content

    def append_content(self, added_content):
        """Adds elements to the content of the container

        This method can only be used to add components to the container, not samples.
        This is because physical samples already have a container. To add a physical
        sample to a container, use the Transfer class (child of Event class).

        Args:
            added_content: component or list of components to be added to the container
        """
        if isinstance(added_content, samp.Component):
            self.content.append(added_content)
        elif isinstance(added_content, list):
            for item in added_content:
                if not isinstance(item, samp.Component):
                    raise TypeError("List contains invalid elements")
            self.content.extend(added_content)
        else:
            raise TypeError("Invalid type for added_content")

    def clear_content(self):
        """Empties the container"""
        self.content.clear()


class MixerBowl(Container):
    """
    Attributes:
        content: a list of Component and/or Sample objects indicating the
        content of the container.
        name: a string indicating the name of the container.
        volume: a float indicating the volume of the container in mL.
    """

    def __init__(self, name: str, volume: float):
        super().__init__()
        self.name = name
        self.volume = volume
