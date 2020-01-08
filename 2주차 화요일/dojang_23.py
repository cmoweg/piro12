from pprint import pprint
col, row = map(int, input().split())
matrix = []
count = 0
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j]=='.':
            count = 0
            for t in range(i-1,i+2):
                for k in range(j-1,j+2):
                    if  0<=t<row and 0<=k<col and '*'==matrix[t][k]:
                        count += 1
                        # print(t+1, '행', k+1, '열', count,'개')
            matrix[i][j] = count
            # print('====S===')
            # print(matrix)
            # print('====E===')

#pprint(matrix, indent = 4, width=40)
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()