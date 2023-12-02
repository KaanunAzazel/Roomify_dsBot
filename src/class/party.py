class Party:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f"{member} joined {self.name}!")


    def display_members(self):
        print(f"Members of {self.name}:")
        for member in self.members:
            print(member)