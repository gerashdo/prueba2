

numCandidatos = int(input())
contCombinaciones = 0
nombres = []

for i in range(0,numCandidatos):
	nombres.append(input())
	if(i>=1):
		for j in range(i-1,-1,-1):
			if(nombres[i] != nombres[j] and nombres[i][0]==nombres[j][0]):
				contCombinaciones=contCombinaciones+2

print(contCombinaciones)