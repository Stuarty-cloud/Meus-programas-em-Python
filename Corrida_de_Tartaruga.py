import tkinter as tk
from tkinter import messagebox
import turtle
import random

class CorridaTartarugas:
    def __init__(self, root):
        self.root = root
        self.root.title("🐢 Corrida de Tartarugas")
        self.root.geometry("900x650")

        self.tartarugas = []
        self.correndo = False
        self.posicoes = []
        self.cores_tartarugas = []

        # Título
        titulo = tk.Label(
            root,
            text="🐢 CORRIDA DE TARTARUGAS 🐢",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=10)

        # Área da corrida
        self.canvas = tk.Canvas(root, width=850, height=480)
        self.canvas.pack()

        # Turtle usa o Canvas do tkinter
        self.tela = turtle.TurtleScreen(self.canvas)
        self.tela.bgcolor("lightgreen")

        # Botões
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.botao_iniciar = tk.Button(
            frame,
            text="🏁 INICIAR CORRIDA",
            font=("Arial", 14, "bold"),
            command=self.iniciar_corrida
        )
        self.botao_iniciar.pack(side=tk.LEFT, padx=10)

        self.botao_nova = tk.Button(
            frame,
            text="🔄 NOVA CORRIDA",
            font=("Arial", 14, "bold"),
            command=self.nova_corrida,
            state = tk.DISABLED
        )
        self.botao_nova.pack(side=tk.LEFT, padx=10)

        self.nova_corrida()

    def nova_corrida(self):
        self.correndo = False
        self.botao_iniciar.config(state=tk.DISABLED)
        self.botao_nova.config(state=tk.DISABLED)

        # Limpa tudo
        self.tela.clear()
        self.tartarugas.clear()
        self.posicoes.clear()
        self.cores_tartarugas.clear()

        # Linha de chegada
        linha = turtle.RawTurtle(self.tela)
        linha.hideturtle()
        linha.penup()
        linha.goto(320, 200)
        linha.setheading(270)
        linha.pendown()
        linha.pensize(5)

        for _ in range(10):
            linha.forward(40)
            linha.penup()
            linha.forward(10)
            linha.pendown()

        # Criar tartarugas
        cores = [
            "red",
            "blue",
            "yellow",
            "purple",
            "orange",
            "pink",
            "brown",
            "cyan"
        ]

        y_inicial = 160

        for i, cor in enumerate(cores):
            tartaruga = turtle.RawTurtle(self.tela)
            tartaruga.shape("turtle")
            tartaruga.color(cor)
            tartaruga.penup()

            x = -350
            y = y_inicial - (i * 45)

            tartaruga.goto(x, y)

            self.tartarugas.append(tartaruga)
            self.posicoes.append(x)
            self.cores_tartarugas.append(cor)

            # Nome da tartaruga
            texto = turtle.RawTurtle(self.tela)
            texto.hideturtle()
            texto.penup()
            texto.goto(-410, y - 8)
            texto.write(
                f"{i + 1}",
                font=("Arial", 12, "bold")
            )

        self.botao_iniciar.config(state=tk.NORMAL)

    def iniciar_corrida(self):
        if self.correndo:
            return

        self.correndo = True

        self.botao_iniciar.config(state=tk.DISABLED)
        self.botao_nova.config(state=tk.DISABLED)

        self.correr()

    def correr(self):
        if not self.correndo:
            return

        for i, tartaruga in enumerate(self.tartarugas):

            # Movimento aleatório
            distancia = random.randint(1, 15)

            tartaruga.forward(distancia)

            self.posicoes[i] += distancia

            # Verifica chegada
            if self.posicoes[i] >= 320:
                self.correndo = False

                vencedor = i + 1
                cor_vencedora = self.cores_tartarugas[i]

                messagebox.showinfo(
                    "🏆 FIM DA CORRIDA!",
                    f"🏆 A TARTARUGA {cor_vencedora.upper()} VENCEU!\n\n"
                    f"Parabéns! 🐢"
                )

                self.botao_nova.config(state=tk.NORMAL)

                return

        # Continua a corrida
        self.root.after(50, self.correr)


# Programa principal
root = tk.Tk()

jogo = CorridaTartarugas(root)

root.mainloop()