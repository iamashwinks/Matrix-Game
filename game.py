import random
class ConsoleGame(object):

    def __init__(self):
        self.matrix = [[random.randint(1,20) for j in range(8)] for i in range(8)]

    def run(self):
        num = int(input("Enter the the nos. between 1 to 20: "))
        for i in self.matrix:
            if num in i:
                print("You Lost! :P")
                break
            else:
                print("Yay! You won! :)")
                break
