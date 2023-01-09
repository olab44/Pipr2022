import math
import argparse
import sys


def main(arguments):
    parser = argparse.ArgumentParser()


def read_from_file(file_handle):
    with open(file_handle, 'r') as file_handle:
        kids = []
        for line in file_handle:
            kids.append(line)
        return kids


class Factory:
    def __init__(self, file_naughty_kids, file_brav_kids, elves, elves_on_l4=0):
        self._elves = elves
        self._elves_on_l4 = elves_on_l4
        self._working_elves = int(elves - elves_on_l4)
        self._file_naughty_kids = file_naughty_kids
        self._file_brav_kids = file_brav_kids

    def presents_for_naughty(self):
        return len(read_from_file(self._file_naughty_kids))

    def presents_for_brav(self):
        return len(read_from_file(self._file_brav_kids))

    def total_presents(self):
        return self.presents_for_brav() + self.presents_for_naughty()

    def count_total_time_odd(self):
        if self._working_elves % 2 == 1:
            to_do_p = self.presents_for_brav()
            to_do_r = self.presents_for_naughty()
            presents = self.time_for_brav(to_do_p, self._working_elves)
            naughty_simul = presents * 2 + 2 * self.free_elves(to_do_p, self._working_elves - 1)
            left_n = max(0, to_do_r - naughty_simul)
            naughty_left = self.time_for_naughty(left_n, self._working_elves)
        return presents + naughty_left

    def count_total_time_even(self):
        if self._working_elves % 2 == 0:
            to_do_p = self.presents_for_brav()
            to_do_r = self.presents_for_naughty()
            presents = self.time_for_brav(to_do_p, self._working_elves)
            naughty_simul = 2 * self.free_elves(to_do_p, self._working_elves - 1)
            left_n = max(0, to_do_r - naughty_simul)
            naughty_left = self.time_for_naughty(left_n, self._working_elves)
            return presents + naughty_left

    def rounding_time(self, time):
        fractorial = time - int(time)
        if fractorial <= 0.5:
            time = int(time) + 0.5
        if fractorial > 0.5:
            time = math.ceil(time)
        return time

    def free_elves(self, presents, elves):
        '''
        sometimes only some of the elves are working during last hour (when making presents only),
        here we count how many elves do not work, arguments are only even numbers (elves)
        '''
        last_hour_working_pairs = presents % int(elves * 0.5)
        if elves % 2 == 1:
            free_elves = elves - last_hour_working_pairs * 2 - 1
        else:
            free_elves = elves - last_hour_working_pairs * 2
        return free_elves

    def time_for_naughty(self, presents, elves):
        if presents == 0:
            return 0
        time = (0.5 * presents) / elves
        rounded_time = self.rounding_time(time)
        return max(0.5, rounded_time)

    def time_for_brav(self, presents, elves):
        if presents == 0:
            return 0
        time = math.ceil(presents / (elves // 2))
        return max(1, time)



# def main(arguments):
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--list-stations', nargs='?', const=' ')
#     parser.add_argument('--list-sensors'


# print(read_from_file('naughty_kids.txt'))
# print(read_from_file('brav_kids.txt'))


if __name__ == '__main__':
    main(sys.argv)
