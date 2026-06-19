# Requisitos Funcionais

•
RF001 - Interface Gráfica: O sistema deve apresentar uma interface gráfica de usuário (GUI) intuitiva para todas as interações do jogo.

•
RF002 - Configuração de Jogadores (GUI): A GUI deve permitir a inserção e validação dos nomes dos jogadores, exibindo feedback visual.

•
RF003 - Configuração de Rodadas (GUI): A GUI deve permitir a definição do número de rodadas, com validação visual da entrada.

•
RF004 - Exibição de Perguntas (GUI): A GUI deve exibir claramente a pergunta atual da rodada.

•
RF005 - Identificação do Jogador Atual (GUI): A GUI deve indicar qual jogador está na vez de votar.

•
RF006 - Entrada de Voto e Justificativa (GUI): A GUI deve fornecer campos para o jogador selecionar o alvo do voto e inserir a justificativa.

•
RF007 - Validação de Voto e Justificativa (GUI): O sistema deve validar o voto e a justificativa através da GUI, exibindo mensagens de erro ou sucesso.

•
RF008 - Avanço de Turno/Rodada (GUI): A GUI deve ser atualizada automaticamente para o próximo turno/rodada após a submissão de um voto válido.

•
RF009 - Exibição de Resultado Final (GUI): A GUI deve apresentar o resultado final do jogo, incluindo o vencedor e sua pontuação, de forma visualmente atraente.

•
RF010 - Reinício do Jogo (GUI): A GUI deve oferecer uma opção para reiniciar o jogo após o término.

•
RF011 - Validação de Jogador (Lógica): O sistema deve validar o nome do jogador, garantindo que não seja vazio, antes de adicioná-lo ao jogo.

•
RF012 - Adição de Jogador (Lógica): O sistema deve permitir adicionar jogadores, inicializando sua pontuação.

•
RF013 - Validação de Início de Jogo (Lógica): O sistema deve garantir que haja pelo menos dois jogadores para iniciar o jogo.

•
RF014 - Validação de Número de Rodadas (Lógica): O sistema deve validar a entrada do número de rodadas, garantindo que seja um número válido e positivo.

•
RF015 - Sorteio de Pergunta (Lógica): O sistema deve sortear aleatoriamente uma pergunta da lista predefinida para cada turno.

•
RF016 - Identificação do Jogador Atual (Lógica): O sistema deve identificar qual jogador é o atual a realizar uma ação (votar).

•
RF017 - Avanço de Turno/Rodada (Lógica): O sistema deve gerenciar o avanço para o próximo jogador e, se todos os jogadores votaram, avançar para a próxima rodada.

•
RF018 - Verificação de Fim de Jogo (Lógica): O sistema deve identificar quando o número total de rodadas foi atingido e sinalizar o fim do jogo.

•
RF019 - Obtenção do Vencedor (Lógica): O sistema deve ser capaz de determinar o jogador com a maior pontuação ao final do jogo.


# Requisitos Não Funcionais

•
RNF001 - Modularidade: O código deve ser estruturado em módulos (JogoModel, JogoController, main_app) para separar as responsabilidades de dados, lógica de controle e interface de usuário (padrão MVC).

•
RNF002 - Usabilidade (GUI): A interface gráfica deve ser intuitiva, responsiva e fácil de usar, proporcionando uma boa experiência ao usuário.

•
RNF003 - Estética (GUI): A GUI deve ter um design visualmente atraente, utilizando customtkinter para um visual moderno.

•
RNF004 - Robustez: O sistema deve lidar com entradas inválidas do usuário (e.g., texto onde se espera número) sem travar a aplicação.

•
RNF005 - Manutenibilidade: A separação de responsabilidades deve facilitar a manutenção e futuras expansões do código.

•
RNF006 - Clareza: As mensagens de erro e sucesso, tanto na lógica quanto na GUI, devem ser claras e informativas.

•
RNF007 - Portabilidade: O jogo deve ser executável em diferentes sistemas operacionais (Windows, Linux, macOS) que suportem Python e as bibliotecas customtkinter e Pillow.



