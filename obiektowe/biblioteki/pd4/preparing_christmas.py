
def main(naughty_kids, brav_kids, elves, elfs_on_L4):
    pass


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

    def time_of_work_naughty(self):
        presents_for_naughty = self.presents_for_naughty()
        time_in_minutes = (30 * presents_for_naughty) / self._working_elves
        # time_in_hours_brav = presents_for_naughty / working_elves * 2
        return max(time_in_minutes, 30)

    def time_of_work_brav(self):
        presents_for_brav = self.presents_for_brav()
        time_in_minutes = presents_for_brav / (self._working_elves // 2) * 60
        return max(time_in_minutes, 60)

    # def count_total_time(self):
    #     # first delegate elves for brav kids
    #     # see if there are any elves left
    #     # total_time_in_min = 0
    #     if self._working_elves % 2 == 0:
    #         total_time_in_minutes = self.time_of_work_brav() + self.time_of_work_naughty()
    # #     # return total_time_in_minutes

    # def time_for_naughty(self, elves):
    #     time = (30 * self.presents_for_naughty()) / elves
    #     return max(30, time)

    # def time_for_brav(self, presents, elves):
    #     time = presents / (elves // 2) * 60
    #     return max(60, time)

    # def total_time(self):
    #     if self._working_elves % 2 == 1:
    #         time_for_brav = self.time_of_work_brav()
    #         if time_for_brav() >= self.time_for_naughty(1):




print(read_from_file('naughty_kids.txt'))
print(read_from_file('brav_kids.txt'))


if __name__ == '__main__':
    pass
