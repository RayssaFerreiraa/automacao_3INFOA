#from(do arquivo) funcoes import (importa a funcao) CalculateTrianglArea
from funcoes import CalculateTrianglArea, CalculateSquareArea

area = CalculateTrianglArea(10, 10)
print ('Área: ', area)

areaQuadrado = CalculateTrianglArea(10)
print('Área do quadrado', areaQuadrado)