import random
import time

class Robot:
    def __init__(self, name, hp, attack, energy, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.accuracy = random.uniform(0.7, 1.0)
        self.energy = energy
        self.max_energy = energy
        self.defense = defense

        self.stuned = 0
        self.crictical = 0
        self.silenced = 0

    def attack_enemy(self, enemy):
        if self.stuned > 0:
            print(self.name + "Terkena stuned")
            self.stuned -= 1
            return False
        
        if random.random() <= self.accuracy:
            damage = self.attack
            if self.crictical > 0:
                damage *= 2
                print(f"{self.name} melakukan critical hit!!")
                self.crictical -= 1
            reduced_damage = max(1, damage - enemy.defense)
            enemy.hp = max(0, enemy.hp - reduced_damage)
            print(f"{self.name} menyerang {enemy.name} memberikan damage {reduced_damage}")
            self.gain_energy(5)
            return True

        else:
            print(f"{self.name} meleset")
            return False

    def use_skill(self, skill_name, enemy):
        if self.silenced > 0:
            print(f"{self.name} terkena silence")
            self.silenced -= 1
            return False

        if self.stuned > 0:
            print(self.name + "Terkena stuned")
            self.stuned -= 1
            return False

        if self.energy < 20:
            print(f"{self.name} tidak memiliki cukup energi!!")
            return False

        elif skill_name == "stun" and random.random() < 0.8:
            self.energy -= 25
            enemy.stuned = random.randint(1, 3)
            print(f"{self.name} menggunakan stun!, {enemy.name} terkena stuned selam {enemy.stuned} ronde")

        elif skill_name == "critical" and random.random() <  0.6:
            self.energy -= 15
            self.crictical = 2

        elif skill_name == "silence" and random.random() < 0.7:
            self.energy -= 10
            enemy.silenced = random.randint(1, 3)
            print(f"{self.name} menggunakan silence!, {enemy.name} terkena silence selama {enemy.silenced} ronde")
        self.gain_energy(random.randint(5, 10))
        return True

    def regen_health(self):
        if self.energy >= 10:
            self.energy -= 10
            heal = random.randint(10, 20)
            self.hp = min(self.max_hp, self.hp + heal)
            print(f"{self.name} mengisi darah sebesar {heal}")

    def gain_energy(self, energy):
        self.energy = min(self.max_energy, self.energy + energy)
        
    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1
        self.action_log = []

    def play_round(self, robot, enemy):
        print(f"\nGiliran {robot.name} (HP: {robot.hp}. energy: {robot.energy})")

        if random.random() <= 0.4 and robot.energy >= 25:
            skill = random.choice(["stun", "critical", "silence"])
            robot.use_skill(skill, enemy)
            self.action_log.append(f"{robot.name} menggunakan skill {skill}")
            
        elif random.random() <= 0.5 and robot.energy >= 10:
            robot.regen_health()
            self.action_log.append(f"{robot.name} mengisi darah")

        else:
            robot.attack_enemy(enemy)
            self.action_log.append(f"{robot.name} menyerang {enemy.name}")
    

    def start(self):
        print("=" * 5 + "Game Dimulai" + "=" * 5)
        print(f"{self.robot1.name} HP: {self.robot1.hp} vs {self.robot2.name} HP: {self.robot2.hp}")

        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound {self.round}")

            self.play_round(self.robot1, self.robot2)
            if not self.robot2.is_alive():
                print(f"{self.robot2.name} telah dikalahkan!!")
                print(f"{self.robot1.name} menang!!")
                break

            self.play_round(self.robot2, self.robot1)
            if not self.robot1.is_alive():
                print(f"{self.robot1.name} telah dikalahkan!!")
                print(f"{self.robot2.name} menang!!")
                break

            print(f"status: {self.robot1.name} HP: {self.robot1.hp} energy: {self.robot1.energy} |" f"{self.robot2.name} HP: {self.robot2.hp} energy: {self.robot2.energy}")

            self.round += 1
            time.sleep(1)
        print("=" * 5 + "Game Berakhir" + "=" * 5)

if __name__ == "__main__":
    robot1 = Robot(name="Optimus Prime", hp=100, attack=30, energy=100, defense=10)
    robot2 = Robot(name="Bumblebee", hp=80, attack=35, energy=80, defense=5)

    game = Game(robot1, robot2)
    game.start()