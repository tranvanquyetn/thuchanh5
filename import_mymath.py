import mymath as th
values=[2,4,6,8,10]
print('square:')
for c in values:
    print(th.square(c))
    print('cubes:')
    for c in values:
        print(th.cube(c))
        print('Average: ' + str(th.average(values)))