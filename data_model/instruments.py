"""
Classes:
- Instrument (Parent class)
- Mixer (child class)
- Oven (child class)
"""

from . import containers as cont
from . import samples as samp


class Instrument:
    """
    Attributes:
        status: a string indicating the status of the instrument ("free", "in use"...).
    """

    def __init__(self):
        self.status = "free"


class Mixer(Instrument):
    """
    Attributes:
        status: a string indicating the status of the instrument ("free", "in use"...).
        actions: a list of strings indicating what actions an instrument can perform.
        name : a string indicating the name of the mixer.
        max_speed: int indicating the max speed of the mixed (RPM)

    Methods:
        mix: Mix the components in mixer_bowl into a new sample.
    """

    def __init__(self, name: str, max_speed: int):
        super().__init__()
        self.actions = ["Mix"]
        self.name = name
        self.max_speed = max_speed

    def mix(self, bowl: cont.Bowl, sample_name: str, duration: int, speed: int):
        """Mix the components in mixer_bowl into a new sample.

        Creates a new sample (with name sample_name) made out of the components
        and/or samples in the mixer_bowl attribute. Mixing is done at the speed
        indicated in the speed attribute (rot/sec), and for the time indicated
        in the duration attribute (sec).
        """

        if speed > self.max_speed:
            raise ValueError("The chosen speed excedes the maximum speed of the mixer.")

        self.status = "In use"

        content = bowl.get_content()  # List of components and samples
        new_sample_components = []
        for element in content:
            if isinstance(element, samp.Sample):
                for x in element.components:
                    new_sample_components.append(x)
            if isinstance(element, samp.Component):
                new_sample_components.append(element)

        bowl.clear_content()
        samp.Sample(
            sample_name,
            new_sample_components,
            bowl,
            is_template=False,
        )

        self.status = "Free"


class Oven(Instrument):
    """
    Attributes:
        status: a string indicating the status of the instrument ("free", "in use"...).
        name : a string indicating the name of the mixer.
        capacity: an integer indicating the number of tray spaces.
        max_dim: a tuple indicating the max dimensions of the input tray in cm (L,W,H).
        max_temp: an integer indicating the maximum temperature of the oven (in °C).

    Methods:
        bake: bake content of the input tray.
        proof: proof content of the input container.
    """

    def __init__(self, name: str, capacity: int, max_dim: tuple, max_temp: int):
        super().__init__()
        self.name = name
        self.capacity = capacity
        self.max_dim = max_dim
        self.max_temp = max_temp

    def check_tray(self, tray: cont.Tray):
        """Check that the input container is a tray with adequate dimensions."""
        # Check that container is a tray
        if not isinstance(tray, cont.Tray):
            raise ValueError("The input container should be a tray.")

        # Check that the tray is not too large for the oven
        tray_dimensions = tray.dimensions
        for i in range(3):
            if tray_dimensions[i] > self.max_dim[i]:
                raise ValueError("The input tray is too large for this oven.")

    def check_temp(self, temp: int):
        """Check that the input temperature is not above the max oven temperature."""
        if temp > self.max_temp:
            raise ValueError(
                "The chosen temperature exceeds the maximum temperature of the oven."
            )

    def bake(self, tray: cont.Tray, bake_time: int, temp: int):
        self.check_tray(tray)
        self.check_temp(temp)

    def proof(self, tray: cont.Tray, proof_time: int, temp: int):
        self.check_tray(tray)
        self.check_temp(temp)
