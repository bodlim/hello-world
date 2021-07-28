
from typing import List

class Solution:


    def total_array(arr:List[float]) -> float:
        """Total returns the sum of xs."""
        result: float = 0.0
        # for each i float in arr, add it to result
        for i in arr:
            result += i
        return result