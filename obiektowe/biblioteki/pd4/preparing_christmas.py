
def main(naughty_kids, brav_kids, elves, elfs_on_L4):
    pass


def read_from_file(file_handle):
    with open(file_handle, 'r') as file_handle:
        kids = []
        for line in file_handle:
            kids.append(line)
        return kids


class ElvesWorking:
    def __init__(self, file_naughty_kids, file_brav_kids, elves, elves_on_l4=0):
        self._elves = elves
        self._elves_on_l4 = elves_on_l4
        self._working_elves = int(elves - elves_on_l4)
        self._file_naughty_kids = file_naughty_kids
        self._file_brav_kids = file_brav_kids

    def read_from_file(self, file_handle):
        with open(file_handle, 'r') as file_handle:
            kids = []
            for line in file_handle:
                kids.append(line)
            return kids

    def presents_for_naughty(self):
        return len(self.read_from_file(self._file_naughty_kids))

    def presents_for_brav(self):
        return len(self.read_from_file(self._file_brav_kids))

    def time_of_work_naughty(self):
        presents_for_naughty = self.presents_for_naughty()
        time_in_hours = (0.5 * presents_for_naughty) / self._working_elves
        # time_in_hours_brav = presents_for_naughty / working_elves * 2
        return max(time_in_hours, 0.5)

    def time_of_work_brav(self):
        presents_for_brav = self.presents_for_brav()
        time_in_hours = presents_for_brav / (self._working_elves // 2)
        return max(time_in_hours, 1)


print(read_from_file('naughty_kids.txt'))
print(read_from_file('brav_kids.txt'))


if __name__ == '__main__':
    pass
