"""
Description:

A palindrome is something that reads the same front and back.
Hypothesis: take any natural number. If it is not a palindrome,
write it backwards and add both numbers. If the result is still not a palindrome,
continue taking as given. Stop on reaching the palindrome or after the 10th try.

For example: 78 + 87 = 165, 165 + 561 = 726, 726 + 627 = 1353, 1353 + 3531 = 4884.

It is a hypothesis testing program for the first 200 natural numbers as starting points.
"""

# Function that checks a palindrome for a specific starting point number
def look_for_pallidrom(num):
    sum = int(num)
    counter = 1

    # The while function that runs until the number to be checked, read from left to right,
    # will be equal to its counterpart read from right to left
    while str(sum) != str(sum)[::-1]:
        next_sum = int(str(sum)[::-1])
        sum = sum + next_sum
        # If function used to end the while loop after the 10th try
        if counter == 11:
            # Values used to check for an exception after exiting a while loop
            sum = -10
            counter = -10
            return sum, counter
        counter = counter + 1
    return sum, counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Welcome prompt
    print("\nPalindromic Numbers Finder v1.0\n")

    # Checking the speed of the program
    import time
    start = time.perf_counter()

    for i in range (1, 201):
        # Checking whether the limit of 10 attempts has not been exceeded
        if look_for_pallidrom(i)[0] == -10 and look_for_pallidrom(i)[1] == -10:
            print("Could not find palindrome for number {} in the assumed 10 steps". format(i))
        # If a palindrome is found within the set limit of attempts, display the result
        else:
            print("The palidrome for the number {} found in step {} is {}".format(i, look_for_pallidrom(i)[1], look_for_pallidrom(i)[0]))

    # Display of program execution time
    elapsed = time.perf_counter() - start
    print("\nIt took {:.2f}s".format(elapsed))

