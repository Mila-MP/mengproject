from abc import ABC, abstractmethod

from . import containers as cont
from . import samples as samp
from . import instruments as inst


class Event(ABC):
    def __init__(self):
        self.status = "instantiated"

    @abstractmethod  # any subclass of Event must implement the run method, or it will raise an error at instantiation.
    def run(self):
        pass


class MakeSample(Event):
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
        if self.status == "Completed":
            raise RuntimeError("This event has already been completed")
        else:
            samp.Sample(
                self.sample_name, self.components, self.container, is_template=False
            )
            self.status = "Completed"


class Mix(Event):
    def __init__(self, mixer_bowl: cont.MixerBowl, mixer: inst.Mixer, sample_name: str):
        super().__init__()
        self.mixer_bowl = mixer_bowl
        self.mixer = mixer
        self.sample_name = sample_name

    def run(self):
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
