from random import randint


class EmptyNameError(Exception):
    pass


class Casino:
    def __init__(self, list_of_players=None):
        '''class Casino. contains attribute:
        :param representation: list_of_players
        :param type: list
        '''
        if not list_of_players:
            list_of_players = []
        self.list_of_players = list_of_players

    def add_player(self, new_player):
        '''
        adds player to the game
        '''
        self.list_of_players.append(new_player)
        return self.list_of_players

    def remove_player(self, old_player):
        '''
        removes player from the game
        '''
        if old_player not in self.list_of_players:
            raise ValueError('chosen player is not on the list')
        self.list_of_players.remove(old_player)
        return self.list_of_players

    def throw_dice(self):
        '''
        returns the list of 4 numbers- dices
        '''
        dices = []
        for number in range(1, 5):
            dices.append(randint(1, 6))
        return dices

    def game(self):
        '''
        each player gets his result,
        returns list of tuples: (player, his result)
        '''
        results = []
        for player in self.list_of_players:
            player.dices = self.throw_dice()
            pair = player.name, player.result
            results.append(pair)
        return results

    def result_of_game(self):
        '''
        returns the winner of the game, or info that there is draw
        '''
        results = self.game()
        sorted_results = sorted(results, key=lambda results: results[1], reverse=True)
        winner, winning_score = sorted_results[0]
        runner_up, second_score = sorted_results[1]
        if winning_score == second_score:
            return 'the game is unresolved'
        else:
            return f'{winner} won'


class Player:
    '''
    Class Player. Contains attributes:
    :param name: name
    :param type: str
    :param name: dices
    :param type: list
    :param name: result
    :param type: int
    '''
    def __init__(self, name, dices=None, result=0):
        if not name:
            raise EmptyNameError('name cannot be empty')
        if not dices:
            dices = []
        self.name = name
        self.dices = dices
        self._result = result

    def __eq__(self, other: 'Player') -> 'bool':
        return self.name == other.name

    @property
    def result(self):
        '''
        gets the player's result, based on his dices
        '''
        possible_results = []
        [a, b, c, d] = sorted(self.dices, reverse=True)
        if a == b == c == d:
            result_1 = a * 6
            possible_results.append(result_1)
        if (a * b * c * d) % 2 == 1:
            result_2 = sum(self.dices) + 3
            possible_results.append(result_2)
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
            result_3 = sum(self.dices) + 2
            possible_results.append(result_3)
        if a == b == c or b == c == d:
            result_4 = b * 4
            possible_results.append(result_4)
        if a == b or b == c:
            # pair is either a, b or b, c so in both cases result is, b * 2
            result_5 = b * 2
            possible_results.append(result_5)
        if c == d:
            result_6 = c * 2
            possible_results.append(result_6)
        else:
            result_7 = max(self.dices)
            possible_results.append(result_7)
            # if there is nothing, the result equals to the max number on dices
        self._result = max(possible_results)
        return self._result
