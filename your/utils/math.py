import math
from functools import reduce

import numpy as np
from scipy import stats

def closest_number(big_num, small_num):
    """
    Finds the difference between the closest multiple of a smaller number with respect to a bigger number

    Args:

        big_num: The bigger number to find the closest of

        small_num: Number whose multiple is to be found and subtracted

    Returns:

        The difference between the closest multiple of a smaller number with respect to a bigger number

    """
    if big_num % small_num == 0:
        return 0
    else:
        q = big_num // small_num
        return (q + 1) * small_num - big_num


def primes(n):
    """
    All the prime factors of a positive number

    Args:

        n: a positive number

    Returns: primes
    """

    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def closest_divisor(n, m):
    """

    Calculates the divisor of n, which is closest to (i.e bigger than) m

    Args:

        n: larger number of which divisor is to be found

        m: divisor closest to this number


    Returns:

        The divisor of n, which is closest to (i.e bigger than) m

    """
    pfs = primes(n)
    div = 1
    ind = 0
    while div < m:
        div *= pfs[ind]
        ind += 1
    return div


def find_gcd(list_of_nos):
    """
    Greatest Common Divisor for a list of nos

    Args:

        list_of_nos: list of numbers

    Returns:

        GCD

    """
    x = reduce(math.gcd, list_of_nos)
    return x


def normalise(data):
    """
    Subtract median, divide by standard deviations

    Args:

        data (numpy.ndarray): data

    Returns:

        numpy.ndarray: normalised data

    """
    data = np.array(data, dtype=np.float32)
    data -= np.median(data)
    data /= np.std(data)
    return data

def smad_plotter(freq_time, sigma=3.0, clip=True):
    """
    spectal Median Absolute Deviation clipper
   
    Args:
        
        freq_time: the frequency time data

        sigma (float): sigma at which to clip data 
    """
    sigs = 1.4826*stats.median_absolute_deviation(freq_time, axis=0)
    if clip:
        return np.transpose([np.clip(freq_time[:,j], a_min=-sigma, a_max=sigma) \
                                 for j, sigma in enumerate(sigs)])
