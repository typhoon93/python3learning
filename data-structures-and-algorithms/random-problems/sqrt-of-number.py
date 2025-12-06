"""
Square root of number, without using a func
E.g. leetcode
https://leetcode.com/problems/sqrtx/description/


"""


def sqrt_newton(n, tolerance=1e-10):
    """
    0.0000000001
    """
    if n < 0:
        raise ValueError("Cannot take square root of negative number")

    x = n
    while True:
        root = 0.5 * (x + n / x)
        if abs(root - x) < tolerance:
            return root
        x = root


def sqrt_binary(n, tolerance=1e-10):
    """
    1e-10 is python scientific notation for 0.0000000001

    """
    if n < 0:
        raise ValueError("Cannot take square root of negative number")

    low, high = 0, max(1, n)

    while high - low > tolerance:
        mid = (low + high) / 2
        if mid * mid > n:
            high = mid
        else:
            low = mid
    return (low + high) / 2





def run_sqrt_binary_tests():
    GREEN = "\033[92m"
    RED   = "\033[91m"
    RESET = "\033[0m"

    test_cases = [
        (0, 0),
        (1, 1),
        (4, 2),
        (9, 3),
        (2, 2**0.5),
        (10, 10**0.5),
        (1e-6, (1e-6)**0.5),
        (1e6, (1e6)**0.5),
    ]

    print("Testing sqrt_binary:\n")

    for i, (n, expected) in enumerate(test_cases, 1):
        result = sqrt_binary(n)
        if abs(result - expected) < 1e-7:
            print(f"{GREEN}✅ Test {i}: n={n} → {result} (expected {expected}){RESET}")
        else:
            print(f"{RED}❌ Test {i}: n={n} → {result} (expected {expected}){RESET}")

    # error test
    try:
        sqrt_binary(-1)
        print(f"{RED}❌ Test error: negative input did NOT raise ValueError{RESET}")
    except ValueError:
        print(f"{GREEN}✅ Test error: negative input correctly raised ValueError{RESET}")


if __name__ == "__main__":
    run_sqrt_binary_tests()