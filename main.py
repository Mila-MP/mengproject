from data_model import samples as samp
from data_model import containers as cont
from data_model import instruments as inst
from data_model import actions


def main():

    ## Instantiating container, instrument, and ingredients
    bowl1 = cont.Bowl("Bowl 1", 500)
    mixer1 = inst.Mixer("Mixer 1", max_speed=15)
    flour = samp.Component("Flour", 100, "g")
    sugar = samp.Component("Sugar", 80, "g")
    butter = samp.Component("Butter", 85, "g")
    dry_ingredients = [flour, sugar]

    ## Adding dry ingredient to bowl
    bowl1.append_content(dry_ingredients)

    print("Content of bowl 1 before running step 1:")
    print(bowl1.get_content())  # Individual dry ingredients
    print(100 * "=")

    # Mix dry ingredients
    mix1 = actions.Mix(bowl1, mixer1, "Dry ingredients mix")
    mix1.run()

    print("Content of bowl 1 after running step 1:")
    print(bowl1.get_content())  # Dry ingredients sample
    print(f"The name of the sample is: {bowl1.get_content()[0].name}")
    print(100 * "=")

    # Add butter to bowl
    bowl1.append_content(butter)

    print("Content of bowl 1 before running step 2:")
    print(bowl1.get_content())  # Dry ingredients sample and butter component
    print(100 * "=")

    # Mix to make dough
    mix2 = actions.Mix(bowl1, mixer1, "Dough")
    mix2.run()

    print("Content of Mixer bowl 1 after running step 2:")
    print(bowl1.get_content())  # Contains Step 2 sample
    print(f"The name of the sample is: {bowl1.get_content()[0].name}")
    print(100 * "=")


if __name__ == "__main__":
    main()
