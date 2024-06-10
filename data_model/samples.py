"""
Classes:
- Component (dataclass)
- Sample
"""

from dataclasses import dataclass
from . import containers as cont


@dataclass
class Component:
    """Component of a sample.

    A component is the equivalent of an ingredient in a recipe or protocol.

    Attributes:
        name: a string indicating the name of the component.
        quantity: a float indicating the quantity of the component.
        unit: a string indicating the unit of the quantity.
    """

    name: str
    quantity: float
    unit: str


class Sample:
    """A mixture of components.

    A sample consists of a mixture of components. It can be a physical
    sample (is_template=False) or a template sample (is_template=True).
    Physical samples need a container as they represent a physical item.

    Attributes:
        name: a string indicating the name of the sample.
        components: a list of Component objects indicating the
        components in the sample.
        container: a Container object indicating the vessel of the sample
        if is_template=False.
        is_template: boolean indicating if the sample is a template or not.
    """

    def __init__(
        self,
        name: str,
        components: list,
        container: "cont.Container" = None,
        is_template: bool = False,
    ):
        self.name = name
        self.components = components
        self.is_template = is_template

        if not self.is_template:  # If sample is physical
            if container is None:
                raise ValueError("Physical samples require a container.")
            if container.get_content():
                raise ValueError("The container should be empty")
            self.container = container
            self.container.content.append(self)
        else:  # If sample is a template
            if container is not None:
                raise ValueError("Template samples should not have a container.")
            self.container = None

    def get_components(self):
        """Returns the components attribute of the sample (list)"""
        return self.components
