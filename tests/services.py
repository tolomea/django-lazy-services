class Service:
    def __init__(self):
        self.base = 7

    def set_val(self, val):
        self.func_val = val

    def get_val(self):
        return self.func_val


class Service2(Service):
    def __init__(self):  # pragma: no cover
        self.base = 8
