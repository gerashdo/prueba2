

numCandidatoss = int(input())
contCombinaciones = 0
nombres = []
##geras
for i in range(0,numCandidatoss):
	nombres.append(input())
	if(i>=1):
		for j in range(i-1,-1,-1):
			if(nombres[i] != nombres[j] and nombres[i][0]==nombres[j][0]):
				contCombinaciones=contCombinaciones+2

print(contCombinaciones)