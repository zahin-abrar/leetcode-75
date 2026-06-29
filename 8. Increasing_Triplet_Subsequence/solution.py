def increasingTriplet(num: list) -> bool:
    smallest_so_far = float("inf")
    middle_candidate = float("inf")

    for n in num:
        if n <= smallest_so_far:
            smallest_so_far = n
        elif n <= middle_candidate:
            middle_candidate = n
        else:
            return True

    return False

print(increasingTriplet([2, 1, 5, 0, 4]))