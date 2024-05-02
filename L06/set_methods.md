# Set methods

    add
    clear
    copy
    pop - removes and returns "random" element
    remove - removes element, raises exception if element is missing
    discard - removes element, do nothing if element is missing

    # methods with update, applies operation to left operand
    # methods with update, return new set
    union (s3 = s1 | s2)
    update

    difference (s3 = s1 - s2)
    difference_update

    intersection  (kind of "not intersetion") (s3 = s1 & s2)
    intersection_update

    symmetric_difference (s3 = s1 ^ s2)
    symmetric_difference_update

    isdisjoint (no common elements, "sets are independent")
    issubset  (<=)
    issuperset (>=)
