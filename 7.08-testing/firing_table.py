# Computes trajectories of cannonballs.


def get_float(prompt):
    """
    Get a floating point value from user input.

    :param prompt: A string to show the user
    :return: The next float the user types
    """
    return 0


def time_of_flight(height):
    """
    Compute a cannonball's ideal time of flight.

    :param height: A floating point initial height
    :return: The floating point time of flight
    """
    return (2 * height / 9.81) ** 0.5


def range(time, velocity):
    """
    Compute a cannonball's ideal range.

    :param time: A floating point time of flight
    :param velocity: A floating point horizontal velocity
    :param range: The floating point distance traveled
    """
    # Initially, this will just be a "stub": the bare minimum code needed to
    #  produce a syntactically valid function.
    return 0


def main():
    # Information that we need from the user:
    #   * How high is the cliff?
    #   * How fast is the cannonball?
    #   * How far away is the target?
    # Information that we can then compute:
    #   * How long is the cannonball in the air?
    #   * How far does the cannonball travel?
    # Based on these questions, a "wishlist" of functions:
    #   * Function(s) to get input from the user
    #   * Function to compute the time of flight
    #   * Function to compute the range
    print("Not done yet!")


if __name__ == "__main__":
    main()
