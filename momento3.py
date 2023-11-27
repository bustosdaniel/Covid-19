import pandas as pd
import matplotlib.pyplot as plt

##PUNTO 1

datos = pd.read_excel('COVID-19.xlsx', sheet_name='Hoja1')

departamentos = datos['departamento'].tolist()

muertes = datos['muertes'].tolist()

plt.figure(figsize=(160, 40))
plt.bar(departamentos, muertes, color='green')
plt.ylabel('Número de muertes')
plt.xlabel('Departamento')
plt.savefig('grafico_muertes.png')
plt.show()

##PUNTO 2

ciudades = ['Bogotá D.C', 'Medellin', 'Cali', 'Barranquilla', 'Bucaramanga']
indice_muertes = [17775, 6390, 5041, 4723, 2302] 

plt.figure(figsize=(10, 6))
plt.barh(ciudades, indice_muertes, color='green')

plt.title('Top 5 Ciudades con Mayor Índice de Muertes por Casos Confirmados (2021)')
plt.xlabel('Índice de Muertes por Casos Confirmados')
plt.ylabel('Ciudades')

plt.tight_layout()
plt.savefig('indice_muertes.png')
plt.show()

##PUNTO 3

confirmados = 75048
sospechosos = 14485
descartados = 3794

total_casos = confirmados + sospechosos + descartados

porcentaje_confirmados = (confirmados / total_casos) * 100
porcentaje_sospechosos = (sospechosos / total_casos) * 100
porcentaje_descartados = (descartados / total_casos) * 100

labels = ['Confirmados', 'Sospechosos', 'Descartados']
sizes = [porcentaje_confirmados, porcentaje_sospechosos, porcentaje_descartados]
colors = ['green', 'gold', 'skyblue']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal') 
plt.title('Casos de COVID-19 en 2021')
plt.savefig('grafico_porcentaje.png')
plt.show()

##PUNTO 4

muertes_por_mes = [11, 5, 30, 320, 867, 2829, 5869, 7997, 5496, 5224, 5232, 6728]

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

plt.figure(figsize=(10, 6))
plt.plot(meses, muertes_por_mes, marker='o', linestyle='-', color='gold', linewidth=2, markersize=8)

plt.title('Muertes COVID-19 Confirmadas por Mes en 2020')
plt.xlabel('Mes')
plt.ylabel('Total de Muertes')
plt.grid(True)
plt.xticks(meses) 

plt.tight_layout()
plt.savefig('grafico_fechas.png')
plt.show()

##PUNTO 5

edades = [0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-84, 85-89, 90-100]
muertes_por_edad = [82, 39, 112, 63, 140, 242, 389, 653, 946, 1320, 2085, 3090, 4307, 5056, 5500, 5335, 5217, 3686, 2346]

plt.figure(figsize=(10, 6))
plt.bar(edades, muertes_por_edad, width=4, color='yellowgreen')  

plt.title('Histograma de Muertes COVID-19 Confirmadas por Edades Quinquenales')
plt.xlabel('Edades')
plt.ylabel('Cantidad de Muertes')
plt.xticks(edades)

plt.tight_layout()
plt.savefig('muertes_edades.png')
plt.show()