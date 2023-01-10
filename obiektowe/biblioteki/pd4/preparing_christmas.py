import math
import argparse
import sys


def main(arguments):
    args = parser(arguments)
    file_naughty_kids = args.NAUGHTY_KIDS
    file_polite_kids = args.POLITE_KIDS
    all_elves = args.ALL_ELVES
    elves_on_elf4 = args.ELVES_ON_eLf4

    amount_of_sticks = len(read_from_file(file_naughty_kids))
    amount_of_presents = len(read_from_file(file_polite_kids))
    file_naughty_kids.close()
    file_polite_kids.close()

    village = Village(amount_of_sticks, amount_of_presents, all_elves, elves_on_elf4)
    time = village.count_total_time()
    f_time = FormatTime(time)
    print_results(amount_of_presents, amount_of_sticks, f_time)


def print_results(presents, sticks, time):
    print('Raport for St Claus village:')
    print(f'There are {presents} presents and {sticks} sticks to produce')
    print(f'The elves need {time} to produce it')


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
    kids = []
    for line in file_handle:
        if line:
            kids.append(line)
    return kids


class Village:
    def __init__(self, am_sticks, am_presents, elves, elves_on_elf4=0):
        if elves < 0 or elves_on_elf4 < 0:
            raise ValueError('elves number cannot be negative')
        self._elves = elves
        self._elves_on_l4 = elves_on_elf4
        self._working_elves = elves - elves_on_elf4
        if self._working_elves == 1 and am_presents > 0:
            raise ValueError('one elf cannot produce presents')
        if self._working_elves < 0:
            raise ValueError('there cannot be more elf4 than all elves')
        self._am_sticks = am_sticks
        self._am_presents = am_presents

    def count_total_time_odd(self):
        '''
        counts the number of time needed to make presents when
        the number of elves is odd
        '''
        time_presents = self.time_for_presents(self._am_presents, self._working_elves)
        sticks_simul = time_presents * 2 + 2 * self.free_elves(self._am_presents, self._working_elves - 1)
        sticks_left = max(0, self._am_sticks - sticks_simul)
        time_sticks = self.time_for_sticks(sticks_left, self._working_elves)
        return time_presents + time_sticks

    def count_total_time_even(self):
        '''
        counts the number of time needed to make presents when
        the number of elves is even
        '''
        time_presents = self.time_for_presents(self._am_presents, self._working_elves)
        sticks_simul = 2 * self.free_elves(self._am_presents, self._working_elves)
        left_n = max(0, self._am_sticks - sticks_simul)
        naughty_left = self.time_for_sticks(left_n, self._working_elves)
        return time_presents + naughty_left

    def count_total_time(self):
        '''
        counts total time
        '''
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
        if fractorial == 0:
            return time
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
        last_hour_working_pairs = presents % (elves // 2)
        if elves % 2 == 1:
            free_elves = elves - last_hour_working_pairs * 2 - 1
        if elves % 2 == 0:
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
        elves = elves
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
        return int(self.time) // 24

    def hours(self):
        return int(self.time) % 24

    def minutes(self):
        minutes = (self.time - int(self.time)) * 60
        return int(minutes)

    def __str__(self):
        """
        returns the str representation: how many days, minutes and hours
        (even if one of the numbers is 0)
        """
        if self.hours() == 1 and self.days() == 1:
            return f'{self.days()} day, {self.hours()} hour and {self.minutes()} minutes'
        if self.days() == 1:
            return f'{self.days()} day, {self.hours()} hours and {self.minutes()} minutes'
        if self.hours() == 1:
            return f'{self.days()} days, {self.hours()} hour and {self.minutes()} minutes'
        else:
            return f'{self.days()} days, {self.hours()} hours and {self.minutes()} minutes'


if __name__ == "__main__":
    main(sys.argv)