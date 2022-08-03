import sys


def parse_row(row, pops):
    """
    Read the contents of a single CSV row.

    :param row: A string row from a CSV
    :param pops: A dictionary mapping regions to [population, count] lists
    """
    cells = row.split(",")
    region = cells[1].strip()
    pop = int(cells[2].strip())

    if region in pops:
        pops[region][0] = pops[region][0] + pop
        pops[region][1] = pops[region][1] + 1
    elif region != "":
        pops[region] = [pop, 1]


def read_file(csv_name):
    """
    Read the contents of a CSV file.

    :param csv_name: A CSV's filename
    :return: A dictionary mapping regions to [population, count] lists
    """
    pops = {}

    with open(csv_name, "r") as csv:
        # NOTE: The first line is the header, which we need to ignore.
        csv.readline()

        # NOTE: This loop will pick up from the second line; it won't reset.
        for row in csv:
            parse_row(row, pops)

    return pops


def main():
    pops = read_file(sys.argv[1])

    print("  Region  |  Avg. Pop.")
    print("----------+------------")
    for region in pops:
        average = pops[region][0] / pops[region][1]
        print("%-9s | %11.2f" % (region, average))


if __name__ == "__main__":
    main()
