class OddNumber:
    def odd(self, num):
        for number in num :
            if number % 2 != 0 :
                print(number)


o = OddNumber()
o.odd(range(10,20))