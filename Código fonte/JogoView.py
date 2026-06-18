import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import JogoController as ct
import JogoModel as model
# Configuração global de aparência do CustomTkinter
ctk.set_appearance_mode("Light")  # Força o modo claro, já que o tema original é light
ctk.set_default_color_theme("blue")

# cria a classe principal
class App(ctk.CTk):
    # função de inicialização
    def __init__(self):
        # iniciando a janela
        super().__init__()
        self.title('Entre Amigos e Inimigos')
        self.geometry('1024x576')
        
        # Define a cor de fundo da janela principal (mesmo fundo roxo do tema antigo)
        self.configure(fg_color="#674c82")
        
        # criando o primeiro frame
        frame_principal = ctk.CTkFrame(self, fg_color="transparent") # Fundo transparente para ver o roxo da janela
        frame_principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        # Labels usam text_color para a cor da fonte. Definido para branco para contrastar com o fundo
        label_1 = ctk.CTkLabel(self, text='ENTRE AMIGOS E INIMIGOS', font=('CinzelDecorate', 35, 'bold'), text_color="#ffffff")
        label_1.pack(pady=5)
        
        # cria uma lista que vai guardar os nomes das classes que vamos criar ainda
        self.frames = {}

        # Esse loop vai criar um frame em cima do outro
        for f in (TelaMenu, TelaJogo):
            frame = f(parent=frame_principal, controller=self)
            self.frames[f] = frame
    
            frame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
    
        self.mostrar_frame(TelaMenu)

    # função que puxa um frame pra frente    
    def mostrar_frame(self, nome_do_frame):
        frame = self.frames[nome_do_frame]
        frame.tkraise()
            
class TelaMenu(ctk.CTkFrame):
    # função de inicialização
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent") # Mantém transparente para herdar o fundo

        # Card central branco onde ficam as opções
        frame_menu = ctk.CTkFrame(self, fg_color='#ffffff', corner_radius=30)
        frame_menu.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # criando as labels (text_color adicionado para preto, já que o fundo do frame é branco)
        label_1 = ctk.CTkLabel(frame_menu, text='Quem serão os jogadores', font=('Cinzel', 30, 'bold'), text_color="#000000")
        label_1.place(relx=0.1, rely=0.2)

        label_2 = ctk.CTkLabel(frame_menu, text='De 2 a 15 jogadores', font=('Cinzel', 14, 'bold'), text_color="#343a40")
        label_2.place(relx=0.1, rely=0.3)

        # Container para a caixa de entrada e botão de adicionar
        frame_nomes = ctk.CTkFrame(frame_menu, fg_color='#fefefe', corner_radius=30, border_width=1, border_color="#bfbfbf")
        frame_nomes.place(relx=0.1, rely=0.4, relwidth=0.6, relheight=0.12)

        # Caixa de entrada de texto arredondada
        self.entry_nomes = ctk.CTkEntry(
            frame_nomes, 
            font=('Cinzel', 14,'bold'), 
            fg_color='#948d9c', 
            text_color='#000000', 
            placeholder_text="Nome do jogador...",
            corner_radius=30,
            border_width=0 # Deixa sem borda interna pois o frame externo já tem borda
        )
        self.entry_nomes.place(relx=0.01, rely=0.1, relwidth=0.68, relheight=0.8)

        # Botão "+ Adicionar" customizado com as cores do seu tema
        botao_add = ctk.CTkButton(
            frame_nomes, 
            text='+ Adicionar', 
            font=('Cinzel', 12, 'bold'),
            text_color='#000000',
            fg_color='#948d9c', 
            hover_color='#290b0b',
            corner_radius=30,
            command=self.clicar_adicionar
        )
        botao_add.place(relx=0.7, rely=0.1, relwidth=0.28, relheight=0.8)

        # Botão principal arredondado (estilo cápsula)
        botao_iniciar = ctk.CTkButton(
            frame_menu, 
            text='Iniciar o CAOS', 
            font=('CinzelDecorate', 14, 'bold'),
            corner_radius=30, 
            fg_color='#948d9c', 
            hover_color='#290b0b',
            text_color='#000000',
            command=lambda: controller.mostrar_frame(TelaJogo)
        )
        botao_iniciar.place(relx=0.4, rely=0.6,relwidth=0.3,relheight=0.1)

    def clicar_adicionar(self):

            nome = self.entry_nomes.get()
            
            resultado = ct.validar_jogador(nome)

            if resultado['error']:
                tk.messagebox.showerror('erro',resultado['mensagem'])

            else:
                model.registrar_jogador(nome)

                self.entry_nomes.delete(0,'end')
                

        
class TelaJogo(ctk.CTkFrame):
    # função de inicialização
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")

        # CTkFrame simulando o Labelframe (Cards modernos não usam texto cortando a borda)
        frame_jogo = ctk.CTkFrame(self,
                                  fg_color='#948d9c',
                                  corner_radius=15

                                  )
        frame_jogo.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        
        # Título interno do painel
        #text='TESTE DE FRAMELABEL', font=('Cinzel', 12, 'bold'), text_color="#343a40"
        frame_jogadores = ctk.CTkFrame(frame_jogo,
                                       fg_color='#948d9c',
                                       corner_radius=0
                                       )
        frame_jogadores.place(relx=0.32,rely=0.0,relwidth=0.06,relheight=1.0)
        
        # criando as labels
        label_perguntas = ctk.CTkLabel(frame_jogo,
                                       text='Testar',
                                       font=('Cinzel', 14, 'bold'),
                                       text_color="#000000",
                                       fg_color='#ffffff',
                                       corner_radius=30

                                       )
        label_perguntas.place(relx=0.35,rely=0.1,relwidth=0.6,relheight=0.6)

        ent_justificativa = ctk.CTkEntry(
            frame_jogo,
            font=('Cinzel', 14,'bold'), 
            fg_color='#ffffff', 
            text_color='#000000', 
            placeholder_text="Justifique...",
            corner_radius=30,
            border_width=0 

            )
        ent_justificativa.place(relx=0.45,rely=0.73,relwidth=0.4,relheight=0.1)

        # Botão para voltar à tela anterior também no padrão arredondado
        bt_justificar = ctk.CTkButton(
            frame_jogo, 
            text='Justificar Resposta', 
            font=('Cinzel', 12, 'bold'),
            fg_color='#382947', 
            hover_color='#290b0b',
            corner_radius=30,
            command=lambda: controller.mostrar_frame(TelaMenu)
        )
        bt_justificar.place(relx=0.55,rely=0.85,relwidth=0.2,relheight=0.1)
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
