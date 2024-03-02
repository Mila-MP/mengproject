import recipeimp.containers as cont
import recipeimp.events as ev
import recipeimp.samples as samp


def main():
    mixer_bowl = cont.MixerBowl("Mixer bowl", 500)
    component1 = samp.Components("water", 250, "mL")
    component2 = samp.Components("salt", 2, "g")
    comp = [component1, component2]
    mixer_bowl.content = comp
    print(mixer_bowl.content)


if __name__ == "__main__":
    main()
