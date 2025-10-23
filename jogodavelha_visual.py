import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Ex64 - Jogo da Velha")
janela.configure(bg="#f0f0f0")

# Variáveis globais
x_score = 0
o_score = 0
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]
current_theme = "light"  # Tema inicial: light

# Labels para o placar
score_x_label = tk.Label(janela, text="X: 0", font=("Helvetica", 14), bg="#e0e0e0", fg="#004d99")
score_x_label.grid(row=0, column=0, columnspan=3, pady=10)

score_o_label = tk.Label(janela, text="O: 0", font=("Helvetica", 14), bg="#e0e0e0", fg="#004d99")
score_o_label.grid(row=0, column=3, columnspan=3, pady=10)

def handle_click(row, col):
    global current_player, x_score, o_score
    if buttons[row][col]['text'] == "" and not check_win():
        buttons[row][col].config(text=current_player)
        if check_win():
            messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
            if current_player == "X":
                x_score += 1
                score_x_label.config(text=f"X: {x_score}")
            else:
                o_score += 1
                score_o_label.config(text=f"O: {o_score}")
        elif all(buttons[r][c]['text'] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Fim de Jogo", "Empate!")
        current_player = "O" if current_player == "X" else "X"

def check_win():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    return False

def restart_game():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="")

def reset_scores():
    global x_score, o_score
    x_score = 0
    o_score = 0
    score_x_label.config(text="X: 0")
    score_o_label.config(text="O: 0")
    restart_game()

def show_credits():
    messagebox.showinfo("Créditos", "Desenvolvido por Enzo, Turma 18, para fins educacionais.")

def toggle_theme():
    global current_theme
    if current_theme == "light":
        # Alterna para tema escuro
        janela.configure(bg="#333333")
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="#555555", fg="white")
        score_x_label.config(bg="#333333", fg="white")
        score_o_label.config(bg="#333333", fg="white")
        restart_button.config(bg="#555555", fg="white")
        reset_score_button.config(bg="#555555", fg="white")
        credits_button.config(bg="#555555", fg="white")
        mudar_tema_button.config(bg="#555555", fg="white")  # Atualiza o próprio botão
        current_theme = "dark"
    else:
        # Alterna para tema claro
        janela.configure(bg="#f0f0f0")
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="#ffffff", fg="#004d99")
        score_x_label.config(bg="#e0e0e0", fg="#004d99")
        score_o_label.config(bg="#e0e0e0", fg="#004d99")
        restart_button.config(bg="#e0e0e0", fg="#004d99")
        reset_score_button.config(bg="#e0e0e0", fg="#004d99")
        credits_button.config(bg="#e0e0e0", fg="#004d99")
        mudar_tema_button.config(bg="#e0e0e0", fg="#004d99")  # Atualiza o próprio botão
        current_theme = "light"

# Criando os botões do tabuleiro
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(janela, text="", font=("Helvetica", 32), width=5, height=2, bg="#ffffff", fg="#004d99", command=lambda row=r, col=c: handle_click(row, col))
        buttons[r][c].grid(row=r+1, column=c, padx=5, pady=5)

# Botões de controle
restart_button = tk.Button(janela, text="Reiniciar Partida", font=("Helvetica", 14), bg="#e0e0e0", fg="#004d99", command=restart_game)
restart_button.grid(row=4, column=0, columnspan=1, pady=10)

reset_score_button = tk.Button(janela, text="Zerar Placar", font=("Helvetica", 14), bg="#e0e0e0", fg="#004d99", command=reset_scores)
reset_score_button.grid(row=4, column=1, columnspan=1, pady=10)

credits_button = tk.Button(janela, text="Créditos", font=("Helvetica", 14), bg="#e0e0e0", fg="#004d99", command=show_credits)
credits_button.grid(row=4, column=2, columnspan=1, pady=10)

# Novo botão: Mudar Tema
mudar_tema_button = tk.Button(janela, text="Mudar Tema", font=("Helvetica", 14), bg="#e0e0e0", fg="#004d99", command=toggle_theme)
mudar_tema_button.grid(row=5, column=1, pady=10)  # Colocado na linha 5, coluna 1 para centralização

janela.mainloop()

