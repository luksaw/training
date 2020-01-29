
class Counter:

    def __init__(self):
        self.number = 0

    def write_to_file(self):
        print("writing to file")
        file = open("output.txt", "w")
        while self.number < 100:
            self.number += 1
            print(self.number)
            file.write(f"{self.number}\n")
        file.close()

    def print_50_files(self):
        print("reading from file")
        with open("output.txt", "r") as output:
            for line_number, line in enumerate(output):
                if line_number >= 50:
                    break
                print(line, end="")
            # print(line_number)

            # for line in list_of_lines:
            #     print(line.rsplit("\n")[0])
            # first_50 = [next(output) for x in range(50)]
            # print(first_50)


if __name__ == '__main__':
    counter = Counter()
    counter.write_to_file()
    counter.print_50_files()
