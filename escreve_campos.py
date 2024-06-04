def main():
    nomeArq = input('Digite o nome do arquivo: ') ## abre o arquivo
    try: ## recebe try e o with para abrir o arquivo
        with open(nomeArq, 'w', encoding='utf-8') as file: ## abre o arquivo com função de escrita
            sobrenome = input('Digite o sobrenome:\n>>> ') ## recebe o sobrenome
            while sobrenome: ## enquanto o sobrenome não for uma string vazia
                nome = input('Digite seu nome (ex: Aroldo):\n>>> ')
                endereco = input('Digite seu endereço (ex: Av. Brasil):\n>>> ')
                cidade = input('Digite a sua cidade (ex: São Paulo):\n>>> ')
                estado = input('Digite o seu estado (ex: DF):\n>>> ')
                cep = input('Digite o seu CEP (ex: 12345-678):\n>>> ')

                ##organização:
                sobrenome = sobrenome.capitalize() ## Uppercase na primeira letra...
                nome = nome.capitalize()
                endereco = endereco.title()
                cidade = cidade.title()
                estado = estado.upper()
                ## fim organização

                file.write(f'{sobrenome}|{nome}|{endereco}|{cidade}|{estado}|{cep}|') ## concatena as informações
                
                sobrenome = input('Digite o sobrenome ou pressione <ENTER> para finalizar:\n>>> ')
    except:
        print(f'Erro!')

# a exemplo da prof, utilizei um iniciador
if __name__ == '__main__':
    main()
