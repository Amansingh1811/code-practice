class PrimeNumber:
    def prime(self, num ):  
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    print(i, "times" , num//i, "is" , num)
                    break
            else:
                print(num, "is a prime number")
num = int(input("enter the number"))
N = PrimeNumber()
N.prime(num)