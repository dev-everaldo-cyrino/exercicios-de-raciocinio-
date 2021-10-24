citya = int(input('habitantes da cidade A:'))
cityb = int(input('habitantes da cidade B:'))
ano = int(input('ano da realização da pesquisa:'))
taxaa= 1.5
taxab= 1.2
anofixo= ano

if citya >= cityb:
    print('a cidade A ja tem mais habitantes do que a cidade B!')
else:
    while citya < cityb:
        citya *= taxaa
        cityb *= taxab
        ano += 1
        if citya > cityb:
            print("""
--------------------------------------------------------------
            """)

            print('os habitantes da cidade A são {:.0f}'.format(citya))
            print('enquanto os habitantes da cidade B são {:.0f}'.format(cityb))
            print('a diferença entre a cidade A para a B é de {:.0f} habitantes!'.format(citya-cityb))
            print('o ano é {} , tendo se passado {} anos desde o inicio da pesquisa'.format(ano,ano-anofixo))

            print("""
--------------------------------------------------------------
            """)
            break