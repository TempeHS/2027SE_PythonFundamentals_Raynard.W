class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be below 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0 or self._size + n > self._capacity:
            raise ValueError("Deposit invalid")

    def withdraw(self, n):
        if n < 0 or n > self._size:
            raise ValueError("Withdraw invalid")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
