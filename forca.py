# palavra_secreta = ['M', 'A', 'N', 'T', 'E', 'I', 'G', 'A']

print('\n***Jogo da Forca***')

palavra = str(input('Digite uma palavra para a forca\n')).strip().upper()
palavra_secreta = list(palavra)

letras_descobertas = []

print('\n\n\n\n\n\n\n\n\n\n')

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append('_')

acertou = False
contador = 0

while acertou == False:
    print('')
    letra_escrita = str(input('Digite uma letra\n')).strip().upper()

    if len(letra_escrita) >= 2 or len(letra_escrita) <= 0:
        print('Letras demais ou nada escrito')
    else:
        contador += 1
        for i in range(0, len(palavra_secreta)):
            if letra_escrita == palavra_secreta[i]:
                contador -= 1
                letras_descobertas[i] = letra_escrita

        acertou = True

        for x in range(0, len(letras_descobertas)):
            if letras_descobertas[x] == '_':
                acertou = False

        print(letras_descobertas)

        if contador == 7:
            print("""
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
             $$u$ $ $ $ $u$$       
              $$$$$u$u$u$$$       
               "$$$$$$$$$" 
               
              Você Perdeu!!!""")
            break

        if acertou:
            print('')
            print('\033[0;34mVOCÊ GANHOU!!!!!!')
