__author__ = 'rfischer'


T = input()

for i in range(0, T):
    s = raw_input()
    values = [ord(c) for c in s]
    #print values

    funny = True
    l = len(s)
    for j in range(1, l/2+1):
        if (abs(values[j] - values[j-1]) != abs(values[l-j-1] - values[l-j])):
            funny = False
            break


    if (funny):
        print "Funny"
    else:
        print "Not Funny"