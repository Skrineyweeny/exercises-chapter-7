from numbers import Integral

class VerifiedSet(set):
    def __init__(self, values=()):
        for v in values:
            self._verify(v)
        super().__init__(values)

    def add(self, value):
        self._verify(value)
        super().add(value)

    def update(self, value):
        for v in value:
            self._verify(v)
        super().update(value)

    def symmetric_difference_update(self, value):
        for v in value:
            self._verify(v)
        super().symmetric_difference_update(value)

    def union(self, value):
        for v in value:
            self._verify(v)
        return type(self)(super().union(value))

    def intersection(self, value):
        for v in value:
            self._verify(v)
        return type(self)(super().intersection(value))

    def difference(self, value):
        for v in value:
            self._verify(v)
        return type(self)(super().difference(value))

    def symmetric_difference(self, value):
        for v in value:
            self._verify(v)
        return type(self)(super().symmetric_difference(value))

    def copy(self):
        return type(self)(super().copy())

    def _verify(self, value):
        raise NotImplementedError


class IntSet(VerifiedSet):
    def _verify(self, value):
        if not isinstance(value, Integral):
            raise TypeError("Expecting an integer,"
                            f" got a {type(value).__name__}")


class UniqueSet(VerifiedSet):
    def _verify(self, value):
        if value in self:
            raise UniquenessError("Expected to add new integer,"
                                  f"{value} is already in {self}")


class UniquenessError(KeyError):
    pass