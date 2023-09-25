import random
import os
from time import sleep
from termcolor import cprint, colored


def tutorial():
    os.system('cls')
    cprint("-"*42, "red")
    print(" "*17, colored("2048", "green"), " "*18)
    cprint("-"*42, "red")
    sleep(0.05)
    print("* O objetivo do jogo é alcançar um bloco com a soma de 2048.")
    sleep(0.05)
    print("")
    print("* A cada jogada um novo número é adicionado à tela")
    sleep(0.05)
    print("")
    print("* Se você não somar números suficientes a tela vai")
    sleep(0.05)
    print("  se encher toda e não haverão mais jogadas possíveis.")
    sleep(0.05)
    print("")
    print("* Caso o tabuleiro não tena mais movimento possiveis, você perde.")
    print("  quando fizer um movimento, você moverá todas as peças do "
          "tabuleiro.")
    sleep(0.05)
    print("")
    input(colored("Pressione [Enter] Para Continuar.", "green"))


def color(m):
    if m == 0:
        print(f"|{m:>4}|", end="")
    if m == 2:
        cprint(f"|{m:>4}|", "red", end="")
    if m == 4:
        cprint(f"|{m:>4}|", "blue", end="")
    if m == 8:
        cprint(f"|{m:>4}|", "magenta", end="")
    if m == 16:
        cprint(f"|{m:>4}|", "yellow",  end="")
    if m == 32:
        cprint(f"|{m:>4}|", "green",  end="")
    if m == 64:
        cprint(f"|{m:>4}|", "cyan",  end="")
    if m == 128:
        cprint(f"|{m:>4}|", "red",  end="")
    if m == 256:
        cprint(f"|{m:>4}|", "blue",  end="")
    if m == 512:
        cprint(f"|{m:>4}|", "magenta",  end="")
    if m == 1024:
        cprint(f"|{m:>4}|", "yellow",  end="")
    if m == 2048:
        cprint(f"|{m:>4}|", "green",  end="")


def exibir_matriz(m):
    os.system('cls')
    cprint("-"*42, "red")
    print(" "*17, colored("2048", "green"), " "*18)
    cprint("-"*42, "red")
    print(7*" ", f"Recorde: {RECORD_SCORE} / Movimentos: {RECORD_MOVIMENTOS}")
    print("_"*24)
    color(m[0][0])
    color(m[0][1])
    color(m[0][2])
    color(m[0][3])
    print(3*" ", "Pontuação:", SCORE)
    print("-"*24, 2*" ", "Movimentos:", NUMERO_MOVIMENTOS)
    color(m[1][0])
    color(m[1][1])
    color(m[1][2])
    color(m[1][3])
    print("")
    print("-"*24, 3*" ", "Cima     [W]")
    color(m[2][0])
    color(m[2][1])
    color(m[2][2])
    color(m[2][3])
    print(4*" ", "Esquerda [A]")
    print("-"*24, 3*" ", "Direita  [D]")
    color(m[3][0])
    color(m[3][1])
    color(m[3][2])
    color(m[3][3])
    print(4*" ", "Baixo    [S]")
    print("¯"*24)


def verificar_jogada(m):
    tem_jogadas: bool = False
    for i in range(0, 4):
        if m[i][0] == m[i][1]:
            tem_jogadas = True
        elif m[i][1] == m[i][2]:
            tem_jogadas = True
        elif m[i][2] == m[i][3]:
            tem_jogadas = True
        elif m[0][i] == m[1][i]:
            tem_jogadas = True
        elif m[1][i] == m[2][i]:
            tem_jogadas = True
        elif m[2][i] == m[3][i]:
            tem_jogadas = True
    for i in range(0, 4):
        for j in range(0, 4):
            if m[i][j] == 0:
                tem_jogadas = True
    return tem_jogadas


def inserir_random(m):
    onde_tem_zero = []
    for i in range(0, 4):
        for j in range(0, 4):
            if m[i][j] == 0:
                onde_tem_zero.append([i, j])
    lugar_aleatorio = random.choice(onde_tem_zero)
    m[lugar_aleatorio[0]][lugar_aleatorio[1]] = random.choice([2, 4])
    print(onde_tem_zero)
    return m


def aleatorios_iniciais(m):
    onde_tem_zero = []
    for i in range(0, 4):
        for j in range(0, 4):
            if m[i][j] == 0:
                onde_tem_zero.append([i, j])
    lugar_aleatorio = random.sample(onde_tem_zero, 2)
    m[lugar_aleatorio[0][0]][lugar_aleatorio[0][1]] = random.randrange(2, 5, 2)
    m[lugar_aleatorio[1][0]][lugar_aleatorio[1][1]] = random.randrange(2, 5, 2)
    print(onde_tem_zero)
    return m


