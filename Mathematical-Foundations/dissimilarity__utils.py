import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import transforms
import numpy as np

##################
# Synthetic data #
##################

r = 1
np.random.seed(123456)
y1A = np.random.uniform(-r, r, 8)
y2A = np.random.uniform(-r, r, 8)
yA = np.array([y1A, y2A]).T
M, N = 32j, 32j
s, t = np.mgrid[-r:r:N*8, -r:r:M*8]
yB = np.array([s.ravel(), t.ravel()]).T

clni = '''
Um cabra de Lampião
Por nome Pilão Deitado
Que morreu numa trincheira
Em certo tempo passado
Agora pelo sertão
Anda correndo visão
Fazendo mal-assombrado

E foi quem trouxe a notícia
Que viu Lampião chegar
O Inferno nesse dia
Faltou pouco pra virar
Incendiou-se o mercado
Morreu tanto cão queimado
Que faz pena até contar

Morreu a mãe de Canguinha
O pai de Forrobodó
Três netos de Parafuso
Um cão chamado Cotó
Escapuliu Boca Ensossa
E uma moleca moça
Quase queimava o “totó”

Morreram 100 negros velhos
Que não trabalhavam mais
Um cão chamado Trás-cá
Vira-volta e Capataz
Tromba Suja e Bigodeira
Um cão chamado Goteira
Cunhado de Satanás
'''

####################
# Base conversions #
####################

def conv_baseDecimal(N, b):
    S = {e:i for i, e in enumerate('0123456789ABCDEF')}
    N = N.upper()
    Ns = N.split('.' or ',')
    if len(Ns) == 1:
        n = len(Ns[0])
        m = 0
    elif len(Ns) == 2:
        n = len(Ns[0])
        m = len(Ns[1])
    else:
        raise ValueError('The value must have just one fractional part!')
    N = ''.join(Ns)[::-1]
    if not all([S[d] <= b - 1 for d in N]):
        raise ValueError('The value of the digits must be less than the base!')
    return sum([S[d]*b**k for d, k in zip(N, range(-m, n))])

def conv_decimalBase(N, b, prec=32):
    S = {i:e for i, e in enumerate('0123456789ABCDEF')}
    i, f = divmod(N, 1)
    saida = '0' if not i else ''
    while(i):
        i, r = divmod(i, b)
        saida += S[r]
    saida = saida[::-1] + '.'
    
    while(f and len(saida) <= prec):
        f = round(f, 10)
        i, f = divmod(f*b, 1)
        saida += S[int(i)]
    return saida

def ieee754_realBin(N, n=32):
    k = {16: 10, 32: 23, 64: 52, 128: 112, 256: 236}
    if n not in k:
        raise ValueError('Invalid accuracy value!')
    k = k[n]
    nq = n - k - 1
    s = '1' if N < 0 else '0'
    Nb = conv_decimalBase(abs(N), 2, n)
    a, b = Nb.find('1'), Nb.find('.')
    e = b - a if a > b else b - a - 1
    vies = 2**(nq)/2 - 1
    q = conv_decimalBase(vies + e, 2, nq)
    q = q[:-1].rjust(nq, '0')
    Nb = Nb.replace('.', '')
    p = Nb[a+1:a+k+1].ljust(k, '0')
    return s + q + p

def ieee754_binReal(N):
    k = {16: 10, 32: 23, 64: 52, 128: 112, 256: 236}
    n = len(N)
    if n not in k:
        raise ValueError('Invalid IEEE 754 pattern!')
    k = k[n]
    nq = n - k - 1
    v = 2**(nq)/2 - 1
    s = eval(N[0])
    q = N[1:nq+1]
    e = conv_baseDecimal(q, 2) - v
    p = '0.' + N[-k:]
    p = conv_baseDecimal(p, 2)
    return (-1)**s*(1 + p)*2**e

#########
# Plots #
#########

plt.rcParams['figure.figsize'] = (16, 8)
cmap = cm.get_cmap('jet')

