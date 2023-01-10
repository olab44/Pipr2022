import math
import argparse
import sys


def main(arguments):
    args = parser(arguments)
    file_naughty_kids = args.NAUGHTY_KIDS
    file_polite_kids = args.POLITE_KIDS
    all_elves = args.ALL_ELVES
    elves_on_elf4 = args.ELVES_ON_eLf4

    amount_of_presents = read_from_file(file_naughty_kids)
    amount_of_sticks = read_from_file(file_polite_kids)

    village = Village(amount_of_presents, amount_of_sticks, all_elves, elves_on_elf4)
    time = village.count_total_time()
    f_time = FormatTime(time)

    print_results(amount_of_presents, amount_of_sticks, f_time)
    return amount_of_presents, amount_of_sticks


def print_results(presents, sticks, time):
    print(f'there are {presents} presents and {sticks} sticks to produce')
    print(f'in total {presents + sticks} things')
    print(f'st Claus and elves need {time} to produce it')


def parser(arguments):
    '''
    parsers the arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('NAUGHTY_KIDS', type=argparse.FileType('r'))
    parser.add_argument('POLITE_KIDS', type=argparse.FileType('r'))
    parser.add_argument('ALL_ELVES', type=int)
    parser.add_argument('--ELVES_ON_eLf4', nargs='?', default=0, type=int)
    args = parser.parse_args(arguments[1:])
    return args


def read_from_file(file_handle):
    with open(file_handle) as file_handle:
        kids = []
        for line in file_handle:
            kids.append(line)
        return kids


class Village:
    def __init__(self, naughty_kids, polite_kids, elves, elves_on_elf4=0):
        self._elves = elves
        self._elves_on_l4 = elves_on_elf4
        self._working_elves = elves - elves_on_elf4
        self._naughty_kids = naughty_kids
        self._polite_kids = polite_kids

    def total_presents_sticks(self):
        return self._naughty_kids + self._polite_kids

    def count_total_time_odd(self):
        '''
        counts the number of time needed to make presents when
        the number of elves is odd
        '''
        am_presents = self._polite_kids
        am_sticks = self._naughty_kids
        time_presents = self.time_for_presents(am_presents, self._working_elves)
        sticks_simul = time_presents * 2 + 2 * self.free_elves(am_sticks, self._working_elves - 1)
        sticks_left = max(0, am_sticks - sticks_simul)
        time_sticks = self.time_for_sticks(sticks_left, self._working_elves)
        return time_presents + time_sticks

    def count_total_time_even(self):
        '''
        counts the number of time needed to make presents when
        the number of elves is even
        '''
        am_presents = self._polite_kids
        am_sticks = self._naughty_kids
        presents = self.time_for_presents(am_presents, self._working_elves)
        sticks_simul = 2 * self.free_elves(am_sticks, self._working_elves - 1)
        left_n = max(0, am_sticks - sticks_simul)
        naughty_left = self.time_for_sticks(left_n, self._working_elves)
        return presents + naughty_left

    def count_total_time(self):
        '''
        counts total time
        '''
        if self._working_elves == 1 and self._naughty_kids > 0:
            raise ValueError('one elf cannot produce presents himself')
        if self._working_elves % 2 == 1:
            return self.count_total_time_odd()
        if self._working_elves % 2 == 0:
            return self.count_total_time_even()

    def rounding_time(self, time):
        '''
        rounding time to full hours (presents' case)
        or to 30 minutes (sticks' case)
        '''
        fractorial = time - int(time)
        if fractorial <= 0.5:
            time = int(time) + 0.5
        if fractorial > 0.5:
            time = math.ceil(time)
        return time

    def free_elves(self, presents, elves):
        '''
        sometimes only some of the elves work during last hour of making gifts,
        counting how many elves do not work, during last hour
        '''
        last_hour_working_pairs = presents % int(elves * 0.5)
        if elves % 2 == 1:
            free_elves = elves - last_hour_working_pairs * 2 - 1
        else:
            free_elves = elves - last_hour_working_pairs * 2
        return free_elves

    def time_for_sticks(self, presents, elves):
        '''
        counting how much time is needed to produce sticks
        '''
        if presents == 0:
            return 0
        time = (0.5 * presents) / elves
        rounded_time = self.rounding_time(time)
        return max(0.5, rounded_time)

    def time_for_presents(self, presents, elves):
        '''
        counting how much time is needed to produce presents
        '''
        if presents == 0:
            return 0
        time = math.ceil(presents / (elves // 2))
        return max(1, time)


class FormatTime:
    '''
    class FormatTime. contains attribute:
    :param representation: time
    :param type: float
    '''
    def __init__(self, time):
        self.time = time

    def days(self):
        return self.time // 24

    def hours(self):
        return int(self.time) % 24

    def minutes(self):
        minutes = (self.time - int(self.time)) * 60
        return int(minutes)

    def __str__(self):
        return f'{self.days()} days, {self.hours()} hours, and {self.minutes()} minutes'


if __name__ == "__main__":
    # main(sys.argv)
    # print_results(3, 4, 5)
    print(read_from_file('naughty_kids.txt'))
