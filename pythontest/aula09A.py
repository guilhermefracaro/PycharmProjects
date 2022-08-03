frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::4])

print('')

print(len(frase.strip()))
print(frase.upper().count('O'))

frase = frase.replace('Python', 'Android')
print(frase)

print('')

frase = 'Curso em Vídeo Python'
print('Curso' in frase)
print(frase.lower().find('python'))

print('')

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

