
class Data:

    def __init__(self, datapth = r"C:/Users/810052/Desktop/ВМ/Входные данные1..txt", dataBack = r"C:\Users\810052\Desktop\ВМ\Выходные данные1..txt"):
        self.dataPath = datapth #по умолчанию идут пути к файлам, кот-е вычисляются, при проведении тестов аргументы изменяются
        self.dataBack = dataBack
        f = open(self.dataPath, 'r')
        self.x = f.readline().split()
        self.y = f.readline().split() #обозначения как она давала, это вектор Fi
        self.n = int(f.readline())
        self.xx = float(f.readline())
        self.m = int(f.readline())
    def Checking(self):
        check = 0
        if self.m >= (self.n + 1):
            check = 1
            print("Код ошибки 1. Многочлен степени m не может быть построен.")
        for i in range(len(self.x) - 1):
            if float(self.x[i]) >= float(self.x[i + 1]):
                check = 2
                print("Код ошибки 2. Нарушен порядок возрастания во входном векторе X.")
                break
        if check == 0:
            self.func()
    def func(self):
        xs = [] #для ближайших точек x
        ys = [] #для ближайших y
        indxL = indxR = 0
        for j in range(len(self.x)):
            while float(self.x[j]) < self.xx: #находим точку "правее" xx
                j+=1
            indxL = int(j-1) #записываем индексы справа и слева от xx
            indxR = int(j)
        for i in range(self.m):
            if abs(float(self.x[indxL])-float(self.xx)) <= abs(float(self.x[indxR])-float(self.xx)): #определяем с какой стороны точка ближе
                if self.x[indxL] not in xs and indxL>0 and indxL<self.n-1:
                    xs.append(self.x[indxL])
                    ys.append(self.y[indxL])
                    indxL-=1
            else:
                if self.x[indxR] not in xs and indxR>0 and indxR<self.n-1:
                    xs.append(self.x[indxR])
                    ys.append(self.y[indxR])
                    indxR+=1
        A = [] #хранение Ai, индексы будут совпадать тк мы же соотносим ее только с массивами xs и ys
        rs = 1
        for i in range(len(xs)):
            for j in range(len(xs)):
                if j!=i:
                    rs *= float(xs[i])-float(xs[j])
            A.append(1/rs)
            rs=1
        L = 0  #конечный результат запишу сюда
        sum = 0
        for i in range(self.m):
            L += float(ys[i])*A[i]/(self.xx - float(xs[i]))
        for i in range(self.m):
            sum += A[i]/(self.xx - float(xs[i]))
        L /=sum
        f = open(self.dataBack,'w')
        f.write("Входные данные: \n "+str(self.x) + '\n')
        f.write(str(self.y)+ '\n')
        f.write(str(self.n)+ '\n')
        f.write(str(self.xx)+ '\n')
        f.write(str(self.m)+ '\n')
        f.write("Выходные данные: \n"+ str(L))
        f.close()
        print ("Код ошибки - 0, результат в выходном файле. Хотите вывести результат на экран? y/n")
        answer =  input()
        if (answer == "y"):
            print ("Результат : " + str(L))







if __name__ == "__main__":
    num = Data()
    num.Checking()
    answer=""
    while (answer!="no"):
        print("Какой тест хотите провести? test1/test2/no")
        answer = input()
        if answer == "test1":
            num2 = Data(r"C:\Users\810052\Desktop\ВМ\Тестовые входные 2..txt",r"C:\Users\810052\Desktop\ВМ\Тестовые выходные 2..txt")
            num2.Checking()
        elif answer == "test2":
            num2 = Data(r"C:\Users\810052\Desktop\ВМ\Тестовые входные 3..txt", r"C:\Users\810052\Desktop\ВМ\Тестовые выходные 3..txt")
            num2.Checking()


