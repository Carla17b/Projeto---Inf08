# Estruturas de Pastas e Arquivos

O projeto "Jogo da Discórdia" agora adota uma estrutura de arquivos modular, seguindo o padrão Model-View-Controller (MVC), com a adição de uma interface gráfica de usuário (GUI). A organização dos arquivos é a seguinte:

Plain Text


/projeto_jogo_da_discordia/
├── JogoModel.py
├── JogoController.py
├── main_app.py
├── dark_crown.png
└── README.md (Opcional, para informações gerais do projeto)



•
JogoModel.py: Este arquivo contém o modelo de dados do jogo, incluindo variáveis de estado (como rodada_atual, indice_jogador_atual, jogadores, nmr_rodadas) e a lista de perguntas. Ele é responsável por manter o estado do jogo.

•
JogoController.py: Este arquivo atua como o controlador, contendo a lógica de negócio do jogo. Ele interage com o JogoModel.py para manipular os dados e implementa funções como validar_jogador, validar_numeros, sortear_pergunta, proximo_turno e obter_vencedor.

•
main_app.py: Este é o arquivo principal da aplicação GUI (View). Ele define a estrutura da interface gráfica usando customtkinter, incluindo as classes App, TelaMenu, TelaJogo e TelaFim. Este módulo importa e utiliza as funções do JogoController.py para interagir com a lógica do jogo e atualizar a interface.

•
dark_crown.png: Um arquivo de imagem utilizado pela TelaFim para exibir um ícone visual do vencedor.

Esta estrutura modular facilita a compreensão, manutenção e futuras expansões do projeto, permitindo que cada componente seja desenvolvido e testado de forma mais independente.


