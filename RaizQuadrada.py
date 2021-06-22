import sys
import time
from numpy import sqrt 

def main(entrada): 
    a = float(entrada)
    x = a - 1
    terms_7 = 1 + (x/2 - (x*x)/8 + (x*x*x)/16 - (5*(x*x*x*x))/128 + (7 * (x*x*x*x*x))/256 - (21 * (x*x*x*x*x*x))/1024);
    terms_8 = 1 + (x/2 -  (x*x)/8 + (x*x*x)/16 - (5*(x*x*x*x))/128 + (7 * (x*x*x*x*x))/256 - (21 * (x*x*x*x*x*x))/1024 + ( 99 * (x*x*x*x*x*x*x))/2048);

    print("a = {:.2f}".format(a))
    print("x = {:.2f}".format(x))
    print("raiz de a pelo numpy = {:.15f}".format(sqrt(a)))
    print("7 termos = {:.15f}".format(terms_7))
    print("8 termos = {:.15f}".format(terms_8))

if __name__ == '__main__':
    start_time = time.time()
    main(sys.argv[1])
    print("--- %s seconds ---" % (time.time() - start_time))
