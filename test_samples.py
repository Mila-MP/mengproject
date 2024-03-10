"""Tests for the samples module"""

import unittest
import recipeimp.containers as cont
import recipeimp.samples as samp


class TestContainer(unittest.TestCase):
    """Tests the Sample class"""

    def setUp(self):
        self.mixer_bowl = cont.MixerBowl("mixer bowl", 500)
        self.butter = samp.Component("Butter", 50, "g")
        self.eggs = samp.Component("Egg", 2, "unit")
        self.flour = samp.Component("Flour", 120, "g")
        self.sugar = samp.Component("Sugar", 40, "g")

    def test_init(self):
        """Tests constructor of the Sample class"""

        # Checks that ValueError is raised if template sample is instantiated with container
        with self.assertRaises(ValueError):
            samp.Sample("test sample", [self.butter, self.eggs], self.mixer_bowl, True)

        # Checks that ValueError is raised if physical sample is instantiated without container
        with self.assertRaises(ValueError):
            samp.Sample("test sample", [self.butter, self.eggs], None, False)

        # Checks that ValueError is raised if physical sample is instantiated with non-empty container
        with self.assertRaises(ValueError):
            self.mixer_bowl.append_content([self.butter, self.eggs])
            samp.Sample("test sample", [self.flour, self.sugar], self.mixer_bowl, False)
