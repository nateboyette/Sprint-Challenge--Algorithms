class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort_item_right(self):
        if self.compare_item() == 1:
            self.move_right()
        elif self.compare_item() == -1:
            self.swap_item()
            self.move_right()
        elif self.compare_item() == 0:
            self.move_right()
        elif self.compare_item() is None:
            self.swap_item()
            self.move_right()

    def sort_item_left(self):
        if self.compare_item() == 1:
            self.swap_item()
            self.move_left()
        elif self.compare_item() == -1:
            self.move_left()
        elif self.compare_item() == 0:
            self.move_left()

    def sort(self):
        """
        Sort the robot's list.
        """

        # If robot is at the beggining and either holding None
        # Turn on the light to start sorting
        if self.can_move_left() is False and self.compare_item() is None:
            self.set_light_on()

        # while the light is on the robot will sort to the right
        # until it reaches the end of the list
        while self.light_is_on() is True:\

            # If the robot reaches the end of the list and the held item
            # is less that the item in the list. Turn off the light to start
            # sorting left/back down the list.
            if self.compare_item() == -1 and self.can_move_right() is False:
                self.set_light_off()

            # If the item is greater than the last item in the list
            # swap and turn off the light to start sorting back down the list.
            elif self.compare_item() == 1 and self.can_move_right() is False:
                self.swap_item()
                self.set_light_off()

            # If the robot makes it back to the beggining of the list and
            # THe first item is none, swap the item held and continue sorting right.
            elif self.can_move_left() is False and self.compare_item() is None:
                self.swap_item()
                self.move_right()

            # If the last item held is None and we've reached the end of the list
            # That means the list has been sorted and we can break out of the loop
            elif self.can_move_right() is False and self.compare_item() is None:
                return
            else:
                self.sort_item_right()

        while self.light_is_on() is False:

            # While sorting left, if the item is None
            # Swap and begin sorting to right from this position
            if self.compare_item() is None:
                self.swap_item()
                self.move_right()
                self.set_light_on()
            else:
                self.sort_item_left()

        self.sort()
    # Fill this out


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    # l = [48, 33, 2, 5, 6]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


# I realized I needed a way to loop up and down the list, checking for when the robot reaches the end of the list and whether the number at the start/end of the list needs to be sorted.

# The list now sorts properly but I've created an endless loop. I need to figure out how to break out of it.


# **SOLVED** I realized in order to break out of the list I needed to move "None" up the list as it got sorted. That was I could check once the robot made it back up to the list and whether or not the comparison returned None. If so I knew the list is sorted and I could break out of the loop and return the sorted list.


# Solution also passes the stretch tests.
