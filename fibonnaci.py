# This class implements Fibonacci series
# Enter your max sequence as input and get Fib series printed accordingly

class FibonacciSeries:
    max_series = 0  # Variable to  store max series from user input
    max_fibValue = 0  # Variable to count the values from 0 to max series

    def fibseries(self):
        fib_start, fib_next = 0, 1  # Fib start value and next value
        fib_sum = fib_start + fib_next
        fib_seq = 1  # fib sequence is 1 by default
        print("Your Fibonacci Series for max of ", end=" ")
        while (fib_seq <= self.max_series):
            fib_seq += 1  # increment of fib sequence with 1
            print(fib_start, end=" ")
            fib_start = fib_next   # Assign next fib value to fib start of next sequence
            fib_next = fib_sum   # Assign incremented sequence to next value
            fib_sum = fib_start + fib_next  # Sum of start and next
            self.max_fibValue = fib_sum  # assign sum to max value for unit test

fibObject = FibonacciSeries()
fibObject.max_series = int(input ("Sequence up to what value you want to show ? "))
fibObject.fibseries()
