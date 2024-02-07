def is_prime(n):
    if n < 2:
        return False
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    return True

def find_3_primes_prod(nums):
    res = []
    for num in nums:
        factors = []
        curr = 2

        while len(factors) < 3 and curr <= num:
            if is_prime(curr) and num % curr == 0:
                factors.append(curr)
                num //= curr
            else:
                curr += 1

        if len(factors) == 3 and num == 1:
            res.append(factors)

    return res

# Example usage:
num_list = [15, 8, 27, 30, 64]
result = find_3_primes_prod(num_list)

for i, factors in enumerate(result):
    prod = 1
    for factor in factors:
        prod *= factor
    print(f"Num {num_list[i]} can be represented as product of 3 primes: {factors} (Product: {prod})")
