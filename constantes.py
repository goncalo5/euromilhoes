import math

L = 600  # largura
H = 600  # altura

# tela (numbers e stars)
L_TELA = 180  # largura
TELA_BG = 'white'
TELA_FG = 'red'

N_BOLAS_RET = 5  # numero de bolas tiradas
N_EST_RET = 2  # numero de estrelas tiradas

DINHEIRO_POR_PREMIO = \
    [72000000, 536000, 120000, 4500, 220, 100, 72, 23, 15, 11, 12, 8, 3.5]
PREMIOS_BOLA_EST = \
    [[5, 2], [5, 1], [5, 0], [4, 2], [4, 1], [4, 0], [3, 2],
     [2, 2], [3, 1], [3, 0], [1, 2], [2, 1], [2, 0]]

# positions
TELA_POSX0 = 0
TELA_POSY0 = 0
TELA_POSX = TELA_POSX0 + L_TELA

# numbers
MARGEM = 2
NUM_I, NUM_F = 1, 50  # number inicial e final incluindo
N_NUM = NUM_F - NUM_I + 1  # number of numbers(+1 por estarem incluindos)
NUM_POR_FILA = 6
NUM_POR_COLUNA = int(math.ceil(N_NUM*1. / NUM_POR_FILA))
# quadradinhos
NUM_Q_TAM = L_TELA / NUM_POR_FILA - MARGEM
E_N = NUM_Q_TAM + MARGEM  # espacamento entre numeros
NUM_Q_POSX = TELA_POSX0 + MARGEM
NUM_Q_POSY = TELA_POSY0 + MARGEM
# numeros
NUM_POSX = TELA_POSX0 + NUM_Q_TAM / 2 + MARGEM
NUM_POSY = TELA_POSY0 + NUM_Q_TAM / 2 + MARGEM
NUM_FONT = {'font': ('Comic Sans MS', NUM_Q_TAM/2)}

TELA_POSY_MED = TELA_POSY0 + NUM_POR_COLUNA * E_N + 20

# estrelas
EST_I, EST_F = 1, 11  # numero inicial e final incluindo
N_EST = EST_F - EST_I + 1  # numero de numeros(+1 por estarem incluindos)
EST_POR_FILA = 3
EST_POR_COLUNA = int(math.ceil(N_EST*1. / EST_POR_FILA))
# quadradinhos
E_E = (L_TELA + 1) / (2 * EST_POR_FILA)  # espacamento entre estrelas = tamanho dum quadrado
EST_Q_POSX = TELA_POSX0 + E_E/2
EST_Q_POSY = TELA_POSY_MED
# numeros
EST_POSX = EST_Q_POSX + E_E / 2
EST_POSY = EST_Q_POSY + E_E / 2
EST_FONT = {'font': ('Comic Sans MS', E_E/2)}

TELA_POSY = TELA_POSY_MED + EST_POR_COLUNA * 2 * E_E
H_TELA = TELA_POSY - TELA_POSY0
