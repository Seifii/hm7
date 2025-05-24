class n:
    def __init__(self):
        self.data = [10, 20, 30]

    def __iter__(self):
        return iter(self.data)
