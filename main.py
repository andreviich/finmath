from scipy.optimize import linprog
import numpy as np



def createMatrix(length, rows , axe="X"):
    """Функция для создания матрицы в зависимости от задаваемой оси и количеству рядов"""
    arr = []
    if axe == "X":
        startIndex = 0
        endIndex = startIndex + rows - 1
        for i in range(rows):
            print(f"{i} time, {startIndex=} {endIndex=}")
            arrExtra = []
            for i in range(length):

                if i >= startIndex and i<= endIndex:
                    arrExtra.append(1)
                else:
                    arrExtra.append(0)
            startIndex = startIndex +  rows
            endIndex = startIndex + rows - 1
            arr.append(arrExtra)

    elif axe == "Y":
        for i in range(1, rows+1):
            startIndex = i
            endIndex = int(startIndex + rows * (length / rows * (2/3)))
            arrExtra = []
            print(f"{startIndex=} {endIndex=} {rows=}")
            inds = list(range(startIndex-1, endIndex, rows ))
            print(inds)
            for i in range(length):
                if i in inds:
                    arrExtra.append(1)
                else:
                    arrExtra.append(0)
            arr.append(arrExtra)
    return arr



def main():
    """Function for optimization"""
    try:
        count = input("Введите размерность матрицы (целое число)...").strip()

        if (count.isdigit()):

            count = int(count)
            Xrow = input("Введите числа по оси X через пробел (целые числа)... ")

            if (len(Xrow.split()) == count and all([i.isdigit() for i in Xrow.split()])):

                Xrow = [int(i.strip()) for i in Xrow.split()]
                Yrow = input("Введите числа по оси Y через пробел (целые числа)... ")

                if (len(Yrow.split()) == count and all([i.isdigit() for i in Yrow.split()])):

                    Yrow = [int(i) for i in Yrow.split()]

                    countVals = len(Xrow)*len(Yrow)
                    inputValues = input(f"Введите {countVals} чисел для оптимизации через пробел... ")
                    print([i.isdigit() for i in inputValues])
                    if (len(inputValues.split()) == countVals and all([i.isdigit() for i in inputValues.split()])):

                        inputValues = [int(i.strip()) for i in inputValues.split()]

                        cols = createMatrix(length=len(inputValues), rows=len(Yrow), axe="Y")
                        rows = createMatrix(length=len(inputValues), rows=len(Xrow), axe="X")

                        print(f"{cols=} {rows=} {inputValues=} {Xrow=} {Yrow=}")


                        print(f"{linprog(inputValues, rows,Yrow, cols, Xrow)} - result")

                    else:
                        raise TypeError("Неправильный ввод данных")


                else:
                    raise TypeError('Вы ввели числа в неверном формате')
            else:
                raise TypeError('Вы ввели числа в неверном формате')
        else:
            raise TypeError('Введено не число')
    except TypeError as e:
        print(e)
if __name__ == '__main__':
    main()
    # print(createMatrix(9, 3, axe="X"))
