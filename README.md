# elder-sieve
New Prime Number Sieve

Authors: J. W. Helkenberg, Derek P. Moore

The distribution of the prime numbers is a topic of much debate, with most authors believing that there is not a discernable pattern to the distribution. In order to generate a list of primes most previous work relies on an algorithm that first builds a list, then finds the first element in the list (sually 2), and then removes all multiples of that elements. The algorithm then calls for finding the next surviving element and removing all multiples of it, and this carries on until the square root of the limit has been reached, resulting with a list of primes.

We have developed an algorithm that starts with a set of generator functions that are capable of printing all composite terms beneath a limit without need of referencing elements in the generated list. We further demonstrate that the twin primes, cousin primes, sexy primes and quadruple primes are in fact infinite sequences; the algorithm we designed cannot produce a prime number but can produce all composite numbers.

