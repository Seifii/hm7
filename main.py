class m:
    def __init__(self):
        self.n = [10, 20, 30]

    def __iter__(self):
        for it in self.n:
            yield it

