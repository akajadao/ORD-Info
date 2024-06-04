def ler_campos(file):
    campo = ''
    f = file.read(1) ## lê a primeira informação para inicializar
    while (f != '') and (f != '|'):
        campo += f
        f = file.read(1) #lê a próxima informação
    return campo ## retorna as informações

def main():
    nomeArq = input('Digite o nome do arquivo: ')
    i = 1
    try:
        with open(nomeArq, 'r', encoding='utf-8') as file:
            campo = ler_campos(file) ## usa a função
            print('Início da execução!\n')
            while campo:
                print(f'CAMPO #{i}: {campo}')
                campo = ler_campos(file)
                i += 1
                if i > 6:
                    print('')
                    i = 1
        print('\nFim da execução!')
    except FileNotFoundError:
        print(f'Não foi possível abrir o arquivo {nomeArq} pois ele não existe!')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()
