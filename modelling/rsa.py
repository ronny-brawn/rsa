import math
import random


def is_prime(n):
    """
    Check if a number is prime

    Args:
        n (int): Number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check divisibility up to square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def rsa(p, q):
    """
    Generate and display RSA public and private keys

    Args:
        p (int): First prime number
        q (int): Second prime number

    Raises:
        ValueError: If p or q are not prime, or if no suitable key pairs are found
    """
    # Verify that p and q are prime numbers
    if not is_prime(p):
        raise ValueError(f"{p} is not a prime number")
    if not is_prime(q):
        raise ValueError(f"{q} is not a prime number")

    n = p * q
    m = (p - 1) * (q - 1)

    # Find all possible values for e
    e_list = []
    for i in range(2, n):
        if math.gcd(i, m) == 1:
            e_list.append(i)

    # Try different e values until we find one where d != e
    for e in random.sample(e_list, len(e_list)):
        # Find one valid d value
        d = None
        for j in range(n):
            d_val = (m * j + 1) / e
            if d_val == round(d_val, 0):
                d_val = int(d_val)
                if d_val < n and d_val != 1 and d_val != e:
                    d = d_val
                    break

        if d is not None:
            print(f"Public Key: {e},{n}")
            print(f"Private Key: {d},{n}")
            return

    raise ValueError("No suitable e and d pairs found (d cannot equal e)")


