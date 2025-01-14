def min_steps_to_one_candy(n: int) -> int:
    """
    Greedy Algorithm to find the minimum steps required to reduce the number 
    of candies to one, using either half-division, adding one, or subtracting one.
    """
    steps = 0
    while n > 1:
        if n % 2 == 0:
            # If n is even, divide by 2
            n //= 2
        else:
            # If n is odd, choose whether to add or subtract 1 for better divisibility
            if (n == 3) or (n % 4 == 1):
                n -= 1
            else:
                n += 1
        steps += 1
    return steps

# Example usage:
candies = 15
print(min_steps_to_one_candy(candies))  # Output: 5
