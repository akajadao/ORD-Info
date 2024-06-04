## Aluno: Jader Alves dos Santos
## RA: 120286

# a função le o arquivo em binário
def leia_reg(file):
    tam_bytes = file.read(2)
    # converte os bytes para inteiro
    tam = int.from_bytes(tam_bytes)
    if tam > 0:
        # armazena no buffer o texto do tamanho dos bytes
        buffer = file.read(tam)
        # transforma numa string
        buffer = buffer.decode()
        return buffer
    else:
        return ''

def main():
    
    nomeArq = input('Digite o nome do arquivo: ')
    print('')
    try:
        i = 0
        with open(nomeArq, 'rb') as file:
            # enquanto o buffer não for vazio
            while True:
                buffer = leia_reg(file)
                # separa o buffer em campos pelo indicador: "|"
                campos = buffer.split(sep='|')
                if buffer == '':
                    break
                if i == 0:
                    print('Início da execução!\n')
                i = 1
                for campo in campos:
                    if (campo != ''):
                    # para cada item na lista campos, ele vai mostrar na tela
                        print(f'CAMPO #{i}: {campo}')
                        i += 1
                        if i == 7:
                            print('')
        print('\nFim da execução!')
    except FileNotFoundError:
        print(f'O arquivo {nomeArq} não foi encontrado.')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()