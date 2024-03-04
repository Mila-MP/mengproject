"""
Classes:
- Event (Parent class)
- MakeSample (Child class)
- Mix (Child class)
"""

from abc import ABC, abstractmethod

from . import containers as cont
from . import samples as samp
from . import instruments as inst


class Event(ABC):
    """A step in workflow

    An event is the smallest division of a workflow. All subclasses of Event have a run method
    which models the execution of the event.

    Attributes:
        status: a string indicating the status of the event ("Instatiated", "Completed"...).
    """

    def __init__(self):
        self.status = "Instantiated"

    @abstractmethod  # subclasses of Event must implement run method
    def run(self):
        """Models the execution of the event"""


class MakeSample(Event):
    """An event used to make a sample.

    The MakeSample event is used to make a sample out of the input components. The sample created is a
    physical sample so it requires a container, which must be empty.

    Attributes:
        status: a string indicating the status of the event ("Instatiated", "Completed"...).
        sample_name: a string indicating the name of the sample to be created.
        container: a Container object indicating the vessel of the sample to be created.
        components: a list of Component objects indicating the content of the sample to be created.
    """

    def __init__(self, sample_name: str, container: cont.Container, components: list):

        super().__init__()

        if container.content:  # if container is not empty, event is not instantiated
            raise ValueError(
                "The chosen container is not empty, please choose another one."
            )

        self.sample_name = sample_name
        self.container = container
        self.components = components

    def run(self):
        """Creates the sample

        Creates a sample based of the attributes of the MakeSample event.

        Raises:
            RuntimeError: The MakeSample event cannot be run if its status is already "completed".
        """
        if self.status == "Completed":
            raise RuntimeError("This event has already been completed")
        else:
            samp.Sample(
                self.sample_name, self.components, self.container, is_template=False
            )
            self.status = "Completed"


class Mix(Event):
    """Mixes components and/or samples to make a new sample.

    The Mix event is used to combines the input components and/or samples into a new sample.
    This event requires a mixer and a mixer bowl, whose content attribute holds the input
    components and/or samples. The new sample's container is the inputted mixer bowl.

    Attribute:
        status: a string indicating the status of the event ("Instatiated", "Completed"...).
        mixer_bowl: a MixerBowl object containing the input components and/or samples.
        mixer: a Mixer object indicating on which mixer the event is run.
        sample_name: a string indicating the name of the sample to be created.

    """

    def __init__(self, mixer_bowl: cont.MixerBowl, mixer: inst.Mixer, sample_name: str):
        super().__init__()
        self.mixer_bowl = mixer_bowl
        self.mixer = mixer
        self.sample_name = sample_name

    def run(self):
        """Creates a new sample out of the input components and/or samples.

        Creates a new sample made out of the components and/or samples in the mixer_bowl attribute.
        The new sample will be composed of the input components and the components of the input samples.

        Raises:
            RuntimeError: The Mix event cannot be run if its status is already "completed".
        """
        if self.status == "Completed":
            raise RuntimeError("This event has already been completed")
        else:
            content = self.mixer_bowl.content  # List of components and samples
            new_sample_components = list()
            for element in content:
                if isinstance(element, samp.Sample):
                    for x in element.components:
                        new_sample_components.append(x)
                if isinstance(element, samp.Component):
                    new_sample_components.append(element)
            self.mixer_bowl.content.clear()
            samp.Sample(
                self.sample_name,
                new_sample_components,
                self.mixer_bowl,
                is_template=False,
            )
            self.status = "Completed"
