import sys


def copy(src, dest):
    """
    Copy the contents of a file.

    :param src: A filename from which to copy
    :param dest: A filename to which to copy
    """
    # NOTE: We want to avoid storing the entire file in memory, so we need to
    #       be able to write a line into dest as soon as it is read from src.
    with open(src, "r") as src_file, open(dest, "w") as dest_file:
        for line in src_file:
            dest_file.write(line)


def main():
    # NOTE: It is common for programs that work with files to take their
    #       filenames as command line arguments. By convention, the zeroth
    #       argument is the name of the program.
    copy(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
