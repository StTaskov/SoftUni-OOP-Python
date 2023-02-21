def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            return False

    if number == 1:
        return False
    if number == 0:
        return False
    return True


def get_primes(numbers):
    return (num for num in numbers if check_prime(num))
