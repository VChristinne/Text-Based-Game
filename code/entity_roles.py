class EntityRoles:
    def __init__(self, is_melee, is_ranged, is_magic, is_tank):
        self.is_melee = is_melee
        self.is_ranged = is_ranged
        self.is_magic = is_magic
        self.is_tank = is_tank

    ### Attack Type ###
    def get_is_melee(self):
        return self.is_melee

    def get_is_ranged(self):
        return self.is_ranged

    def get_is_magic(self):
        return self.is_magic

    def get_is_tank(self):
        return self.is_tank
