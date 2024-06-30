class Countdown:
    def __init__(self, start):
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value <= 0:
            raise StopIteration
        else:
            self.value -= 1
            return self.value
