
class Numbers:

    def generate_numbers(self, last):
        lst = []
        try:
            for numb in range(1, last + 1):
                lst.append(numb)
        except TypeError as t_error:
            raise t_error
        return lst

    def print_to_console(self, amount):
        print("printing....")
        for x in self.generate_numbers(amount):
            print(f"{x}\n", end="")

    def write_numbers_to_file(self, filename, amount):
        try:
            with open(filename, "w") as file:
                for numb in self.generate_numbers(amount):
                    file.write(f"{numb}\n")
        except IOError as io_error:
            raise io_error

    def read_numbers(self, filename, amount):
        print("reading....")
        try:
            for x in self.generate_numbers(amount):
                if x == amount:
                    break
            with open(filename, "r") as file:
                for line_number, line in enumerate(file):
                    if line_number == amount:
                        break
                    print(line, end="")
            return int(f"{line}".rstrip()) - 1


            # with open(filename, "r") as file:
            #     for line_number, line in enumerate(file):
            #         if line_number == amount:
            #             break
            #         print(line, end="")
        except FileNotFoundError as fnf_error:
            raise fnf_error


if __name__ == '__main__':
    numbers = Numbers()
    numbers.print_to_console(100)
    numbers.write_numbers_to_file("output.txt", 100)
    numbers.read_numbers("output.txt", 50)
