# -*- coding: utf-8 -*-

lista = [3, 1, 4, 8, 427, 7];

for i in range(len(lista)):
	
	menor = i;

	for j in range(i+1,len(lista)):

		if lista[j] < lista[menor]:
			menor = j;

	if lista[i] != lista[menor]:
		
		aux = lista[i];
		lista[i] = lista[menor];
		lista[menor] = aux;

print (lista);