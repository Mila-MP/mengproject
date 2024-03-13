"""Tests for the events module"""

import unittest
import recipeimp.containers as cont
import recipeimp.events as ev
import recipeimp.samples as samp
import recipeimp.instruments as inst


class TestMix(unittest.TestCase):
    """Tests the Mix class."""

    def setUp(self):

        # Components
        self.butter = samp.Component("Butter", 50, "g")
        self.eggs = samp.Component("Egg", 2, "unit")
        self.flour = samp.Component("Flour", 120, "g")
        self.sugar = samp.Component("Sugar", 40, "g")
        self.wet_ingredients = [self.butter, self.eggs]

        self.mixer = inst.Mixer("Mixer")

    def test_run_1(self):
        """Tests the run method of the Mix class with only components as input."""
        mixer_bowl1 = cont.MixerBowl("Mixer Bowl 1", 3000)
        mixer_bowl1.append_content(self.wet_ingredients)
        mix_event = ev.Mix(mixer_bowl1, self.mixer, "result sample")

        # Check that event status is "Instantiated"
        self.assertEqual(mix_event.status, "Instantiated")

        mix_event.run()

        # Check that there is one sample in the mixer bowl
        self.assertEqual(len(mixer_bowl1.get_content()), 1)
        self.assertIsInstance(mixer_bowl1.get_content()[0], samp.Sample)

        # Check that the content of result sample is as expected
        result_sample = mixer_bowl1.get_content()[0]  # sample
        result_sample_components = result_sample.get_components()
        self.assertEqual(result_sample_components, [self.butter, self.eggs])

        # Check that event status is "Completed"
        self.assertEqual(mix_event.status, "Completed")

    def test_run_2(self):
        """Tests the run method of the Mix class with samples and
        components as input.
        """

        mixer_bowl = cont.MixerBowl("Mixer Bowl", 1000)
        samp.Sample(
            "dry ingredient sample", [self.flour, self.sugar], mixer_bowl, False
        )
        mixer_bowl.append_content(self.wet_ingredients)
        mix_event = ev.Mix(mixer_bowl, self.mixer, "result sample")

        # Check that event status is "Instantiated"
        self.assertEqual(mix_event.status, "Instantiated")

        mix_event.run()

        # Check that there is one sample in the mixer bowl
        self.assertEqual(len(mixer_bowl.get_content()), 1)
        self.assertIsInstance(mixer_bowl.get_content()[0], samp.Sample)

        # Check that the content of result sample is as expected
        result_sample = mixer_bowl.get_content()[0]  # sample
        result_sample_components = result_sample.get_components()
        self.assertEqual(
            result_sample_components, [self.flour, self.sugar, self.butter, self.eggs]
        )


class TestTransfer(unittest.TestCase):
    """Tests the Transfer class."""

    def test_run(self):
        """Tests the run method of the Transfer class."""
        butter = samp.Component("Butter", 50, "g")
        eggs = samp.Component("Egg", 2, "unit")
        original_container = cont.MixerBowl("original container", 500)
        recipient_container = cont.MixerBowl("recipient container", 500)
        test_sample = samp.Sample(
            "test sample", [butter, eggs], original_container, False
        )
        transfer = ev.Transfer(original_container, recipient_container)

        transfer.run()
        # Check that original container is now empty
        self.assertEqual(original_container.get_content(), [])
        # Check that recipient container contains the sample
        self.assertEqual(recipient_container.get_content(), [test_sample])
        # Check that the container of the sample is the recipient
        self.assertEqual(test_sample.container, recipient_container)
