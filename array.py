
from typing import List

class Solution:


    def total_array(arr:List[float]) -> float:
        """Total returns the sum of xs."""
        res: float = 0.0
        # for each i float in arr, add it to res
        for i in arr:
            res += i
        return res
