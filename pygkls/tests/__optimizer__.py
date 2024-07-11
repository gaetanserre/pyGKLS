#
# Created in 2023 by Gaëtan Serré
#

import numpy as np
from typing import Tuple, Callable


class Optimizer:
    def __init__(self, **kwargs):
        pass

    def optimize(
        self, function: Callable, verbose: bool
    ) -> Tuple[Tuple[float, float], np.ndarray, np.ndarray]:
        """
        function: function to be minimized
        Returns a tuple containing:
            - a tuple containing the best point found and value at this point
            - a numpy array containing the points visited
            - numpy array containing the values at the points visited
        """
        raise NotImplementedError