def plotPoints(ax, x, d, dmax):
    xo, yo = x
    for i, [xi, yi] in enumerate(yA):
        color = cmap(d[i]/dmax)
        ax.plot([xo, xi], [yo, yi], '--', c=color, zorder=0)
        cx = (xi + xo)*0.5
        cy = (yi + yo)*0.5
        m = (yi - xo)/(xi - yo)
        theta = np.rad2deg(np.arctan(m))
        ax.text(cx, cy, '{0:.02f}'.format(d[i]),
                 rotation=theta, fontsize=12,
                 horizontalalignment='center',
                 verticalalignment='center',
                 bbox=dict(boxstyle='round',
                           color=color,
                           alpha=0.5))
    ax.scatter(*yA.T, zorder=2)
    ax.scatter(*x, c='k', zorder=2, lw=3)
    ax.annotate('x = ({0}, {1})'.format(*x),
                xy=x, xytext=(xo + 0.1, yo + 0.2),
                ha='left', va='bottom',
                fontsize=12,
                bbox=dict(boxstyle='round,pad=0.5',
                          fc='k',
                          alpha=0.25),
                arrowprops=dict(facecolor = 'black',
                                alpha=0.5,
                                width=1,
                                headwidth=6,
                                connectionstyle='arc3,rad=0.25'))
    ax.set_xlim([-r, r])
    ax.set_ylim([-r, r])

def plotContour(ax, d, title='', fsize=12):
    mesh = ax.pcolormesh(s, t, d, cmap='jet')
    cont = ax.contour(s, t, d, 7, cmap = 'gray')
    ax.clabel(cont, fontsize=fsize, inline=True)
    ax.set_xlim([-r, r])
    ax.set_ylim([-r, r])
    ax.set_title(title)
    return mesh

def plotDist(x, dA, dB, figname, ptitle='', ctitle='', save=False):
    fig, (axA, axB) = plt.subplots(1, 2)
    
    dmax = np.max([dA.max(), dB.max()])

    plotPoints(axA, x, dA, dmax)
    mesh = plotContour(axB, dB, ctitle)
    
    cbar_ax = fig.add_axes([0.125, 0.025, 0.775, 0.05])
    fig.colorbar(mesh, cax = cbar_ax, orientation = 'horizontal')
    fig.suptitle(' '.join([e.capitalize() for e in figname.split('_')]))
    if save:
        fig.savefig('_output/similarity_{}.png'.format(figname), bbox_inches='tight')

def plotText(p, q, dT, figname, save=False):
    fig, axA = plt.subplots(1, 1)
    xo, yo = 0.05, 1
    for i, est in enumerate(q.split('\n\n')):
        yo -= 0.05
        if i == len(q.split('\n\n'))//2:
            xo = 0.55
            yo = 0.9
        for j, ver in enumerate(est.split('\n')):
            ax = plt.gca()
            t = ax.transData
            canvas = ax.figure.canvas
            yo -= 0.05
            for k, pal in enumerate(ver.split()):
                text = axA.text(xo, yo, pal + ' ',color=cmap(dT[pal]/max(dT.values())),
                                fontsize=22,
                                transform=t,
                                horizontalalignment='left',
                                verticalalignment='top')
                text.draw(canvas.get_renderer())
                ex = text.get_window_extent()
                t = transforms.offset_copy(text._transform, x=ex.width, units='dots')
    cbar_ax = fig.add_axes([0.125, 0.025, 0.775, 0.05])
    norm = matplotlib.colors.Normalize(vmin=0, vmax=max(dT.values()))
    matplotlib.colorbar.ColorbarBase(cbar_ax,
                                     cmap=cmap,
                                     norm=norm,
                                     orientation='horizontal')
    axA.set_title(' '.join([e.capitalize() for e in figname.split('_')]))
    axA.axis('off')
    if save:
        fig.savefig('_output/similarity_{}.png'.format(figname), bbox_inches='tight')