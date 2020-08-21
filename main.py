#Calendario Python
from datetime import *
import calendar

#imprimir calendario de un determinado año
#imprimir un determindado mes // determinado año
#imprimir la fecha de hoy

def pedir_year():
	return int(input("Ingrese el Año: \n|: "))


def pedir_mes():
	return int(input("Ingrese el Mes: \n|: "))


def imprimir_year():
	calendario_anual = calendar.TextCalendar()
	year_imprimir = pedir_year()
	calendario_anual = calendario_anual.formatyear(year_imprimir)
	return calendario_anual


def imprimir_year_mes():
	calendario = calendar.TextCalendar()
	year_year = pedir_year()
	mes_mes = pedir_mes()
	calendario.prmonth(year_year, mes_mes)
	return "Fin" 


def imprimir_fecha_hoy():
	today = date.today()
	texto = f"Día: {today.day}\n"
	texto += f"Mes: {today.month}\n"
	texto += f"Año: {today.year}"
	return texto


def funcion(fun):
	print(fun())

def menu():
	funciones = [imprimir_year, imprimir_year_mes, imprimir_fecha_hoy]
	opcion = 0
	while opcion<=0 or opcion>3:
		print("Ingresa Una Opcion: ")
		print("1. Calendario Completo")
		print("2. Mes Determinado")
		print("3. Fecha de Hoy")
		opcion = int(input("|: "))
	funcion(funciones[opcion-1])


if __name__ == "__main__":
	menu()