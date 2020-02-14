# Notas: Para que funcione con inputs
# se cambia el valor de N por input(), se
# elimina m y en Letras se cambia por input()
#Pido el numero de letras y creo array
N = int(input())
Letras = []
Inp = str(input())
#Coloco las letras en el array
for x in range(N):
  Letras = [str(i) for i in Inp.split()]
#Ordeno y muestro
Letras.sort(key=str.lower)
print(' '.join(str(x) for x in Letras))