import numpy as np
"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].
Snake snake = new Snake(width, height, food);
Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)"""
class SnakeGame(object):

    def placeFood(self):
        if len(self.food_sequence) > 0:

            position = self.food_sequence.pop(0)
            if position[0] >=0 and position[0]< len(self.board) and position[1] >=0 and position[1] < len(self.board[0]):
                self.board[position[0]][position[1]] = 1

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.board = np.zeros(( height, width), dtype=int)
        self.food_sequence = food
        self.snake_body = list()
        self.game_score = 0
        self.snake_body.append([0, 0])
        self.snake_head_poisiton = [0,0]
        self.placeFood()

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction == "U":
            new_position = [self.snake_head_poisiton[0] - 1, self.snake_head_poisiton[1]]
            if new_position[0] >=0 :
                last_position = self.snake_body.pop(-1)
                if new_position not in self.snake_body:
                    self.snake_head_poisiton = new_position
                    self.snake_body.insert(0, new_position)
                    if self.board[new_position[0]][new_position[1]] == 1:
                        self.board[new_position[0]][new_position[1]] = 0
                        self.game_score += 1
                        self.placeFood()
                        self.snake_body.append(last_position)
                    return self.game_score
            self.game_score = 0
            return -1
        elif direction == "D":
            new_position = [self.snake_head_poisiton[0] + 1, self.snake_head_poisiton[1]]
            if new_position[0] < len(self.board):
                last_position = self.snake_body.pop(-1)
                if new_position not in self.snake_body:
                    self.snake_head_poisiton = new_position
                    self.snake_body.insert(0, new_position)
                    if self.board[new_position[0]][new_position[1]] == 1:
                        self.board[new_position[0]][new_position[1]] = 0
                        self.game_score += 1
                        self.placeFood()
                        self.snake_body.append(last_position)
                    return self.game_score
            self.game_score = 0
            return -1
        elif direction == "L":
            new_position = [self.snake_head_poisiton[0] , self.snake_head_poisiton[1] - 1]
            if new_position[1] >= 0 :
                last_position = self.snake_body.pop(-1)
                if new_position not in self.snake_body:
                    self.snake_head_poisiton = new_position
                    self.snake_body.insert(0, new_position)
                    if self.board[new_position[0]][new_position[1]] == 1:
                        self.board[new_position[0]][new_position[1]] = 0
                        self.game_score += 1
                        self.placeFood()
                        self.snake_body.append(last_position)
                    return self.game_score
            self.game_score = 0
            return -1
        elif direction == "R":
            new_position = [self.snake_head_poisiton[0] , self.snake_head_poisiton[1] + 1]
            if new_position[1] < len(self.board[0]) :
                last_position = self.snake_body.pop(-1)
                if new_position not in self.snake_body:
                    self.snake_head_poisiton = new_position
                    self.snake_body.insert(0, new_position)
                    if self.board[new_position[0]][new_position[1]] == 1:
                        self.board[new_position[0]][new_position[1]] = 0
                        self.game_score += 1
                        self.placeFood()
                        self.snake_body.append(last_position)
                    return self.game_score
            self.game_score = 0
            return -1




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# # param_1 = obj.move(direction)
obj = SnakeGame(100,30,[[11,0],[58,7]])
# obj = SnakeGame(1,3,[[1,0],[2,0]])
# print obj.move("D"),
# print obj.move("D"),
# print obj.move("D")
# # # [[011]]
# # #  [011]
# # #  [00*]
# obj = SnakeGame(3,3, [[2,0],[0,0],[0,2],[2,2]])
# print obj.move("D"),
# print obj.move("D"),
# print obj.move("R"),
# print obj.move("U"),
# print obj.move("U"),
# print obj.move("L"),
# print obj.move("D"),
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("U"),
# print obj.move("L"),
# print obj.move("D")
# # # [null,0,1,1,1,1,2,2,2,2,3,3,3]
# obj =SnakeGame(3,3,[[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]])
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("D"),
# print obj.move("D"),
# print obj.move("L"),
# print obj.move("L"),
# print obj.move("U"),
# print obj.move("U"),
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("D"),
# print obj.move("D"),
# print obj.move("L"),
# print obj.move("L"),
# print obj.move("U"),
# print obj.move("R"),
# print obj.move("U"),
# print obj.move("L"),
# print obj.move("D")
# #[null,1,2,3,4,5,6,7,7,7,7,7,7,7,7,7,7,7,7,-1]
#
#
# obj = SnakeGame(10000,10000,[[0,1],[0,2],[0,3],[0,4],[1,4],[2,4],[2,3],[2,2],[2,1],[2,0],[1,0]])
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("D"),
# print obj.move("D"),
# print obj.move("L"),
# print obj.move("L"),
# print obj.move("L"),
# print obj.move("L"),
# print obj.move("U"),
# print obj.move("U"),
# print obj.move("U"),
# print obj.move("D"),
# print obj.move("L"),
# print obj.move("U"),
# print obj.move("R"),
# print obj.move("R"),
# print obj.move("D"),
# print obj.move("D"),
# print obj.move("R"),
# print obj.move("U"),
# print obj.move("L"),
# print obj.move("U")
