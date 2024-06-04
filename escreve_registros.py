def main():
    nomeArq = input('Digite o nome do arquivo: ')
    try:
        ## abre o arquivo com função de escrita binária
        with open(nomeArq, 'wb') as file:
            sobrenome = input('Digite o sobrenome: ')
            registro = ''
            ## enquanto o sobrenome não for uma string vazia
            while sobrenome:

                nome = input('Digite seu nome (ex: Aroldo):\n>>> ')
                endereco = input('Digite seu endereço (ex: Av. Brasil):\n>>> ')
                cidade = input('Digite a sua cidade (ex: São Paulo):\n>>> ')
                estado = input('Digite o seu estado (ex: DF):\n>>> ')
                cep = input('Digite o seu CEP (ex: 12345-678):\n>>> ')

                ## organização das letras
                sobrenome = sobrenome.capitalize() 
                nome = nome.capitalize()
                endereco = endereco.title()
                cidade = cidade.title()
                estado = estado.upper()
                ## fim organização
                
                registro = sobrenome+'|'+nome+'|'+endereco+'|'+cidade+'|'+estado+'|'+cep+'|' ##buffer
                registro = registro.encode() ## codifica para binário
                tam = len(registro)
                tam = tam.to_bytes(2) ## armazena em bytes o tamanho da string
                file.write(tam)
                file.write(registro)

                sobrenome = input('Digite o sobrenome ou pressione <ENTER> para finalizar:\n>>> ') ## recebe o sobrenome

    except FileNotFoundError:
        print(f'Erro ao abrir o arquivo {nomeArq} em modo de escrita, verifique por favor se ele existe ou se o nome está correto!')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()
