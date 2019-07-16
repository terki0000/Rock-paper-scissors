import random
moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.score = 0
        self.mm = Player.move(self)
        self.cm = Player.move(self)

    def move(self):
            return moves[0]

    def learn(self, mm, cm):
            self.mm = mm
            self.cm = cm


class Randomizer(Player):
    def move(self):
        return random.choice(moves)


class Human(Player):
    def move(self):
        try:
            usermove = input("Please type rock or paper or scissors")
            while usermove not in moves:
                print("rong, Please try again")
                usermove = input("Please type rock or paper or scissors")
        except KeyboardInterrupt:
                        print('Thanks for playing.')
                        exit()
        return usermove


class Reflector(Player):
    def move(self):
        return self.cm


class Cycler(Player):
    def move(self):
        if self.mm is moves[0]:
            self.mm = moves[1]
        elif self.mm is moves[1]:
            self.mm = moves[2]
        elif self.mm is moves[2]:
            self.mm = moves[0]
        return self.mm


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Repeater(Player):
    def move(self):
        return moves[0]


class Game:
    def __init__(self, p1, p2):
        self.score = 0
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print (f"Player 1: {move1} Player 2: {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print('Player 1 win!')
        elif beats(move2, move1):
            self.p2.score += 1
            print('Player 2 win!')
        else:
            print("tie, tie, tie.")
        print(f"""Score:
        Player 1 | Player 2
           {self.p1.score}          {self.p2.score}""")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("match start!")
        for round in range(1, 6):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print(f"""Player 1 (human Won!)
            Final score:Player 1: {self.p1.score} | Player 2 {self.p2.score}
            Game Over.""")
        elif self.p2.score > self.p1.score:
            print(f"""Player 2 (computer won!)
            Final Score: Player 1: {self.p1.score} | Player 2 {self.p2.score}
            Game Over.""")
        else:
            print(f"""tie, tie, tie.
            Final Score: Player1 = {self.p1.score} | Player2= {self.p2.score}
            Game Over""")


def start_game():
    if __name__ == '__main__':
        print('Welcome to RPS.')
        while True:
            try:
                playerlist = int(input("enter random(1),cycler(2)\
                repeater(3),reflector(4),(0) to quit"))
                if playerlist == 4:
                    game = Game(Human(), Reflector())
                    game.play_game()
                    break
                if playerlist == 1:
                    game = Game(Human(), Randomizer())
                    game.play_game()
                    break
                if playerlist == 2:
                    game = Game(Human(), Cycler())
                    game.play_game()
                    break
                if playerlist == 3:
                    game = Game(Human(), Repeater())
                    game.play_game()
                    break
                if playerlist == 0:
                    print('Goodbye.')
                    exit()
                    game.play_game()
                    break
            except ValueError:
                print('Envalid number. Please try again.')
                continue
            except KeyboardInterrupt:
                print('Thanks for playing.')
                exit()
start_game()
