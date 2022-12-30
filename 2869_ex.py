a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)

#부등식을 계산할 때 시간 초과가 일어남