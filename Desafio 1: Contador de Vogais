def contar_vogais(frase):
  vogal = 0
  for letra in frase.lower():
    if letra in 'a, e, i, o, u':
      vogal += 1
  return vogal

print('=' * 30)
print('     CONTADOR DE VOGAIS')
print('=' * 30)

while True:
  resultado = contar_vogais(str(input('Digite uma palavra ou frase: ')))
  print()
  print(f'O resultado é [{resultado}] vogais.')
  print()
  resp = str(input('Continuar? [S/N] ')).lower()
  print()
  if resp == 'n':
    print('Até a próxima!')
    break
