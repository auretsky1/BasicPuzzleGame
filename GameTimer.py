""" This class will be used for the game timer that can be set to count up or down and return info when the
    timer has reached 0 or has counted up to a goal time. The timer can be reset by calling one of the
    set functions."""

class GameTimer(object):
    # Constructor
    def __init__(self):
        # The amount of time in seconds currently on the timer
        self.current_time = 0

        # The goal time (if 0 then counting down otherwise counting up)
        self.goal_time = 0

        # A flag that will determine if the timer should freeze
        self.freeze_timer = True

    # Set the timer to count down from given time
    def countdown(self, time):
        # Unfreeze the timer if frozen
        self.freeze_timer = False

        # Set the current_time to the time given
        self.current_time = time + 1

        # Set the goal time to 0 so we know we are counting down
        self.goal_time = 0

    # Set the timer to count up to goal time
    def countup(self, time):
        # Unfreeze the timer if frozen
        self.freeze_timer = False

        # Set the current time to 0 to start the counting
        self.current_time = -1

        # Set the goal time to the time given so we know we are counting up
        self.goal_time = time

    # Set the timer to count up to infinity
    def countup_forever(self):
        # Unfreeze the timer if frozen
        self.freeze_timer = False

        # Set the current time to 0 to start the counting
        self.current_time = -1

        # Set the goal time to be -2 thus allowing the clock to count up forever
        self.goal_time = -2

    # Check the timer to see if it's reached it's goal time
    def timer_check(self):
        # We know we have reached our goal when the current time and goal time are equal
        if self.current_time == self.goal_time:
            return True
        else:
            return False

    # Convert seconds to minutes with seconds
    @staticmethod
    def convert_to_minutes(current_time):
        # Set the minutes as a string
        minutes = str(current_time // 60)

        # Get the seconds as an int
        seconds = current_time % 60

        # If seconds is less than 10 add a preceding 0
        if seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)

        # Add together as one time string
        return minutes + ":" + seconds

    # Update the timer by one second
    def timer_update(self):
        # Check to see if the goal has been met
        if self.timer_check():
            self.freeze_timer = True

        # Only tick the clock if the timer is not frozen
        if not self.freeze_timer:
            # If goal_time is above 0 we are counting up
            if self.goal_time > 0 or self.goal_time < 0:
                self.current_time += 1
            else:
                self.current_time -= 1

        # Convert the timer to minutes and seconds and return this value as a string
        return self.convert_to_minutes(self.current_time)




