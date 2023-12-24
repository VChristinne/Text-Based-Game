class EntityRoles:
    def __init__(self, attack_speed, is_melee, is_ranged, is_magic, is_healer, is_tank, is_dps):
        self.roles = []
        self.attack_speed = attack_speed
        self.is_melee = is_melee
        self.is_ranged = is_ranged
        self.is_magic = is_magic
        self.is_healer = is_healer
        self.is_tank = is_tank
        self.is_dps = is_dps

    ### Roles ###
    def add_role(self, role):
        self.roles.append(role)

    def remove_role(self, role):
        self.roles.remove(role)

    def has_role(self, role):
        return role in self.roles

    def has_roles(self, roles):
        return set(roles).issubset(set(self.roles))

    def get_roles(self):
        return self.roles

    def clear_roles(self):
        self.roles = []

    def __str__(self):
        return str(self.roles)

    def __repr__(self):
        return str(self.roles)

    ### Attack Speed ###
    def get_attack_speed(self):
        return self.attack_speed

    ### Attack Type ###
    def get_is_melee(self):
        return self.is_melee

    def get_is_ranged(self):
        return self.is_ranged

    def get_is_magic(self):
        return self.is_magic

    ### Role Type ###
    def get_is_dps(self):
        return self.is_dps

    def get_is_healer(self):
        return self.is_healer

    def get_is_tank(self):
        return self.is_tank
