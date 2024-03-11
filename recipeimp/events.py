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

    An event is the smallest division of a workflow.
    All subclasses of Event have a run method which models the execution of the event.

    Attributes:
        status: a string indicating the status of the event
        ("Instatiated", "Completed"...).

    Methods:
        run: abstract method that models the execution of the event.
    """

    def __init__(self):
        self.status = "Instantiated"

    @abstractmethod
    def run(self):
        """Models the execution of the event"""


class Mix(Event):
    """Mixes components and/or samples to make a new sample.

    The Mix event is used to combines the input components and/or
    samples into a new sample. This event requires a mixer and a mixer bowl,
    whose content attribute holds the input components and/or samples.
    The new sample's container is the inputted mixer bowl.

    Attributes:
        status: a string indicating the status of the event
        ("Instatiated", "Completed"...).
        mixer_bowl: a MixerBowl object containing the input components and/or samples.
        mixer: a Mixer object indicating on which mixer the event is run.
        sample_name: a string indicating the name of the sample to be created.

    Methods:
        run: executes the Mix event.
    """

    def __init__(self, mixer_bowl: cont.MixerBowl, mixer: inst.Mixer, sample_name: str):
        super().__init__()
        self.mixer_bowl = mixer_bowl
        self.mixer = mixer
        self.sample_name = sample_name

    def run(self):
        """Creates a new sample out of the input components and/or samples.

        Creates a new sample made out of the components and/or
        samples in the mixer_bowl
        attribute. The new sample will be composed of the input components and the
        components of the input samples.

        Raises:
            RuntimeError: The Mix event cannot be run if its status
            is already "completed".
        """
        if self.status == "Completed":
            raise RuntimeError("This event has already been completed.")
        content = self.mixer_bowl.get_content()  # List of components and samples
        new_sample_components = []
        for element in content:
            if isinstance(element, samp.Sample):
                for x in element.components:
                    new_sample_components.append(x)
            if isinstance(element, samp.Component):
                new_sample_components.append(element)
        self.mixer_bowl.clear_content()
        samp.Sample(
            self.sample_name,
            new_sample_components,
            self.mixer_bowl,
            is_template=False,
        )
        self.status = "Completed"


class Transfer(Event):
    """Transfers a sample from its original container to another.

    Attributes:
        status: a string indicating the status of the event
        ("Instatiated", "Completed"...).
        sample: the Sample object to be transferred.
        recipient: empty Container object to which the sample will be transferred to.

    Methods:
        run: executes the Transfer event.
    """

    def __init__(self, sample: samp.Sample, recipient: cont.Container):
        super().__init__()

        # Check that sample is a Sample object
        if not isinstance(sample, samp.Sample):
            raise TypeError("The sample argument should be of type Sample.")
        self.sample = sample

        # Check that recipient is empty
        if recipient.get_content():
            raise ValueError("The recipient container is not empty.")
        self.recipient = recipient

    def run(self):
        """Transfer the sample to the new recipient.

        Raises:
            RuntimeError: The Transfer event cannot be run if its status
            is already "completed".
        """
        if self.status == "Completed":
            raise RuntimeError("This event has already been completed.")

        # Extract original container from sample
        orig_container = self.sample.container

        # Check that original container only contains the sample to be transferred
        orig_container_content = orig_container.get_content()
        if orig_container_content != [self.sample]:
            raise ValueError(
                "The original container contains more than just the sample to be transferred."
            )

        # Transfer sample to recipient
        self.sample.container = self.recipient
        self.recipient.content.append(self.sample)
        orig_container.clear_content()

        self.status = "Completed"
