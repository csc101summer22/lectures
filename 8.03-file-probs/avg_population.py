import sys


def parse_row(row, pops):
    pass


def read_file(csv_name):
    pass


def main():
    pops = read_file(sys.argv[1])

    print("  Region  |  Avg. Pop.")
    print("----------+------------")
    for region in pops:
        average = pops[region][0] / pops[region][1]
        print("%-9s | %11.2f" % (region, average))


if __name__ == "__main__":
    main()
