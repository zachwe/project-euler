
def Run():
    with open('input.txt', 'rb') as inp:
        data = [0] * 50
        for line in inp:
            data = [data[i] + int(line[i]) for i in range(len(data))]

        out = [0] * 50
        for i in range(-1, -len(data), -1):
            val = data[i] % 10
            carry = data[i] / 10
            data[i] = val
            data[i - 1] += carry
        data = [str(i) for i in data]
        print data
        data = ''.join(data)
        print len(data[:10])
        return data[:10]

def DumbRun():
    with open('input.txt', 'rb') as inp:
        ar = []
        for line in inp:
            ar.append(int(line))
        return sum(ar)

if __name__ == "__main__":
    print DumbRun()

