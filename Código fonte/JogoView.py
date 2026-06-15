import ttkbootstrap as tb

#cria a classe principal
class App(tb.Window):
	#função de inicialização
	def __init__(self):
		#iniciando a janela usando o tema darkly
		super().__init__(themename='darkly',title='Jogo Da Discordia')
		self.geometry('1024x576')
		
		#criando o primeiro frame
		frame_principal = tb.Frame(self,bootstyle='primary')
		frame_principal.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)
		#cria uma lista que vai guardar os nomes das classes que vamos criar ainda, que no caso são as telas propriamente ditas
		self.frames = {}
		
		#Esse loop vai criar um frame em cima do outro
		for f in (TelaMenu,TelaJogo):
			frame = f(parent=frame_principal,controller=self)
			self.frames[f] = frame
			
			frame.place(relx=0.1,rely=0.2)
			
		self.mostrar_frame(TelaMenu)
	
	#função que puxa um frame pra frente	
	def mostrar_frame(self,nome_do_frame):
			frame = self.frames[nome_do_frame]
			frame.tkraise()
			
class TelaMenu(tb.Frame):
	#função de inicialização
	def __init__(self,parent,controller):
		super().__init__(parent)

		#criando as labels
		label_1 = tb.Label(self,text='Label em contrução')
		label_1.place(relx=0.5,rely=0.5)

		bt_1 = tb.Button(self,text='Botão em contrução',command = lambda:controller.mostrar_frame(TelaJogo),bootstyle='secondary')
		bt_1.place(relx=0.5,rely=0.8)
		
class TelaJogo(tb.Frame):
	#função de inicialização
	def __init__(self,parent,controller):
		super().__init__(parent)
		
		#criando as labels
		label_1 = tb.Label(self,text='Label em contrução 2')
		label_1.place(relx=0.5,rely=0.5)
		
		bt_1 = tb.Button(self,text='Botão em contrução 2',command = lambda:controller.mostrar_frame(TelaMenu))
		bt_1.place(relx=0.5,rely=0.8)
		
if __name__ == '__main__':
	app = App()
	
	app.mainloop()
