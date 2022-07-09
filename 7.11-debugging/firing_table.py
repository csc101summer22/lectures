# Computes trajectories of cannonballs.


def get_float(prompt):
    """
    Get a floating point value from user input.

    :param prompt: A string to show the user
    :return: The next non-negative float the user types
    """
    x = -1
    while x < 0:
        x = float(input(prompt))
    return x


def time_of_flight(height):
    """
    Compute a cannonball's ideal time of flight.

    :param height: A floating point initial height
    :return: The floating point time of flight
    """
    return (2 * height / 9.81) ** 0.5


def range_of_shot(time, velocity):
    """
    Compute a cannonball's ideal range.

    :param time: A floating point time of flight
    :param velocity: A floating point horizontal velocity
    :param range: The floating point distance traveled
    """
    return velocity * time


def is_hit(shot, distance, width):
    """
    Determine whether or not a cannonball hits.

    :param shot: A cannonball's floating point range
    :param distance: A floating point target distance
    :param width: A floating point target width
    :return: Whether or not the cannonball hits the target
    """
    return distance <= shot


def main():
    return 0


if __name__ == "__main__":
    main()
