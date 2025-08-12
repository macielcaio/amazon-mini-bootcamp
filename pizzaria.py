from hr_pizarria import Profiles

profiles = Profiles()

def flavors(choice: int):
    mapping = {
        1: profiles.italian,
        2: profiles.romanian,
        3: profiles.mexican,
        4: profiles.american,
    }
    fn = mapping.get(choice)
    if fn is None:
        return "Invalid choice"
    return fn()

def choices():
    menu = {
            1: "Italian",
            2: "Romanian",
            3: "Mexican",
            4: "American"
            }

    for numb, type in menu.items(): # print all items from the dictionary with the method ".items()"
        print(f"{numb}: {type}")
    return menu

"""
 if __name__ == "__main__":
    choices()          # show menu.
    picked = flavors(3)  # take the type of cuisine.
    print("\nSelected profile:")
    print(picked)      # show the cuisine selected
"""