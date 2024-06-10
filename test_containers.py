"""Tests for the containers module"""

import unittest
import data_model.containers as cont
import data_model.samples as samp


class TestContainer(unittest.TestCase):
    """Tests the Container class"""

    def setUp(self):
        self.bowl_1 = cont.Bowl("bowl 1", 500)
        self.bowl_2 = cont.Bowl("bowl 2", 500)
        self.bowl_3 = cont.Bowl("bowl 3", 500)

        self.butter = samp.Component("Butter", 50, "g")
        self.eggs = samp.Component("Egg", 2, "unit")
        self.flour = samp.Component("Flour", 120, "g")
        self.sugar = samp.Component("Sugar", 40, "g")

        self.bowl_1.content = [self.butter, self.eggs]

        self.test_sample = samp.Sample(
            "test sample",
            [self.flour, self.sugar],
            self.bowl_2,
            is_template=False,
        )

    def test_get_content(self):
        """Tests the get_content method of the Container class"""
        # Test with only components
        self.assertEqual(self.bowl_1.get_content(), [self.butter, self.eggs])
        # Test with only one sample
        self.assertEqual(self.bowl_2.get_content(), [self.test_sample])

    def test_append_content(self):
        """Tests the append_content method of the Container class"""
        # Test with empty container and single component input
        self.bowl_3.append_content(self.sugar)
        self.assertEqual(self.bowl_3.get_content(), [self.sugar])

        # Test with non-empty container and single component input
        self.bowl_1.append_content(self.sugar)
        expected_content = [self.butter, self.eggs, self.sugar]
        self.assertEqual(self.bowl_1.get_content(), expected_content)

        # Test with empty container and several component input
        # (i.e. list of components)
        self.bowl_3.clear_content()
        self.bowl_3.append_content([self.butter, self.eggs])
        self.assertEqual(self.bowl_3.get_content(), [self.butter, self.eggs])

        # Test with non-empty container and several component input
        # (i.e. list of components)
        self.bowl_3.append_content([self.flour, self.sugar])
        expected_content = [self.butter, self.eggs, self.flour, self.sugar]
        self.assertEqual(self.bowl_3.get_content(), expected_content)
