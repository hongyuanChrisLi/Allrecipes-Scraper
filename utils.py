def validate(files):
    max = 0
    seen = {}
    for file in files:
        input = open(file, 'r')
        line = input.readline()
        while line:
            check = int(line)
            if check > max:
                max = check
            if check in seen:
                seen[check].append(file)
            else:
                seen[check] = [file]
            line = input.readline()
        input.close()
    flag = True
    for i in xrange(1, max + 1):
        if i not in seen:
            print str(i) + ' is missing'
            flag = False
        elif len(seen[i]) > 1:
            print str(i) + ' was downloaded in ' + str(seen[i])
            flag = False
    if flag:
        print 'All good'

def count(files):
    count = 0
    for file in files:
        input = open(file, 'r')
        line = input.readline()
        while line:
            count += 1
            line = input.readline()
        input.close()
    print count

def merge(inputs, output):
    out = open(output, 'a')
    for input in inputs:
        inp = open(input, 'r')
        line = inp.readline()
        while line:
            out.write(line)
            line = inp.readline()
        inp.close()
    out.close()

validate(['D:/log1.log', 'D:/log2.log', 'D:/log3.log', 'D:/log4.log', 'D:/log5.log', 'D:/log6.log', 'D:/log7.log', 'D:/log8.log'])
count(['D:/recipes1.data', 'D:/recipes2.data', 'D:/recipes3.data', 'D:/recipes4.data'])
count(['D:/reviews1.data', 'D:/reviews2.data', 'D:/reviews3.data', 'D:/reviews4.data'])
