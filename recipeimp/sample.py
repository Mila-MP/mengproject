from dataclasses import dataclass
from . import containers as cont


@dataclass
class Components:
    name: str
    quantity: float
    unit: str


class Sample:
    def __init__(
        self,
        name: str,
        components: list,
        container: cont.Container = None,
        is_template: bool = False,
    ):
        self.name = name
        self.components = components
        self.is_template = is_template

        if not self.is_template:  # If sample is physical
            if container is None:
                raise ValueError("Physical samples require a container.")
            self.container = container
        else:  # If sample is a template
            if container is not None:
                raise ValueError("Template samples should not have a container.")
            self.container = None
