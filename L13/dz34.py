class Counter():
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        return max_max + 1

    def set_min(self, min_min):
        return min_min - 1

    def step_up(self):
        self.current = self.set_max(self.current)
        if self.current > self.max_value:
            raise ValueError("Достигнут максимум")

    def step_down(self):
        self.current = self.set_min(self.current)
        if self.min_value < self.current:
            raise ValueError("Достигнут минимум")

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())  # 10

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
    try:
        counter.step_down()
    except ValueError as e:
        print(e)
print(counter.get_current())  # 10