def somar_matriz(m, movimento, pontos):
    if movimento.upper() == "W":
        for i in range(0, 4):
            if m[0][i] == m[1][i]:
                m[0][i] = m[0][i] + m[1][i]
                pontos += m[0][i]
                m[1][i] = 0
            if m[1][i] == m[2][i]:
                m[1][i] = m[1][i] + m[2][i]
                pontos += m[1][i]
                m[2][i] = 0
            if m[2][i] == m[3][i]:
                m[2][i] = m[2][i] + m[3][i]
                pontos += m[2][i]
                m[3][i] = 0
    elif movimento.upper() == "S":
        for i in range(0, 4):
            if m[3][i] == m[2][i]:
                m[3][i] = m[3][i] + m[2][i]
                pontos += m[3][i]
                m[2][i] = 0
            if m[2][i] == m[1][i]:
                m[2][i] = m[2][i] + m[1][i]
                pontos += m[2][i]
                m[1][i] = 0
            if m[1][i] == m[0][i]:
                m[1][i] = m[1][i] + m[0][i]
                pontos += m[1][i]
                m[0][i] = 0
    elif movimento.upper() == "A":
        for i in range(0, 4):
            if m[i][0] == m[i][1]:
                m[i][0] = m[i][0] + m[i][1]
                pontos += m[i][0]
                m[i][1] = 0
            if m[i][1] == m[i][2]:
                m[i][1] = m[i][1] + m[i][2]
                pontos += m[i][1]
                m[i][2] = 0
            if m[i][2] == m[i][3]:
                m[i][2] = m[i][2] + m[i][3]
                pontos += m[i][2]
                m[i][3] = 0
    elif movimento.upper() == "D":
        for i in range(0, 4):
            if m[i][3] == m[i][2]:
                m[i][3] = m[i][3] + m[i][2]
                pontos += m[i][3]
                m[i][2] = 0
            if m[i][2] == m[i][1]:
                m[i][2] = m[i][2] + m[i][1]
                pontos += m[i][2]
                m[i][1] = 0
            if m[i][1] == m[i][0]:
                m[i][1] = m[i][1] + m[i][0]
                pontos += m[i][1]
                m[i][0] = 0
    return m, pontos


def mover_matriz(m, movimento):
    if movimento.upper() == "W":
        for j in range(0, 4):
            for i in range(0, 4):
                if m[0][i] == 0:
                    m[0][i] = m[1][i]
                    m[1][i] = 0
                if m[1][i] == 0:
                    m[1][i] = m[2][i]
                    m[2][i] = 0
                if m[2][i] == 0:
                    m[2][i] = m[3][i]
                    m[3][i] = 0
    elif movimento.upper() == "S":
        for j in range(0, 4):
            for i in range(0, 4):
                if m[3][i] == 0:
                    m[3][i] = m[2][i]
                    m[2][i] = 0
                if m[2][i] == 0:
                    m[2][i] = m[1][i]
                    m[1][i] = 0
                if m[1][i] == 0:
                    m[1][i] = m[0][i]
                    m[0][i] = 0
    elif movimento.upper() == "A":
        for j in range(0, 4):
            for i in range(0, 4):
                if m[i][0] == 0:
                    m[i][0] = m[i][1]
                    m[i][1] = 0
                if m[i][1] == 0:
                    m[i][1] = m[i][2]
                    m[i][2] = 0
                if m[i][2] == 0:
                    m[i][2] = m[i][3]
                    m[i][3] = 0
    elif movimento.upper() == "D":
        for j in range(0, 4):
            for i in range(0, 4):
                if m[i][3] == 0:
                    m[i][3] = m[i][2]
                    m[i][2] = 0
                if m[i][2] == 0:
                    m[i][2] = m[i][1]
                    m[i][1] = 0
                if m[i][1] == 0:
                    m[i][1] = m[i][0]
                    m[i][0] = 0
    return m


FIM_DE_JOGO: bool = False
VENCEU_O_JOGO: bool = False
CONTINUAR_JOGANDO: bool = True
SCORE: int = 0
RECORD_SCORE: int = 0
NUMERO_MOVIMENTOS: int = 0
RECORD_MOVIMENTOS: int = 0
tutorial()
while CONTINUAR_JOGANDO is True:
    matriz = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    matriz = aleatorios_iniciais(matriz)
    exibir_matriz(matriz)
    SCORE = 0
    NUMERO_MOVIMENTOS = 0
    while FIM_DE_JOGO is False:
        exibir_matriz(matriz)
        if verificar_jogada(matriz) is True:
            while True:
                os.system('cls')
                exibir_matriz(matriz)
                escolha_de_movimento = input(colored("Movimento: ", "green"))
                if escolha_de_movimento.upper() == "A":
                    break
                if escolha_de_movimento.upper() == "S":
                    break
                if escolha_de_movimento.upper() == "D":
                    break
                if escolha_de_movimento.upper() == "W":
                    break
            mover_matriz(matriz, escolha_de_movimento)
            matriz, SCORE = somar_matriz(matriz, escolha_de_movimento, SCORE)
            mover_matriz(matriz, escolha_de_movimento)
            NUMERO_MOVIMENTOS += 1
            for x in range(0, 4):
                for y in range(0, 4):
                    if matriz[x][y] == 2048:
                        VENCEU_O_JOGO = True
                        FIM_DE_JOGO = True
            matriz = inserir_random(matriz)
        else:
            FIM_DE_JOGO = True
    if VENCEU_O_JOGO is True:
        exibir_matriz(matriz)
        print("Parabéns, você venceu o jogo!")
    else:
        print("Você perdeu!")
    escolha_continuar = input("Deseja continuar jogando? [S/N]: ")
    if escolha_continuar.upper() == "S":
        if SCORE > RECORD_SCORE:
            RECORD_SCORE = SCORE
            RECORD_MOVIMENTOS = NUMERO_MOVIMENTOS
        if SCORE == RECORD_SCORE:
            if NUMERO_MOVIMENTOS > RECORD_MOVIMENTOS:
                RECORD_SCORE = SCORE
                RECORD_MOVIMENTOS = NUMERO_MOVIMENTOS
        VENCEU_O_JOGO = False
        CONTINUAR_JOGANDO = True
        FIM_DE_JOGO = False
    elif escolha_continuar.upper() == "N":
        CONTINUAR_JOGANDO = False
