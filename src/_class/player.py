class Player:
    def __init__(self, name, dsID, character_class, level=1, attackDamage=1, abilityPower=1, health=100, mana=10):
        self.nome = name
        self.discordID = dsID
        self.idParty = None
        self.character_class = character_class
        self.level = level
        self.attackDamage = attackDamage
        self.abilityPower = abilityPower
        self.health = health
        self.mana = mana

    def __str__(self):
        return f"{self.name} ({self.character_class} - Level {self.level})"

    def attack(self, target):
        print(f"{self.name} attacks {target}!")
