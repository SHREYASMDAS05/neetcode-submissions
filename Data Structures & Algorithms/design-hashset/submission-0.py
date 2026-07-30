class MyHashSet:

    def __init__(self):
        self.Hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.Hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.Hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.Hashset