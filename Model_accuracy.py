



f = open('RESNET50-model_2022-12-30_accuracy.txt','r')

T = {}
for x in f:
    x = x.split(':')
    x[1] = float(x[1])
    T[x[0]] = x[1]

print(T)
