import os

restaurantes = [
      {'nome':'Páprica','categoria':'Caseira','ativo':False},
      {'nome':'Tempero Caseiro','categoria':'Buffet Livre','ativo':True},
      {'nome':'Sushin\'Roll','categoria':'Japonesa','ativo':False}
]

def exibir_nome_do_programa():
      ''' Esta função é responsável por exibir o título do programa.'''

      print('''
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      \n\n''')

def finalizar_app():
    ''' Limpa o terminal e exibe ao usuário que o programa está sendo encerrado'''

    os.system('cls')
    print('Encerrando o programa...\n')

def voltar_ao_menu_principal():
      ''' Indica ao usuário para voltar ao menu principal
      
      Outputs:
      - Retorna ao menu principal
      '''
      input('\nAperte qualquer tecla para voltar ao menu principal...')
      main()

def alternar_estado_restaurante():
      ''' Ativa ou desativa um restaurante.
      
      Inputs:
      - Nome do Restaurante

      Outputs:
      - Exibe o sucesso da alteração
      - Exibe se o restaurante não foi encontrado
      '''
      exibir_subtitulo('Alterando estado do restaurante')
      nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
      restaurante_encontrado = False
      for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                  restaurante_encontrado = True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restauranten {nome_restaurante} foi desativado com sucesso'
                  print(mensagem)
      if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
      voltar_ao_menu_principal()

def listar_restaurantes():
      ''' Exibe todos os restaurantes cadastrados.
      
      Outputs:
      - Exibe a lista de restaurantes na tela
      '''

      exibir_subtitulo('Listando restaurantes')
      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
      voltar_ao_menu_principal()

def exibir_opcoes():
      ''' Exibir ao usuário as opções disponíveis'''

      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado do restaurante')
      print('4. Sair\n')

def opcao_invalida():
      ''' Mostra ao usuário que a opção digitada está incorreta
      
      Outputs:
      -  Retorna ao menu principal
      '''

      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      ''' Exibe um subtítulo estilizado na tela.
      
      Inputs:
      - texto: str - O texto do subtítulo
      '''
      os.system('cls')
      linha = '-' * (len(texto) + 4)
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      ''' Essa função é responsável por cadastrar um novo restaurante.
       
      Inputs:
      - Nome do restaurante
      - Categoria

      Outputs:
      - Adiciona um novo restaurante à lista de restaurantes
      
      '''

      
      exibir_subtitulo('Cadastro de novos restaurante')
      nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
      categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
      dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
      voltar_ao_menu_principal()

def escolher_opcao():
      ''' Solicita  e executa a opção escolhida pelo usuário
      
      Outputs:
      - Executa a opção escolhida pelo usuário
      '''
      try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            match opcao_escolhida:
                  case 1:
                        print('Cadastrar restaurante')
                        cadastrar_novo_restaurante()
                  case 2:
                        listar_restaurantes()
                  case 3:
                        alternar_estado_restaurante()
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()
      except:
            opcao_invalida()

def main():
    ''' Função principal que inicia o programa.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()