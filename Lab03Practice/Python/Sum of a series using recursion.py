def ssum(N, I, F):
    if N == 0:
        return 0
    elif N >= 1:
        return ssum(N - 1, I, F) + F + (N - 1) * I


# Main
t = int(input("How many times? : "))

for i in range(t):
    f = int(input("First Number: "))
    d = int(input("Interval: "))
    n = int(input("n: "))

    print("Series sum: ", ssum(n, d, f))
