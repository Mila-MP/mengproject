from . import containers as cont
from . import sample as samp


class Event:
    def __init__(self):
        self.status = "instantiated"


class MakeSample(Event):
    def __init__(self, sample_name: str, container: cont.Container, components: list):
        super().__init__()
        self.sample_name = sample_name
        self.container = container
        self.components = components

    @property
    def container(self):
        return self._container

    @container.setter
    def container(self, value):
        if not isinstance(value, cont.Container):
            raise TypeError("The container should be of Container class")
        self._container = value

    def run(self):
        if self.container.content:
            print("The chosen container is not empty, please choose another one")
        elif self.status == "completed":
            print("This event has already been completed")
        else:
            sample = samp.Sample(
                self.sample_name, self.components, self.container, is_template=False
            )
            container_content = self.container.content
            container_content.append(sample)
            self.status = "Completed"
