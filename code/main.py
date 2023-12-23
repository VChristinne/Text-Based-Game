import attributes


def main():
    atb01 = attributes.Attributes(100, 100, 100, 100, 100, 100, 100, 100)
    status(atb01)


def status(atb):
    print("Health: " + str(atb.get_health()) + "/" + str(atb.get_max_health()))
    print("Shield: " + str(atb.get_shield()) + "/" + str(atb.get_max_shield()))
    print("Stamina: " + str(atb.get_stamina()) + "/" + str(atb.get_max_stamina()))
    print("Mana: " + str(atb.get_mana()) + "/" + str(atb.get_max_mana()))


if __name__ == '__main__':
    main()
