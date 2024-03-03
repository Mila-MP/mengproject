import recipeimp.containers as cont
import recipeimp.events as ev
import recipeimp.samples as samp
import recipeimp.instruments as inst


def main():
    # Instantiating container, instrument, and ingredients
    mixer_bowl1 = cont.MixerBowl("Mixer bowl 1", 500)
    mixer1 = inst.Mixer("Mixer 1")
    banana = samp.Component("Banana", 1, "unit")
    berries = samp.Component("Berries", 50, "g")
    orange_juice = samp.Component("Orange juice", 50, "mL")
    honey = samp.Component("Honey", 10, "g")
    comp_step1 = [banana, berries, orange_juice]

    # Step 1: Mix banana, berries, and orange juice to obtain Step 1 sample
    mixer_bowl1.content = (
        comp_step1  # Add banana, berries, and orange juice to mixer bowl
    )
    print("Content of Mixer bowl 1 before running step 1:")
    print(mixer_bowl1.content)  # Contains individual components

    step1 = ev.Mix(mixer_bowl1, mixer1, "Step 1 sample")
    step1.run()  # Mix the ingredients to obtain Step 1 sample
    print("Content of Mixer bowl 1 after running step 1:")
    print(mixer_bowl1.content)  # Contains Step 1 sample

    # Step 2: Add honey and mix again to obtain Step 2 sample
    mixer_bowl1.content.append(honey)  # Add honey to mixer bowl
    print("Content of Mixer bowl 1 before running step 2:")
    print(mixer_bowl1.content)  # Contains Step 1 sample and honey component

    step2 = ev.Mix(mixer_bowl1, mixer1, "Step 2 sample")
    step2.run()  # Mix the ingredients to obtain step 2 sample
    print("Content of Mixer bowl 1 after running step 2:")
    print(mixer_bowl1.content)  # Contains Step 2 sample


if __name__ == "__main__":
    main()
