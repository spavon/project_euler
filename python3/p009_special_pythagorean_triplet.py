def print_pyth_trips(num):
    for a in range(1, num):
        for b in range(1, num):
            c = (a**2 + b**2)**0.5
            if(c.is_integer()):
                #print("{}^2 + {}^2 = {}^2".format(a,b,c))
                test_trips(a,b,c,1000)

def test_trips(a,b,c,val):
    if(a+b+c == val):
        print(a,b,c,a*b*c)

def main():
    print_pyth_trips(1000)

if __name__ == '__main__':
    main()
