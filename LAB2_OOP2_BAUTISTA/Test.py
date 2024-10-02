import random
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Novice import Novice
from Boss import Boss

class Game:
    def __init__(self):
        self.player_wins = 0
        self.boss_wins = 0
        self.pvp_wins = [0, 0]

    def select_mode(self):
        print("Select Game Mode:")
        print("1. Single Player Mode")
        print("2. Player vs Player Mode")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            self.single_player_mode()
        elif choice == "2":
            self.player_vs_player_mode()
        else:
            print("Invalid choice. Please select again.")
            self.select_mode()

    def single_player_mode(self):
        print("\n--- Single Player Mode ---")
        player = Novice(input("Enter your username: "))
        boss = Boss("Monster")

        wins = 0
        while True:
            print(f"\nMatch {wins + 1}: {player.getUsername()} (HP: {player.getHp()}) vs {boss.getUsername()} (HP: {boss.getHp()})")
            winner = self.start_match(player, boss)

            if winner == player.getUsername():
                wins += 1
                print(f"{player.getUsername()} won the match!")
                if wins == 2:
                    print("\nCongratulations! You can now select an advanced class.")
                    player = self.select_class_upgrade(player.getUsername())
            else:
                print(f"{boss.getUsername()} won the match!")
                break

    def player_vs_player_mode(self):
        print("\n--- Player vs Player Mode ---")
        player1 = self.select_class(input("Player 1, enter your username: "))
        player2 = self.select_class(input("Player 2, enter your username: "))

        while True:
            print(f"\n{player1.getUsername()} (HP: {player1.getHp()}) vs {player2.getUsername()} (HP: {player2.getHp()})")
            winner = self.start_match(player1, player2)

            if winner == player1.getUsername():
                self.pvp_wins[0] += 1
                print(f"{player1.getUsername()} won the match!")
            else:
                self.pvp_wins[1] += 1
                print(f"{player2.getUsername()} won the match!")

            cont = input("Do you want to play another match? (yes/no): ").strip().lower()
            if cont != 'yes':
                print(f"Player 1 Wins: {self.pvp_wins[0]}, Player 2 Wins: {self.pvp_wins[1]}")
                break

    def select_class_upgrade(self, username):
        print("\nSelect a new class:")
        print("1. Swordsman")
        print("2. Archer")
        print("3. Magician")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return Swordsman(username)
        elif choice == "2":
            return Archer(username)
        elif choice == "3":
            return Magician(username)
        else:
            print("Invalid choice. Defaulting to Swordsman.")
            return Swordsman(username)

    def select_class(self, username):
        print("\nSelect a class for the player:")
        print("1. Novice")
        print("2. Swordsman")
        print("3. Archer")
        print("4. Magician")
        choice = input("Enter 1, 2, 3, or 4: ").strip()
        if choice == "1":
            return Novice(username)
        elif choice == "2":
            return Swordsman(username)
        elif choice == "3":
            return Archer(username)
        elif choice == "4":
            return Magician(username)
        else:
            print("Invalid choice. Defaulting to Novice.")
            return Novice(username)

    def start_match(self, player1, player2):
        players = [player1, player2]
        random.shuffle(players)  # Randomize turn order
        while player1.getHp() > 0 and player2.getHp() > 0:
            attacker, defender = players
            print(f"\n{attacker.getUsername()}'s turn!")

            move = input("Choose an attack: 1. Basic Attack  2. Special Attack: ").strip()
            if move == "1":
                attacker.basicAttack(defender)
            elif move == "2" and hasattr(attacker, 'slashAttack'):
                attacker.slashAttack(defender)
            elif move == "2" and hasattr(attacker, 'rangedAttack'):
                attacker.rangedAttack(defender)
            elif move == "2" and hasattr(attacker, 'magicAttack'):
                attacker.magicAttack(defender)
            else:
                print("Invalid move. Skipping turn.")

            players.reverse()

        if player1.getHp() <= 0:
            return player2.getUsername()
        else:
            return player1.getUsername()

if __name__ == "__main__":
    game = Game()
    game.select_mode()

