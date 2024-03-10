"""Tests for the events module"""

import unittest
import recipeimp.containers as cont
import recipeimp.events as ev
import recipeimp.samples as samp
import recipeimp.instruments as inst


class TestMix(unittest.TestCase):
    """Tests the Mix class"""

    def setUp(self):
        self.butter = samp.Component("Butter", 50, "g")
        self.eggs = samp.Component("Egg", 2, "unit")
        self.flour = samp.Component("Flour", 120, "g")
        self.sugar = samp.Component("Sugar", 40, "g")

        self.wet_ingredients = [self.butter, self.eggs]
        # self.dry_ingredients = samp.Sample("input sample", [self.flour, self.sugar],)

        self.mixer_bowl = cont.MixerBowl("Mixer Bowl 1", "3000")
        self.mixer_bowl.append_content(self.wet_ingredients)
        self.mixer = inst.Mixer("Mixer 1")
        self.mix_event = ev.Mix(self.mixer_bowl, self.mixer, "result sample")

    def test_run_1(self):
        """Tests the run method of the Mix class with only components as input"""

        # Check that event status is "Initiated"
        self.assertEqual(self.mix_event.status, "Instantiated")

        self.mix_event.run()

        # Check that there is one sample in the mixer bowl
        self.assertEqual(len(self.mixer_bowl.get_content()), 1)
        self.assertIsInstance(self.mixer_bowl.get_content()[0], samp.Sample)

        # Check that the content of result sample is as expected
        result_sample = self.mixer_bowl.get_content()[0]  # sample
        result_sample_components = result_sample.get_components()
        self.assertEqual(result_sample_components, [self.butter, self.eggs])

        # Check that event status is "Completed"
        self.assertEqual(self.mix_event.status, "Completed")

    # def test_run_2(self):
    #     """Tests the run method of the Mix class with samples and components as input"""
