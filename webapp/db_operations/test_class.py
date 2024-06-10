from dataclasses import dataclass


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
