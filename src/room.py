# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    # Construct a Room object instance
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return "Name: {name}\nDescription: {description}\n----\nn_to: {nto}\ns_to: {sto}\ne_to: {eto}\nw_to: {wto}\n".format(
            name=self.name,
            description=self.description,
            nto=self.n_to,
            sto=self.s_to,
            eto=self.e_to,
            wto=self.w_to)
