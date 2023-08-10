# funWithMath
Code for dealing with popular and trivial math problems.

<h1>Prime Numbers</h1>

<h3>isPrime</h3>

<b>Dependencies:</b> math

The isPrime function takes a single int argument (arg) and returns True if it is a prime, or False if it's composite.

<code>def isPrime (arg):
        n = round(math.sqrt(arg),0)
        while (n > 1):
            if (arg % n == 0):
                return (False)
            else:
                n -= 1
       return (True)</code>