"""
Result:

Palindromic Numbers Finder v1.0

The palidrome for the number 1 found in step 1 is 1
The palidrome for the number 2 found in step 1 is 2
The palidrome for the number 3 found in step 1 is 3
The palidrome for the number 4 found in step 1 is 4
The palidrome for the number 5 found in step 1 is 5
The palidrome for the number 6 found in step 1 is 6
The palidrome for the number 7 found in step 1 is 7
The palidrome for the number 8 found in step 1 is 8
The palidrome for the number 9 found in step 1 is 9
The palidrome for the number 10 found in step 2 is 11
The palidrome for the number 11 found in step 1 is 11
The palidrome for the number 12 found in step 2 is 33
The palidrome for the number 13 found in step 2 is 44
The palidrome for the number 14 found in step 2 is 55
The palidrome for the number 15 found in step 2 is 66
The palidrome for the number 16 found in step 2 is 77
The palidrome for the number 17 found in step 2 is 88
The palidrome for the number 18 found in step 2 is 99
The palidrome for the number 19 found in step 3 is 121
The palidrome for the number 20 found in step 2 is 22
The palidrome for the number 21 found in step 2 is 33
The palidrome for the number 22 found in step 1 is 22
The palidrome for the number 23 found in step 2 is 55
The palidrome for the number 24 found in step 2 is 66
The palidrome for the number 25 found in step 2 is 77
The palidrome for the number 26 found in step 2 is 88
The palidrome for the number 27 found in step 2 is 99
The palidrome for the number 28 found in step 3 is 121
The palidrome for the number 29 found in step 2 is 121
The palidrome for the number 30 found in step 2 is 33
The palidrome for the number 31 found in step 2 is 44
The palidrome for the number 32 found in step 2 is 55
The palidrome for the number 33 found in step 1 is 33
The palidrome for the number 34 found in step 2 is 77
The palidrome for the number 35 found in step 2 is 88
The palidrome for the number 36 found in step 2 is 99
The palidrome for the number 37 found in step 3 is 121
The palidrome for the number 38 found in step 2 is 121
The palidrome for the number 39 found in step 3 is 363
The palidrome for the number 40 found in step 2 is 44
The palidrome for the number 41 found in step 2 is 55
The palidrome for the number 42 found in step 2 is 66
The palidrome for the number 43 found in step 2 is 77
The palidrome for the number 44 found in step 1 is 44
The palidrome for the number 45 found in step 2 is 99
The palidrome for the number 46 found in step 3 is 121
The palidrome for the number 47 found in step 2 is 121
The palidrome for the number 48 found in step 3 is 363
The palidrome for the number 49 found in step 3 is 484
The palidrome for the number 50 found in step 2 is 55
The palidrome for the number 51 found in step 2 is 66
The palidrome for the number 52 found in step 2 is 77
The palidrome for the number 53 found in step 2 is 88
The palidrome for the number 54 found in step 2 is 99
The palidrome for the number 55 found in step 1 is 55
The palidrome for the number 56 found in step 2 is 121
The palidrome for the number 57 found in step 3 is 363
The palidrome for the number 58 found in step 3 is 484
The palidrome for the number 59 found in step 4 is 1111
The palidrome for the number 60 found in step 2 is 66
The palidrome for the number 61 found in step 2 is 77
The palidrome for the number 62 found in step 2 is 88
The palidrome for the number 63 found in step 2 is 99
The palidrome for the number 64 found in step 3 is 121
The palidrome for the number 65 found in step 2 is 121
The palidrome for the number 66 found in step 1 is 66
The palidrome for the number 67 found in step 3 is 484
The palidrome for the number 68 found in step 4 is 1111
The palidrome for the number 69 found in step 5 is 4884
The palidrome for the number 70 found in step 2 is 77
The palidrome for the number 71 found in step 2 is 88
The palidrome for the number 72 found in step 2 is 99
The palidrome for the number 73 found in step 3 is 121
The palidrome for the number 74 found in step 2 is 121
The palidrome for the number 75 found in step 3 is 363
The palidrome for the number 76 found in step 3 is 484
The palidrome for the number 77 found in step 1 is 77
The palidrome for the number 78 found in step 5 is 4884
The palidrome for the number 79 found in step 7 is 44044
The palidrome for the number 80 found in step 2 is 88
The palidrome for the number 81 found in step 2 is 99
The palidrome for the number 82 found in step 3 is 121
The palidrome for the number 83 found in step 2 is 121
The palidrome for the number 84 found in step 3 is 363
The palidrome for the number 85 found in step 3 is 484
The palidrome for the number 86 found in step 4 is 1111
The palidrome for the number 87 found in step 5 is 4884
The palidrome for the number 88 found in step 1 is 88
Could not find palindrome for number 89 in the assumed 10 steps
The palidrome for the number 90 found in step 2 is 99
The palidrome for the number 91 found in step 3 is 121
The palidrome for the number 92 found in step 2 is 121
The palidrome for the number 93 found in step 3 is 363
The palidrome for the number 94 found in step 3 is 484
The palidrome for the number 95 found in step 4 is 1111
The palidrome for the number 96 found in step 5 is 4884
The palidrome for the number 97 found in step 7 is 44044
Could not find palindrome for number 98 in the assumed 10 steps
The palidrome for the number 99 found in step 1 is 99
The palidrome for the number 100 found in step 2 is 101
The palidrome for the number 101 found in step 1 is 101
The palidrome for the number 102 found in step 2 is 303
The palidrome for the number 103 found in step 2 is 404
The palidrome for the number 104 found in step 2 is 505
The palidrome for the number 105 found in step 2 is 606
The palidrome for the number 106 found in step 2 is 707
The palidrome for the number 107 found in step 2 is 808
The palidrome for the number 108 found in step 2 is 909
The palidrome for the number 109 found in step 3 is 1111
The palidrome for the number 110 found in step 2 is 121
The palidrome for the number 111 found in step 1 is 111
The palidrome for the number 112 found in step 2 is 323
The palidrome for the number 113 found in step 2 is 424
The palidrome for the number 114 found in step 2 is 525
The palidrome for the number 115 found in step 2 is 626
The palidrome for the number 116 found in step 2 is 727
The palidrome for the number 117 found in step 2 is 828
The palidrome for the number 118 found in step 2 is 929
The palidrome for the number 119 found in step 3 is 1331
The palidrome for the number 120 found in step 2 is 141
The palidrome for the number 121 found in step 1 is 121
The palidrome for the number 122 found in step 2 is 343
The palidrome for the number 123 found in step 2 is 444
The palidrome for the number 124 found in step 2 is 545
The palidrome for the number 125 found in step 2 is 646
The palidrome for the number 126 found in step 2 is 747
The palidrome for the number 127 found in step 2 is 848
The palidrome for the number 128 found in step 2 is 949
The palidrome for the number 129 found in step 3 is 1551
The palidrome for the number 130 found in step 2 is 161
The palidrome for the number 131 found in step 1 is 131
The palidrome for the number 132 found in step 2 is 363
The palidrome for the number 133 found in step 2 is 464
The palidrome for the number 134 found in step 2 is 565
The palidrome for the number 135 found in step 2 is 666
The palidrome for the number 136 found in step 2 is 767
The palidrome for the number 137 found in step 2 is 868
The palidrome for the number 138 found in step 2 is 969
The palidrome for the number 139 found in step 3 is 1771
The palidrome for the number 140 found in step 2 is 181
The palidrome for the number 141 found in step 1 is 141
The palidrome for the number 142 found in step 2 is 383
The palidrome for the number 143 found in step 2 is 484
The palidrome for the number 144 found in step 2 is 585
The palidrome for the number 145 found in step 2 is 686
The palidrome for the number 146 found in step 2 is 787
The palidrome for the number 147 found in step 2 is 888
The palidrome for the number 148 found in step 2 is 989
The palidrome for the number 149 found in step 3 is 1991
The palidrome for the number 150 found in step 3 is 303
The palidrome for the number 151 found in step 1 is 151
The palidrome for the number 152 found in step 3 is 707
The palidrome for the number 153 found in step 3 is 909
The palidrome for the number 154 found in step 3 is 1111
The palidrome for the number 155 found in step 4 is 4444
The palidrome for the number 156 found in step 4 is 6666
The palidrome for the number 157 found in step 4 is 8888
The palidrome for the number 158 found in step 4 is 11011
The palidrome for the number 159 found in step 3 is 1221
The palidrome for the number 160 found in step 3 is 343
The palidrome for the number 161 found in step 1 is 161
The palidrome for the number 162 found in step 3 is 747
The palidrome for the number 163 found in step 3 is 949
The palidrome for the number 164 found in step 4 is 2662
The palidrome for the number 165 found in step 4 is 4884
The palidrome for the number 166 found in step 6 is 45254
Could not find palindrome for number 167 in the assumed 10 steps
The palidrome for the number 168 found in step 4 is 13431
The palidrome for the number 169 found in step 3 is 1441
The palidrome for the number 170 found in step 3 is 383
The palidrome for the number 171 found in step 1 is 171
The palidrome for the number 172 found in step 3 is 787
The palidrome for the number 173 found in step 3 is 989
The palidrome for the number 174 found in step 5 is 5115
The palidrome for the number 175 found in step 5 is 9559
The palidrome for the number 176 found in step 6 is 44044
Could not find palindrome for number 177 in the assumed 10 steps
The palidrome for the number 178 found in step 4 is 15851
The palidrome for the number 179 found in step 3 is 1661
The palidrome for the number 180 found in step 4 is 747
The palidrome for the number 181 found in step 1 is 181
The palidrome for the number 182 found in step 7 is 45254
The palidrome for the number 183 found in step 5 is 13431
The palidrome for the number 184 found in step 4 is 2552
The palidrome for the number 185 found in step 4 is 4774
The palidrome for the number 186 found in step 4 is 6996
Could not find palindrome for number 187 in the assumed 10 steps
The palidrome for the number 188 found in step 8 is 233332
The palidrome for the number 189 found in step 3 is 1881
The palidrome for the number 190 found in step 8 is 45254
The palidrome for the number 191 found in step 1 is 191
The palidrome for the number 192 found in step 5 is 6996
The palidrome for the number 193 found in step 9 is 233332
The palidrome for the number 194 found in step 4 is 2992
The palidrome for the number 195 found in step 5 is 9339
Could not find palindrome for number 196 in the assumed 10 steps
The palidrome for the number 197 found in step 8 is 881188
The palidrome for the number 198 found in step 6 is 79497
The palidrome for the number 199 found in step 4 is 3113
The palidrome for the number 200 found in step 2 is 202

It took 0.04s
"""