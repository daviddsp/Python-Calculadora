#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 

#FUNCIONES DE LA CALCULADORA

#FUNCION QUE SUMA DOS VALORES
def sumar(valor1=0,valor2=0):
	return valor1 + valor2 
#FUNCION QUE SUMA DOS VALORES

#FUNCION QUE RESTA DOS VALORES
def restar(valor1=0,valor2=0):
	return valor1 - valor2 
#FUNCION QUE RESTA DOS VALORES

#FUNCION QUE MULTIPLICACION DOS VALORES
def multiplicar(valor1=0,valor2=0):
	return valor1 * valor2 
#FUNCION QUE MULTIPLICACION DOS VALORES

#FUNCIONES DE LA CALCULADORA
def menu():
	#MENU DE OPCIONES
	print("** ::::::::::::::::::::::::: **")
	print(":: Seleccione una operanción ::")
	print("** ::::::::::::::::::::::::: **")
	print("-------------------------------")
	print("| Suma:             ->  1     |")
	print("| Resta:            ->  2     |")
	print("| Multiplicación:   ->  3     |")
	print("| División:         ->  4     |") 
	print("| Potencia:         ->  5     |")
	print("| Raiz cuadrada:    ->  6     |")
	print("| Borrar:           ->  b     |")
	print("| Salir:            ->  s     |")
	print("-------------------------------")
	print("** ::::::::::::::::::::::::: **") 
	print("\n")
	#MENU DE OPCIONES
#OPCIÓN DEL MENU

def opciones(opc=0):
	opcion = int(input("Selecione una Opción... "))
	return opcion

def valores(valor1=0,valor2=0):
	valor1 = int(raw_input("Ingrese su primer valor: "))
	valor2 = int(raw_input("Ingrese su segundo valor: "))
	return (valor1,valor2)

def errorOperacion(opcionError=0):
	regresar = raw_input("¿Quiere realizar una nueva operanción [S/N]? ")
	return (regresar)

menuPrincipal = menu()
opc = opciones()
#OPCIÓN DEL MENU

#MODULO DE SUMA
if(opc == 1):
	print("\n")
	print "** Entrando al modulo de Suma **"
	valoresTeclado = valores()
	valor1 = valoresTeclado[0]
	valor2 = valoresTeclado[1]
	resultadoSuma = sumar(valor1, valor2)
	print "El resultado de su suma es: " + str(resultadoSuma)
	#print "Quiere realizar otra operanción?.."
	nuevaOperacion = errorOperacion()
	#regresar = raw_input("¿Quiere realizar una nueva operanción [Si/No]? ")
	if(nuevaOperacion == "S" and "s"):
		print "Muestro el menu"
		menuNuevo = menu()
		opc = opciones()
		if(opc == 1):
			valoreTecladoNuevo = valores()
			val1Ope = valoreTecladoNuevo[0]
			val2Ope = valoreTecladoNuevo[1]
			sumarNuevo = sumar(val1Ope,val2Ope)
			print "El resultado de su suma es: " + str(sumarNuevo)

		elif(opc == 2):
			restarNuevo = restar(valor1,valor2)

		elif(opc == 3):
			multiplicacionNuevo = multiplicar(valor1,valor2)

	if (nuevaOperacion != "N" and "n" and "S" and "s"):
		print "sali"
		nuevaOperacion2 = errorOperacion()

		if(nuevaOperacion2 == "S" and "s"):
			print "Muestro el menu"
			menuNuevo2 = menu()
			opc2 = opciones()

			if(opc2 == 1):
				valoreTecladoNuevo2 = valores()
				val1Ope2 = valoreTecladoNuevo2[0]
				val2Ope2 = valoreTecladoNuevo2[1]
				sumarNuevo2 = sumar(val1Ope2,val2Ope2)
				print "El resultado de su suma es: " + str(sumarNuevo2)

			elif(opc == 2):
				restarNuevo2 = restar(valor1,valor2)

			elif(opc == 3):
				multiplicacionNuevo2 = multiplicar(valor1,valor2)
	
	#PROBLEMA QUE LA LETRA SEA DISTINTA A S Y A N	
	# if(nuevaOperacion != "S" and "s" and "N" and "n"):
	# 	print "Seleccione una opción valida"



#MODULO DE SUMA

#MODULO DE RESTA
if(opc == 2):
	print("\n")
	print "** Entrando al modulo de Resta **"
	valor1 = int(raw_input("Ingrese su primer valor: "))
	valor2 = int(raw_input("Ingrese su segundo valor: "))
	resultadoResta = restar(valor1,valor2)
	print "El resultado de su resta es: " + str(resultadoResta)

#MODULO DE MULTIPLICACIÓN
if(opc == 3):
	print("\n")
	print "** Entrando al modulo de Multiplicación **"
	valor1 = int(raw_input("Ingrese su primer valor: "))
	valor2 = int(raw_input("Ingrese su segundo valor: "))
	resultadoMultiplicacion = multiplicar(valor1,valor2)
	print "El resultado de su Multiplicación es: " + str(resultadoMultiplicacion)
#MODULO DE MULTIPLICACIÓN