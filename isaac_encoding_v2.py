import datetime, sys

today = datetime.datetime.today()

def space_print(n_spaces, *args):
    st = ""
    for i in range(len(args)):
        st += f"{args[i]}{' '*(n_spaces-len(str(args[i])))}"
    print(st)

def encode(raw_string: str, month: int=None, year: int=None, debug=False) -> str:
    ab = list('abcdefghijklmnopqrstuvwxyz')
    if month == None:
        month = datetime.datetime.today().month
    if year == None:
        year = datetime.datetime.today().year

    if debug:    
        print(month, year, ((year % 2) * 12), ((year % 2) * 12) + month)
        print(ab, '\n')
        print("\033[4mc    prev curr i    off  offl  res\033[0m")

    res = ""


    for i in range(len(raw_string) + 1):
        if i == 0:
            offset = ((year % 2) * 12) + month
            st1 = "?"
            st2 = "-"
            st3 = "-"
        else:
            c = raw_string[i-1]
            prev = ab.index(res[i-1]) + 1
            curr =  ab.index(c) + 1
            offset = ( prev + curr + i ) % 26
        
            st1 = c
            st2 = str(prev)
            st3 = str(curr)
        res += ab[offset-1]
        st4 = str(i)
        st5 = str(offset)
        st6 = ab[offset-1]
        st7 = res

        if debug:
            space_print(5, st1, st2, st3, st4, st5, st6, st7)
    return res[1:]

def decode(raw_string: str, month: int=None, year: int=None, debug=False) -> str:
    ab = list('abcdefghijklmnopqrstuvwxyz')
    if month == None:
        month = datetime.datetime.today().month
    if year == None:
        year = datetime.datetime.today().year
    
    if debug:
        print(month, year, ((year % 2) * 12), ((year % 2) * 12) + month)
        print(ab, '\n')
        print("\033[4mc    prev curr i    off  offl res\033[0m")

    raw_string = "abcdefghijklmnopqrstuvwxyz"[((year % 2) * 12) + month-1] + raw_string
    res = ""
    for i in range(len(raw_string)):

        c = raw_string[i]
        enc = ab.index(c) + 1

        if i == 0:
            prev = 0
        else:
            prev = ab.index(raw_string[i-1]) + 1

        true_val = (enc - i - prev) % 26

        if i != 0:
            res += ab[true_val-1]

        if debug:
            st1 = c
            st2 = str(enc)
            st3 = str(i)
            st4 = str(prev)
            st5 = str(true_val)
            st6 = ab[true_val-1]
            st7 = res
            space_print(5, st1, st2, st3, st4, st5, st6, st7)


    return res
    

if len(sys.argv) == 1:
    string_to_test = input("Enter string to encode: ")
if len(sys.argv) > 1:
    string_to_test = sys.argv[1]
if len(sys.argv) > 2:
    print(f"All arguments after {sys.argv[1]} have been ignored")

print(f"Your string {string_to_test}")
print(f"Encoded: {encode(string_to_test)}")
print(f"Decoded: {decode(encode(string_to_test), 7, 2024)}")
print(f"decoded(encoded) == original: {decode(encode(string_to_test), 7, 2024) == string_to_test}")
