from Tkinter import *
import random
from constantes import *


class Game(object):
    def __init__(self):
        self.i = Tk()
        self.i.title('Euro Milhoes')
        self.i.geometry('%ix%i' % (L, H))
        self.i.configure(bg='yellow')

        Label(self.i, text="5 Numeros", wraplength=1)\
            .grid(row=0, column=0, rowspan=3)
        Label(self.i, text="+", wraplength=1).grid(row=3, column=0)
        Label(self.i, text="2 Estrelas", wraplength=1)\
            .grid(row=4, column=0, rowspan=2)

        self.canvas = Canvas(self.i, width=L_TELA, height=H_TELA)
        self.canvas.focus_force()
        self.canvas.grid(row=0, column=1, rowspan=6)
        self.canvas.bind('<1>', self.selecionar)

        self.desenhar_numbers()
        self.desenhar_estrelas()
        self.cruzes = []

        Label(self.i, text='Numero de jogos').grid(row=0, column=2)
        self.n_j = Entry(self.i)
        self.n_j.insert(0, '1')
        self.n_j.grid(row=0, column=3)

        self.b_rand = Button(self.i, text='Numeros Aleatorios', command=self.gerar_aleatorios)
        self.b_rand.grid(row=1, column=2)

        self.b_clean = Button(self.i, text='Limpar Numeros', command=self.apagar_cruzes)
        self.b_clean.grid(row=1, column=3)

        self.l_dinheiro_gasto = Label()
        self.l_dinheiro_gasto.grid(row=2, column=2, columnspan=2)
        self.l_dinheiro_ganho = Label()
        self.l_dinheiro_ganho.grid(row=3, column=2, columnspan=2)
        self.l_total_dinheiro_ganho = Label()
        self.l_total_dinheiro_ganho.grid(row=4, column=2, columnspan=2)
        self.l_lucro = Label()
        self.l_lucro.grid(row=5, column=2, columnspan=2)

        self.bolas_iguais = self.est_iguais = None

        self.premios = [0] * 13  # [1 premio, 2 premio, ...]
        self.dinheiro = [0] * 13
        self.dinheiro_gasto = 0

        self.bolas_escolhidas = []
        self.est_escolhidas = []

        self.i.mainloop()

    def gerar_aleatorios(self):
        self.apagar_cruzes()
        self.bolas_escolhidas = sortear(NUM_I, NUM_F, N_BOLAS_RET)
        self.est_escolhidas = sortear(EST_I, EST_F, N_EST_RET)
        for n in self.bolas_escolhidas:
            x, y = encontrar_coord(n, True)
            self.desenhar_cruz(x, y)
        for n in self.est_escolhidas:
            x, y = encontrar_coord(n)
            self.desenhar_cruz(x, y)

        self.premiar()

    def selecionar(self, event):
        # selecionar numeros
        # print event.x/E_N+1 + event.y/E_N*NUM_POR_FILA
        if NUM_I <= event.x/E_N+1 + event.y/E_N*NUM_POR_FILA <= NUM_F:
            b = event.x / E_N + 1 + event.y / E_N * NUM_POR_FILA
            if b not in self.bolas_escolhidas \
                    and len(self.bolas_escolhidas) < N_BOLAS_RET:
                self.desenhar_cruz(event.x, event.y)
                self.bolas_escolhidas.append(b)
        # selecionar estrelas
        # print event.x/(2*E_E)+1 + (event.y-TELA_POSY_MED)/(2*E_E)*EST_POR_FILA
        elif EST_I <= event.x/(2*E_E)+1 + (event.y-TELA_POSY_MED)/(2*E_E)*EST_POR_FILA <= EST_F:
            e = event.x/(2*E_E)+1 + (event.y-TELA_POSY_MED)/(2*E_E)*EST_POR_FILA
            if e not in self.est_escolhidas \
                    and len(self.est_escolhidas) < N_EST_RET:
                self.desenhar_cruz(event.x, event.y)
                self.est_escolhidas.append(e)

        if len(self.bolas_escolhidas) == N_BOLAS_RET \
                and len(self.est_escolhidas) == N_EST_RET:
            self.premiar()

    def premiar(self):
        n = int(self.n_j.get())
        self.dinheiro_gasto += n * 2
        for jogo in range(n):
            self.bolas_iguais = comparar(
                self.bolas_escolhidas, sortear(NUM_I, NUM_F, N_BOLAS_RET))
            self.est_iguais = comparar(
                self.est_escolhidas, sortear(EST_I, EST_F, N_EST_RET))
            for i, (b, e) in enumerate(PREMIOS_BOLA_EST):
                if self.bolas_iguais == b and self.est_iguais == e:
                    self.premios[i] += 1
                    self.dinheiro[i] += DINHEIRO_POR_PREMIO[i]

        self.l_dinheiro_gasto['text'] = 'dinheiro gasto: %i euros' \
                                        % self.dinheiro_gasto
        s = ''
        for i, p in enumerate(self.premios):
            s += 'ganhaste %i vezes o %i. lugar (%i euros)\n' \
                % (p, i + 1, self.dinheiro[i])
        self.l_dinheiro_ganho['text'] = s
        self.l_total_dinheiro_ganho['text'] = 'dinheiro ganho: %i euros' \
                                              % sum(self.dinheiro)
        self.l_lucro['text'] = 'lucro: %i euros' \
                               % (sum(self.dinheiro) - self.dinheiro_gasto)

    def desenhar_numbers(self):
        n = 1
        for f in xrange(NUM_POR_COLUNA):
            for c in xrange(NUM_POR_FILA):
                # desenhar quadradinhos
                self.canvas.create_rectangle(
                    NUM_Q_POSX + c*E_N, NUM_Q_POSY + f*E_N,
                    NUM_Q_POSX + NUM_Q_TAM + c*E_N, NUM_Q_POSY + NUM_Q_TAM + f*E_N,
                    activefill=TELA_FG)
                # write number of squares
                self.canvas.create_text(
                    NUM_POSX + c * E_N, NUM_POSY + f * E_N, text=n, **NUM_FONT)
                n += 1
                if n == N_NUM + 1:
                    break

    def desenhar_estrelas(self):
        n = 1
        for f in xrange(EST_POR_COLUNA):
            for c in xrange(EST_POR_FILA):
                # desenhar quadradinhos
                self.canvas.create_rectangle(
                    EST_Q_POSX + c * 2 * E_E, EST_Q_POSY + f * 2 * E_E,
                    EST_Q_POSX + E_E + c * 2 * E_E, EST_Q_POSY + E_E + f * 2 * E_E,
                    fill=TELA_BG)
                # escrever number on quadradinho
                self.canvas.create_text(
                    EST_POSX + c * 2 * E_E, EST_POSY + f * 2 * E_E,
                    text=n, **EST_FONT)
                n += 1
                if n == N_EST + 1:
                    break

    def desenhar_cruz(self, x, y):
        self.cruzes.append(
            self.canvas.create_line(
                x - E_N / 2, y - E_N / 2, x + E_N / 2, y + E_N / 2, tag='cruz') +
            self.canvas.create_line(
                x + E_N / 2, y - E_N / 2, x - E_N / 2, y + E_N / 2, tag='cruz'))

    def apagar_cruzes(self):
        self.bolas_escolhidas = []
        self.est_escolhidas = []
        self.canvas.delete('cruz')


# encontra as coordenadas, dando um numero ou uma estrela
def encontrar_coord(n, se_num=False):
    if se_num:
        x = E_N * (((n + NUM_POR_FILA - 1) % NUM_POR_FILA) + 0.5)
        y = E_N * ((n - 1) / NUM_POR_FILA + 0.5)
    else:  # se for uma estrela
        x = E_E * (((n + EST_POR_FILA - 1) % EST_POR_FILA) * 2 + 1)
        y = E_E * (((n - 1) / EST_POR_FILA) * 2 + 0.5) + TELA_POSY_MED
    return x, y


# i-inicial, f-final, n_ret-numero de objetos(bolas ou estrelas) retirados
def sortear(i, f, n_ret):
    sorteadas = []
    por_sortear = range(i, f + 1)
    for i in range(n_ret):  # 0, 1, 2
        sorteada = random.choice(por_sortear)
        por_sortear.remove(sorteada)
        sorteadas.append(sorteada)
    sorteadas.sort()
    return sorteadas


def comparar(list1, list2):  # diz o number de numeros iguais nas duas listas
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
                break
    return count

if __name__ == '__main__':
    Game()
