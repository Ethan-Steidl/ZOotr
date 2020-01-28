
'''
Class representing doorways WIP
holds name of Edge the door represents
holds condition requirement for door
holds if door is currently accessible (can be derived from condition)
'''

class Door():

    def __init__(self, names, conds):
        self.name = names
        self.condition = conds
        self.accessible = False

    def get_condition():
        return self.condition

    def get_name():
        return self.name

    def __str__(self):
        res = "name: " + str(self.name) + " condition: " + str(self.condition)

        return res
