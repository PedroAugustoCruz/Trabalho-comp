import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from dados import *
class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cientistas Brasileiras")
        self.geometry("800x600")

        tk.Label(self, text="Nome:").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(self, text="Área de Pesquisa:").grid(row=1, column=0)
        self.entry_area = tk.Entry(self)
        self.entry_area.grid(row=1, column=1)

        tk.Label(self, text="Instituição:").grid(row=2, column=0)
        self.entry_instituicao = tk.Entry(self)
        self.entry_instituicao.grid(row=2, column=1)

        tk.Button(self, text="Buscar", command=self.buscar).grid(row=3, column=0, columnspan=2)

        self.tree = ttk.Treeview(self, columns=("Nome", "Área", "Instituição"), show='headings')
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Área", text="Área")
        self.tree.heading("Instituição", text="Instituição")
        self.tree.bind("<<TreeviewSelect>>", self.mostrar_informacoes)
        self.tree.grid(row=4, column=0, columnspan=3)

        self.foto_label = tk.Label(self)
        self.foto_label.grid(row=5, column=0)
        self.resumo_label = tk.Label(self, text="", wraplength=400)
        self.resumo_label.grid(row=5, column=1)

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=6, column=0, columnspan=3)

    def buscar(self):
        nome = self.entry_nome.get()
        area = self.entry_area.get()
        instituicao = self.entry_instituicao.get()

        resultados = self.filtrar_dados(nome, area, instituicao)

        for item in self.tree.get_children():
            self.tree.delete(item)
        for resultado in resultados:
            self.tree.insert("", "end", values=resultado[:3])

    def mostrar_informacoes(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            valores = item["values"]

            nome, area, instituicao = valores

            caminho_foto = "caminho_para_imagem.png" 
            imagem = Image.open(caminho_foto)
            imagem = imagem.resize((150, 150), Image.ANTIALIAS)
            foto = ImageTk.PhotoImage(imagem)
            self.foto_label.config(image=foto)
            self.foto_label.image = foto

            resumo = "Texto do resumo do cientista selecionado."
            self.resumo_label.config(text=resumo)

    def salvar(self):
        with open("dados_selecionados.txt", "w") as f:
            f.write("Nome, Área, Instituição, Resumo...\n")  
        messagebox.showinfo("Salvar", "Dados salvos com sucesso!")

    def filtrar_dados(self, nome, area, instituicao):
        filtro_nome = nome.lower() in dados_cientistas[:, 0].astype(str).lower()
        filtro_area = area.lower() in dados_cientistas[:, 1].astype(str).lower()
        filtro_instituicao = instituicao.lower() in dados_cientistas[:, 2].astype(str).lower()

        resultados = dados_cientistas[(filtro_nome) & (filtro_area) & (filtro_instituicao)]
        return resultados

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
