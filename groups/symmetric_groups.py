from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    """Initialise the Symmetric Group."""

    symbol = "S"

    def _validate(self, permutation):
        if not ((isinstance(permutation, np.ndarray))
                and np.array_equal(np.sort(permutation), np.arange(self.n))):
            raise ValueError("Element value must be an array"
                             f"in the range [0,{self.n})")

    def operation(self, a, b):
        """Operate."""
        return a[b]
