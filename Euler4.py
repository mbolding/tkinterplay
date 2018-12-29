#!/usr/bin/env python

palindrome = 1001  # set starting number
B = 10  # B = base used, default is base 10

k = 0  # k = number of digits of 'palindrome'
m = palindrome
while m != 0:  # find k
    m //= B
    k += 1

while k <= 4:

    print(palindrome)

    m = (k - 1) // 2  # compute the middle position
    l = m  # get at the middle position

    while l >= 0:  # l < 0 marks the end of the current k

        # get the digit at position l (counting from l=0)
        digit = (palindrome // (B ** l)) % B

        if digit == B - 1:  # check if digit at l is the last digit 'B-1'
            l -= 1  # if true then base case for l is reached
            continue  # so shift right, to a lower l position

        add = B ** l
        if l < k // 2:  # will evaluate to false only when k%2=1 and l=m
            add += B ** (l + 1)

        palindrome += add
        print(palindrome)

        l = m  # get at the middle position

    palindrome += 2  # base-case for changing the number of digits
    k += 1
