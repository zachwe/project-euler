"""
n --> n / 2         N IS EVEN
n --> 3n+ 1         N IS ODD

Theorem (unproven): all sequences end at 1.
"""

class Collatz:
    def Call(self, new):
        steps = 1
        val = new
        while val > 1:
            if val % 2 == 0:
                val = self.Even(val)
            elif val % 2 == 1:
                val = self.Odd(val)
            steps += 1
        return steps


    def Even(self, start):
        return start / 2
    
    def Odd(self, start):
        return 3 * start + 1

def Run():
    maxsteps, maxval = 0, 0
    c = Collatz()
    for i in range(500000, int(1000000 + 1)):
        tmp = c.Call(i)
        if tmp > maxsteps:
            maxsteps = tmp
            maxval = i
    print "Maximum length chain: " + str(maxsteps)
    print "Value that yields that chain: " + str(maxval)
        


if __name__ == "__main__":
    Run()


