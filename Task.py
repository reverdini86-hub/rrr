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
        all_negative = True

        for i in range(n):
            if matrix[i][j] >= 0:
                all_negative = False
                break
        if all_negative:
            negative_columns.append(j + 1)
    print("\nИсходная матрица:")
    for row in matrix:
        print(" ".join(f"{x:8.2f}" for x in row))

    if negative_columns:
        print(f"\nСтолбцы, содержащие только отрицательные элементы: {negative_columns}")
    else:
        print("\nНет столбцов, содержащих только отрицательные элементы")
if __name__ == "__main__":
    main()
