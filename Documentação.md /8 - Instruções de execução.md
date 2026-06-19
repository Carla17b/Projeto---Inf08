# Instruções de Execução

Para executar o "Jogo da Discórdia" com sua nova interface gráfica, siga os passos abaixo:

Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema. Você pode verificar a versão do Python digitando o seguinte comando no terminal:

Bash


python3 --version



Se o Python 3 não estiver instalado, você pode baixá-lo e instalá-lo a partir do site oficial do Python: https://www.python.org/downloads/

Além do Python, você precisará instalar as bibliotecas customtkinter e Pillow. Você pode instalá-las usando pip:

Bash


pip install customtkinter Pillow



Estrutura de Arquivos

Certifique-se de que os seguintes arquivos estejam na mesma pasta:

•
JogoModel.py

•
JogoController.py

•
main_app.py

•
dark_crown.png (imagem utilizada na tela final)

Executando o Jogo

1.
Abra o Terminal: Navegue até o diretório onde você salvou os arquivos do projeto usando o terminal ou prompt de comando.

2.
Execute o Script Principal: Digite o seguinte comando e pressione Enter:

Bash


python3 main_app.py



•
Observação: Em alguns sistemas, o comando pode ser apenas python em vez de python3.



3.
Interaja com a Interface Gráfica: A janela do jogo será aberta. Siga as instruções na tela para adicionar jogadores, definir o número de rodadas e jogar. A interação será feita através dos elementos da GUI (campos de texto, botões).

Exemplo de interação inicial na GUI:

•
Na Tela de Menu, digite os nomes dos jogadores e clique em "+ Adicionar".

•
Após adicionar todos os jogadores, digite o número de rodadas e clique em "Iniciar o CAOS".

•
Na Tela de Jogo, digite o nome do jogador alvo e a justificativa, e clique em "Justificar Resposta".

•
Na Tela Final, você verá o resultado e poderá clicar em "Reiniciar" para jogar novamente.


