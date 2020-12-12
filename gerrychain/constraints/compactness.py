
import math

from .bounds import SelfConfiguringLowerBound, SelfConfiguringUpperBound

# take the sum of all Polsby Popper scores in the partition (each district) raised to the power of -1 prior to summation
def L1_reciprocal_polsby_popper(partition):
    return sum(1 / value for value in partition["polsby_popper"].values())

# take the sum of all Polsby Popper scores in the partition (each district)
def L1_polsby_popper(partition):
    return sum(value for value in partition["polsby_popper"].values())

# take the sum of all Polsby Popper scores in the partition (each district) raised to the power of 2 before summation
def L2_polsby_popper(partition):
    return math.sqrt(sum(value ** 2 for value in partition["polsby_popper"].values()))

# take the number of parts in the partition divided by the sum of all Polsby Popper scores in the partition (each district) raised to the power of -1 prior to summation
def L_minus_1_polsby_popper(partition):
    return len(partition.parts) / sum(
        1 / value for value in partition["polsby_popper"].values()
    )


no_worse_L_minus_1_polsby_popper = SelfConfiguringLowerBound(L_minus_1_polsby_popper)

no_worse_L1_reciprocal_polsby_popper = SelfConfiguringUpperBound(
    L1_reciprocal_polsby_popper
)
