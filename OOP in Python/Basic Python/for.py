numbers= [40, 50, 20, 30, 29, 49, 21, 31]
sum =0;
for num in numbers:
    sum +=num;

print(sum)

chr= 'oi kire oi kire'
for c in chr:
    print(c)


fr = ['alamin','hadi', 'munim']
for f in fr:
    print(f)


fr = ['alamin1', 'hadi1', 'munim1']

for index, f in enumerate(fr):
    print(f"{index}: {f}") #output: 0: alamin1, 1: hadi1, 2: munim1


# iterate from i = 0 to i = 3
for i in range(0, 4):
    print(i)