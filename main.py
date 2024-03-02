import recipeimp.containers as cont
import recipeimp.events as ev
import recipeimp.sample as samp


def main():
    bowl = cont.Container("Bowl", 500)
    component1 = samp.Components("water", 250, "mL")
    component2 = samp.Components("salt", 2, "g")
    comp = [component1, component2]
    event1 = ev.MakeSample("make sample", bowl, comp)
    event1.run()
    print(bowl.content)
    print(event1.status)


if __name__ == "__main__":
    main()
