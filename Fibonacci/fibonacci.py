# Fibonacci Sequence by Angelique Everitt
print()
print("Fibonacci Sequence Mini Project")
print()
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence [-2]
        sequence.append(next_value)
    return sequence

num_terms = int(input("enter the number of terms:"))
print()

fib_sequence = fibonacci(num_terms)
print("Fibonacci Sequence: ")
print(fib_sequence)
print()
print("fin")
print()
