nombre=input("digite nombre del estudiante:  ")
nota_examen_final=float(input("digite la nota de evaluacion final:  "))
nota_quiz_uno=float(input("digite la nota del quiz 1: "))
nota_quiz_dos=float(input("digite la nota del quiz 2:  "))
nota_quiz_tres=float(input("digite la nota del quiz 3: "))
nota_trabajo_final=float(input("digite la nota de trabajo final:  "))
nota=(nota_quiz_uno+nota_quiz_dos+nota_quiz_tres)/3
notafinal=float(nota_examen_final*0.5)+(nota*0.20)+(nota_trabajo_final*0.30)
print(f'el estudiante {nombre} , tiene una nota final de asignatura de: {notafinal}')

