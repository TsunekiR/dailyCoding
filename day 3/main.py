v=[1,2,0]

v.sort()

ans = 1

for i in v:
    if i == ans:
        ans += 1

    
print(ans)