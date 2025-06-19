# Вариант 33. F(n<3)=2;F(n)= (-1)n*(F(n-1)-(n-2)!+F(n-1)/(2n)!)(при n >12), F(n)=F(n-2)-F(n-1) (при 5<n<=12)
import math
import timeit
import matplotlib.pyplot as plt

def sign(n):
    return 1 if n % 2 == 0 else -1

def F_recursive(n):
    if n < 3:
        return 2
    if n <= 12:
        return F_recursive(n-2) - F_recursive(n-1)
    return sign(n) * (F_recursive(n-1) - math.factorial(n-2) + F_recursive(n-1) / math.factorial(2*n))

def F_iterative(n):
    if n < 3:
        return 2
    f_prev2, f_prev1 = 2, 2
    fact_n_minus2 = 1
    fact_2n = math.factorial(2)
    for i in range(3, n+1):
        fact_n_minus2 *= (i-2)
        fact_2n *= (2*i - 1) * (2*i)
        if i <= 12:
            f_current = f_prev2 - f_prev1
        else:
            f_current = sign(i) * (f_prev1 - fact_n_minus2 + f_prev1 / fact_2n)
        f_prev2, f_prev1 = f_prev1, f_current
    return f_prev1

def main():
    start_n = 1
    end_n = 25 
    results = []
    for n in range(start_n, end_n + 1):
        tr = timeit.timeit(lambda: F_recursive(n), number=10)
        ti = timeit.timeit(lambda: F_iterative(n), number=10)
        results.append((n, tr, ti))

    print(f"{' n':>4} | {'Rec Time (s)':>12} | {'Iter Time (s)':>12}")
    print("-" * 42)
    for n, tr, ti in results:
        print(f"{n:4d} | {tr:12.6f} | {ti:12.6f}")

    xs = [r[0] for r in results]
    yr = [r[1] for r in results]
    yi = [r[2] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(xs, yr, '--o', label='Рекурсивный')
    plt.plot(xs, yi,  '-o', label='Итеративный')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение времени вычисления F(n)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
