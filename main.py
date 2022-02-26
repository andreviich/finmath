from scipy.optimize import linprog

def createMatrix(length, rows , axe="X"):
    """Функция для создания матрицы в зависимости от задаваемой оси и количеству рядов"""
    arr = []

    #генерация матрицы для горизонатали
    if axe == "X":
        startIndex = 0
        endIndex = startIndex + rows - 1
        for i in range(rows):
            arrExtra = []
            for i in range(length):

                if i >= startIndex and i<= endIndex:
                    arrExtra.append(1)
                else:
                    arrExtra.append(0)
            startIndex = startIndex +  rows
            endIndex = startIndex + rows - 1
            arr.append(arrExtra)

    #генерация матрицы для вертикали
    elif axe == "Y":
        for i in range(1, rows+1):
            startIndex = i
            endIndex = int(startIndex + rows * (length / rows * (2/3)))
            arrExtra = []
            inds = list(range(startIndex-1, endIndex, rows ))
            for i in range(length):
                if i in inds:
                    arrExtra.append(1)
                else:
                    arrExtra.append(0)
            arr.append(arrExtra)
    return arr



def main():
    """Функция для оптимизации"""
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

                        # генерируем матрицу для колонок
                        cols = createMatrix(length=len(inputValues), rows=len(Yrow), axe="Y")

                        # генерируем матрицу для строк
                        rows = createMatrix(length=len(inputValues), rows=len(Xrow), axe="X")


                        # вызываем функцию linprog для оптимизации
                        return linprog(inputValues, rows,Yrow, cols, Xrow)

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

def output():
    print(f"{main()} - result")
if __name__ == '__main__':
    output()
