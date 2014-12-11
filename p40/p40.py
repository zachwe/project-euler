
def Run():
    dn_ar = []
    index = 0 # how many digits does out do the first dpn-digit numbers take
              # us.
    dpn = 1 # digits per number
    for i in range(2, 8):
        di = 10 ** (i - 1)
        while di > index + (dpn * ((10** dpn) - (10 ** (dpn - 1)))):
            # look at the (dpn + 1) digit numbers
            index += dpn * ((10** dpn) - (10 ** (dpn - 1)))
            dpn += 1
        rem = di - index
        n = rem / dpn
        dig = rem % dpn
        dn = (10 ** (dpn - 1)) + n
        
        c = str(dn)[dig - 1]
        print index, rem, n, dn
        dn_ar.append(int(c))
    print dn_ar

if __name__ == '__main__':
    Run()
