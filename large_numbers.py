import math, random

def space_print(col_size:int, *args):
    st = ""
    for i in range(len(args)):
        st += f"{args[i]}{' '*(col_size-len(str(args[i])))}"
    print(st)

class BigNum:
    def __init__(self, digits=None) -> None:
        self.digits = []
        if type(digits) == str or type(digits) == int:
            templist = list(str(digits))
            for s in templist:
                self.digits.append(int(s))
        elif type(digits) == list or type(digits) == tuple:
            for i in digits:
                self.digits.append(int(i))
    
    def __str__(self) -> str:
        if self.digits == []:
            return "Empty BigNum"
        st = ""
        for d in self.digits:
            st += str(d)
        return st
    
    def __add__(self, other):
        debug = True
        ans = BigNum(0)
        if len(self.digits) < len(other.digits):
            longer = other
            shorter = self
        else:
            longer = self
            shorter = other

        for i in range(len(longer.digits) - len(shorter.digits)):
            other.digits.insert(0, 0)
        
        for i in range(len(self.digits)):
            ans.digits.append(0)

        if debug:
            print("self", self.digits)
            print("other", other.digits)
            print("ans", ans.digits)
            print()
        for d in range(len(self.digits)-1, -1, -1):
            #print(f"d{d}  s{self.digits[d]}  o{other.digits[d]}")
            
            if debug:
                print(f"d{d}  ds{self.digits[d]}  do{other.digits[d]}  da{ans.digits[d+1]}")


            dsum = self.digits[d] + other.digits[d] + ans.digits[d+1]
            r = dsum % 10
            carry = None
            
            ans.digits[d+1] += r

            if debug:
                print(f"d{d} ds{dsum} c{carry} r{r}")
                print(ans.digits)
                print()

        if ans.digits[0] == 0:
                del ans.digits[0]
        return ans
    

a = 308
b = 292
n1 = BigNum(a)
n2 = BigNum(b)

sum = n1+n2
print(a, n1, b, n2, a+b, sum, str(a+b) == str(sum))

for i in range(10):
    a = random.randint(1, 999)
    b = random.randint(1, 999)
    n1 = BigNum(a)
    n2 = BigNum(b)
    #print(a, n1, b, n2, a+b, n1+n2, str(a+b) == str(n1+n2))
