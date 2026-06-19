# Desenvolvimento

O projeto "Jogo da Discórdia" foi significativamente refatorado para uma arquitetura Model-View-Controller (MVC), incorporando uma Interface Gráfica de Usuário (GUI) desenvolvida com customtkinter. Essa abordagem separa claramente as responsabilidades:

•
Model (JogoModel.py): Gerencia os dados e o estado do jogo.

•
Controller (JogoController.py): Contém a lógica de negócio, validações e orquestra as interações entre o Modelo e a Visão.

•
View (main_app.py - classes App, TelaMenu, TelaJogo, TelaFim): Responsável pela apresentação visual e interação com o usuário.

Estrutura do Código

O código é agora composto por três módulos Python principais:

•
JogoModel.py: Contém os dados do jogo (jogadores, perguntas, rodada atual, etc.) e funções básicas de registro.

•
JogoController.py: Contém a lógica de negócio, validações e o fluxo do jogo, interagindo com o JogoModel.py.

•
main_app.py: Contém a implementação da GUI, definindo as telas e a forma como o usuário interage com o jogo.

Módulos Utilizados

•
random: Utilizado para selecionar aleatoriamente as perguntas do jogo.

•
os: (Assumido, mas não presente no código fornecido) Utilizado para interagir com o sistema operacional, especificamente para limpar a tela do console (os.system(\'cls\' if os.name == \'nt\' else \'clear\')).

•
tkinter: Módulo padrão do Python para GUI, utilizado indiretamente pelo customtkinter e para messagebox.

•
customtkinter: Biblioteca para criar GUIs modernas e personalizáveis.

•
PIL (Pillow): Biblioteca para manipulação de imagens, utilizada para carregar a imagem da coroa na tela final.

JogoModel.py

Este módulo atua como o modelo de dados do jogo, armazenando o estado atual e as informações essenciais.

Variáveis Globais:

•
rodada_atual: Inteiro que indica a rodada atual do jogo, inicializado em 1.

•
indice_jogador_atual: Inteiro que rastreia o índice do jogador que deve agir no turno atual, inicializado em 0.

•
jogadores: Dicionário onde as chaves são os nomes dos jogadores e os valores são suas pontuações, inicializado vazio.

•
nmr_rodadas: Inteiro que armazena o número total de rodadas configuradas para o jogo, inicializado em 0.

•
perguntas: Lista de strings contendo todas as perguntas possíveis para o jogo da discórdia.

## Funções:

•
registrar(jogador, pergunta, alvo):

•
Esta função, conforme o código fornecido, parece ser um placeholder ou uma função incompleta. Atualmente, ela inicializa a pontuação de um jogador para 0 no dicionário jogadores e imprime o dicionário. Para um registro completo de votos, ela precisaria de lógica adicional para associar a pergunta e o alvo ao jogador e atualizar a pontuação de forma adequada. No contexto da GUI, a atualização da pontuação é feita diretamente no JogoController (model.jogadores[alvo] += 1).



## JogoController.py

Este módulo contém a lógica de controle do jogo, orquestrando as interações e as regras, e interagindo com o JogoModel.py.

Funções:

•
validar_jogador(nome):

•
Recebe o nome de um jogador.

•
Verifica se o nome não está vazio.

•
Se válido, adiciona o jogador ao model.jogadores com pontuação 0.

•
Retorna um dicionário indicando sucesso ou erro e uma mensagem.



•
validar_numeros(rodadas):

•
Recebe o número de rodadas como string.

•
Verifica se há pelo menos 2 jogadores já registrados.

•
Verifica se rodadas é um número válido e maior que zero.

•
Se válido, armazena o número de rodadas em model.nmr_rodadas.

•
Retorna um dicionário indicando sucesso ou erro e uma mensagem.



•
sortear_pergunta():

•
Seleciona e retorna uma pergunta aleatória da lista model.perguntas.



•
proxima_pergunta():

•
Similar a sortear_pergunta(), seleciona e retorna uma nova pergunta aleatória.



•
jogador_atual():

•
Retorna o nome do jogador que deve agir no turno atual, com base em model.indice_jogador_atual.



•
proximo_turno():

•
Incrementa model.indice_jogador_atual para avançar para o próximo jogador.

•
Se todos os jogadores votaram na rodada, incrementa model.rodada_atual e reinicia model.indice_jogador_atual.

•
Verifica se o jogo terminou (se model.rodada_atual excedeu model.nmr_rodadas).

•
Retorna um dicionário contendo o status do jogo (fim), a próxima pergunta, o jogador do próximo turno e a rodada atual.



•
obter_vencedor():

•
Determina e retorna o jogador com a maior pontuação no dicionário model.jogadores.

•
Retorna um dicionário com o status de sucesso, o nome do jogador vencedor e seus votos (pontuação).



main_app.py (Módulo da GUI)

Este módulo é a camada de Visão, responsável por toda a interface gráfica e a interação direta com o usuário. Ele importa JogoController (como ct) e JogoModel (como model) para interagir com a lógica e os dados do jogo.

## Classes:

•
App(ctk.CTk):

•
Classe principal da aplicação GUI, herda de customtkinter.CTk.

•
Configura a janela principal (título, geometria, cor de fundo).

•
Cria um frame_principal para conter as diferentes telas do jogo.

•
Inicializa um dicionário self.frames para gerenciar as instâncias das telas (TelaMenu, TelaJogo, TelaFim).

•
Instancia cada tela e as posiciona no frame_principal.

•
Define o método mostrar_frame(nome_do_frame) para alternar entre as telas.

•
Inicia mostrando a TelaMenu.



•
TelaMenu(ctk.CTkFrame):

•
Representa a tela inicial de configuração de jogadores e rodadas.

•
Contém campos de entrada (CTkEntry) para o nome do jogador e o número de rodadas.

•
Botões (CTkButton) para adicionar jogadores (clicar_adicionar) e iniciar o jogo (clicar_iniciar).

•
Os métodos clicar_adicionar e clicar_iniciar chamam funções do JogoController para validação e manipulação dos dados do jogo, e atualizam a GUI ou trocam de tela conforme necessário.



•
TelaJogo(ctk.CTkFrame):

•
Representa a tela onde as rodadas do jogo acontecem.

•
Exibe a pergunta atual, a rodada e o jogador da vez usando CTkLabel.

•
Possui campos de entrada (CTkEntry) para o alvo do voto e a justificativa.

•
Um botão (CTkButton) bt_justificar que, ao ser clicado, chama o método justificar.

•
O método justificar valida as entradas, atualiza a pontuação no JogoModel (via JogoController), e avança o turno ou finaliza o jogo, alternando para a TelaFim.



•
TelaFim(ctk.CTkFrame):

•
Representa a tela final que exibe o resultado do jogo.

•
Mostra uma imagem de coroa, o nome do vencedor e uma mensagem descritiva usando CTkLabel.

•
Um botão (CTkButton) botao_reiniciar que, ao ser clicado, chama o método reiniciar_jogo (não fornecido no snippet, mas esperado para resetar o estado do jogo e voltar à TelaMenu).

•
O método atualizar_resultado obtém o vencedor do JogoController e atualiza os labels da tela.



Fluxo de Execução

1.
O script main_app.py é executado.

2.
Uma instância da classe App é criada e a janela principal é configurada.

3.
A TelaMenu é exibida, permitindo a configuração inicial.

4.
Jogadores são adicionados e o número de rodadas é definido. As validações são feitas pelo JogoController.

5.
Ao clicar em "Iniciar o CAOS", o jogo transiciona para a TelaJogo.

6.
Na TelaJogo, os jogadores votam e justificam. A lógica de avanço de turno e rodada é gerenciada pelo JogoController.

7.
Ao final das rodadas, o jogo transiciona para a TelaFim.

8.
Na TelaFim, o vencedor é exibido, e o usuário pode optar por reiniciar o jogo.

