n = int(input())
answer = 0
for i in range( 1, n):
    for j in range( 1, n):
        if i >= j:
            continue
        if n % (i+j) == 0:
            answer = (answer * 10) + i
            if j < 10:
                answer = (answer * 10) + j
            else:
                answer = (answer * 100) + j
print(answer)