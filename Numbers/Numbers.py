
class Numbers:

    def generate_numbers(self, last):
        """Generate numbers from 1 to given 'last' parameter
        :param last: int
        :return: lst: list
        """

        lst = []
        try:
            for numb in range(1, last + 1):
                lst.append(numb)
        except TypeError as t_error:
            raise t_error
        return lst

    def print_to_console(self, amount):
        """Print generated numbers tp console
        :param amount: int
        """

        print("Printing....")
        for x in self.generate_numbers(amount):
            print(f"{x}\n", end="")

    def write_numbers_to_file(self, filename, amount):
        """Write generated numbers to file
        :param filename: with extension i.e "file.txt"
        :param amount: int
        """

        try:
            with open(filename, "w") as file:
                for numb in self.generate_numbers(amount):
                    file.write(f"{numb}\n")
        except IOError as io_error:
            raise io_error

    def read_numbers_from_file(self, filename):
        """Read numbers from file and save it to list
        :param filename: with extension i.e "file.txt"
        :return: lst: list
        """

        lst = []
        try:
            with open(filename, "r") as file:
                for x in file.readlines():
                    lst.append(x.rstrip())
        except FileNotFoundError as fnf_error:
            raise fnf_error
        return lst

    def print_numbers_from_file(self, filename, amount):
        """Print to console given amount of numbers from file
        :param filename: with extension i.e "file.txt"
        :param amount: int
        """

        print("printing from file....")
        from_file = self.read_numbers_from_file(filename)
        try:
            for x in from_file[0:amount]:
                print(f"{x}\n", end="")
        except TypeError as t_error:
            raise t_error


if __name__ == '__main__':

    numbers = Numbers()
    numbers.print_to_console(100)
    numbers.write_numbers_to_file("output.txt", 100)
    numbers.read_numbers_from_file("output.txt")
    numbers.print_numbers_from_file("output.txt", 50)
