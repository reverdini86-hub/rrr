def main():
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        if len(row) != m:
            print(f"Ошибка: должно быть {m} элементов в строке")
            return
        matrix.append(row)
    negative_columns = []
    for j in range(m):
        if all(matrix[i][j] < 0 for i in range(n)):
            negative_columns.append(j + 1)
    positive_rows = [i + 1 for i in range(n) if all(x > 0 for x in matrix[i])]
    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:8.2f}" for x in row))
    if negative_columns:
        print(f"\nСтолбцы с только отрицательными элементами: {negative_columns}")
    else:
        print("\nНет столбцов с только отрицательными элементами")
    if positive_rows:
        print(f"Строки с только положительными элементами: {positive_rows}")
    else:
        print("Строк с только положительными элементами нет")
if __name__ == "__main__":
    main()

