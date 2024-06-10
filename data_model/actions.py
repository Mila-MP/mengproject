"""
Classes:
- Action (Parent class)
- Mix (Child class)
- Transfer (Child class)
"""

from abc import ABC, abstractmethod

from . import containers as cont
from . import samples as samp
from . import instruments as inst


class Action(ABC):
    """A step in workflow

    An action is the smallest division of a workflow.
    All subclasses of Action have a run method which models the execution of the action.

    Attributes:
        status: a string indicating the status of the action
        ("Instatiated", "Completed"...).

    Methods:
        run: abstract method that models the execution of the action.
    """

    def __init__(self):
        self.status = "Instantiated"

    @abstractmethod
    def run(self):
        """Models the execution of the action"""


class Mix(Action):
    """Mixes components and/or samples to make a new sample.

    The Mix action is used to combines the input components and/or
    samples into a new sample. This action requires a mixer and a mixer bowl,
    whose content attribute holds the input components and/or samples.
    The new sample's container is the inputted mixer bowl.

    Attributes:
        status: a string indicating the status of the action
        ("Instatiated", "Completed"...).
        mixer_bowl: a MixerBowl object containing the input components and/or samples.
        inst: an Instrument object indicating on which instrument the action is run.
        sample_name: a string indicating the name of the sample to be created.

    Methods:
        run: executes the Mix action.
    """

    def __init__(self, bowl: cont.Bowl, instrument: inst.Instrument, sample_name: str):
        super().__init__()
        self.bowl = bowl
        self.instrument = instrument
        self.sample_name = sample_name

    def run(self):
        """Creates a new sample out of the input components and/or samples.

        Creates a new sample made out of the components and/or
        samples in the mixer_bowl attribute. The new sample will
        be composed of the input components and the components of the input samples.

        Raises:
            RuntimeError: The Mix action cannot be run if its status
            is already "completed".
            ValueError: The instrument cannot perform the Mix action.
        """
        if "Mix" not in self.instrument.actions:
            raise ValueError("The chosen instrument cannot perform the Mix action")
        if self.status == "Completed":
            raise RuntimeError("This action has already been completed.")
        content = self.bowl.get_content()  # List of components and samples
        new_sample_components = []
        for element in content:
            if isinstance(element, samp.Sample):
                for x in element.components:
                    new_sample_components.append(x)
            if isinstance(element, samp.Component):
                new_sample_components.append(element)
        self.bowl.clear_content()
        samp.Sample(
            self.sample_name,
            new_sample_components,
            self.bowl,
            is_template=False,
        )
        self.status = "Completed"


class Transfer(Action):
    """Transfers a sample from its original container to another.

    Attributes:
        status: a string indicating the status of the action
        ("Instatiated", "Completed"...).
        orig_container: Container object only containing the sample to be transferred
        recipient: empty Container object to which the sample will be transferred to.

    Methods:
        run: executes the Transfer action.
    """

    def __init__(self, orig_container: cont.Container, recipient: cont.Container):
        super().__init__()

        # Check that original container only contains one sample
        if not orig_container.get_content():
            raise ValueError("The original container is empty")
        if len(orig_container.get_content()) != 1:
            raise ValueError("The original container contains more that one element")
        elif not isinstance(orig_container.get_content()[0], samp.Sample):
            raise ValueError("The content of the container is not a sample object")
        self.orig_container = orig_container

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

        # Extract sample from original container
        sample = self.orig_container.get_content()[0]

        # Transfer sample to recipient
        sample.container = self.recipient
        self.recipient.content.append(sample)
        self.orig_container.clear_content()

        self.status = "Completed"
