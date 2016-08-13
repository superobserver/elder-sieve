# elder-sieve
New Prime Number Sieve

Authors: J. W. Helkenberg, Derek P. Moore

The distribution of the prime numbers is a topic of much debate, with most authors believing that a discernable underlying pattern does not exist. In order to generate a list of primes most previous work relies on an algorithm that first builds a list, then finds the first element (2 in the case of Sieve of Eratosthenes), and then removes all multiples of that element. The algorithm then calls for finding the next surviving element and removing all multiples of it, and this carries on until the square root of the limit has been reached, resulting with a list of primes.

We have developed an algorithm that starts with a set of sequence generator functions that are capable of printing all composite terms beneath a limit without need of referencing elements in the generated list; this means the we can sieve from the limit down or from 0 up or both simultaneously, as there is no "internal" state dependency. We further demonstrate that the twin primes, cousin primes, sexy primes and quadruple primes are in fact infinite sequences; proving that the algorithm we designed cannot produce a prime number but can produce all composite numbers is trivial.

In order to recover a base 10 number one needs to multiply the output by 90 and add a related constant. Many, though not all, of our sequences correspond with OEIS database entries. We offer the following programs in the hopes of furthering awareness of this unique sieve and of stimulating discussions regarding the prime numbers.

