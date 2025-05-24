class n:
    def __init__(self):
        self.m = [10, 20, 30]

    def __iter__(self):
        return iter(self.m)
