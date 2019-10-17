from itertools import permutations

# Simple technique using python itertools library 
def makeLargestNumber(numbers):
    largestNumber = list()
    
    # putting all the possible permutations in a list, and mapping it based on the index
    for i in permutations(numbers, len(numbers)):
        largestNumber.append("".join(map(str, i)))
    
    return max(largestNumber)

# Checking any individual pairs of numbers and checking which value is bigger if we put the first
# or second number first before the other
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))


def myCompare(mycmp):

    # Convert a cmp= function into a key= function
    class Comparison(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return Comparison
     

numbers = [17, 7, 2, 45, 72]
print(makeLargestNumber(numbers))
# 77245217
# 7 72 45 2 17

# driver code
if __name__ == "__main__":
    a = [17, 7, 2, 45, 72]
    sorted_array = sorted(a, key=myCompare(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)
