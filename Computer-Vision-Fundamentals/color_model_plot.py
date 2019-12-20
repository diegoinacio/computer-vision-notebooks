import numpy as np

from plotly import __version__, tools
from plotly.offline import init_notebook_mode, iplot

from plotly.graph_objs import *
init_notebook_mode(connected=True)


def plotRGB(points):
    ##########################
    # Identity visualization #
    ##########################
    # Create identity points
    iRGB = np.array([
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1]
    ])
    # Identity point color
    ipColor = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in zip(*iRGB)]
    # Identity point scatter
    ipMODEL = Scatter3d(
        x=iRGB[0],
        y=iRGB[1],
        z=iRGB[2],
        mode='markers',
        hovertext=[f'iPoint {e}' for e in range(8)],
        marker={
            'size': 8,
            'color': ipColor
        }
    )
    # Create identity edges
    edge_pairs = [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    x_lines, y_lines, z_lines, c_lines = [], [], [], []
    for p in edge_pairs:
        for i in range(2):
            x_lines.append(iRGB[0][p[i]])
            y_lines.append(iRGB[1][p[i]])
            z_lines.append(iRGB[2][p[i]])
            c_lines.append(ipColor[p[i]])
        x_lines.append(None)
        y_lines.append(None)
        z_lines.append(None)
        c_lines.append('rgb(1, 0, 0)')
    # Identity edge scatter
    ieMODEL = Scatter3d(
        x=x_lines,
        y=y_lines,
        z=z_lines,
        mode='lines',
        line={'color': c_lines, 'width': 4}
    )
    #############################
    # Point cloud visualization #
    #############################
    # Split channels
    R, G, B = points.T
    # Define point colors
    color = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in points]
    MODEL = Scatter3d(
        x=R, y=G, z=B,
        name='RGB color model',
        mode='markers',
        line={'dash': 'dot'},
        marker={
            'size': 1,
            'color': color
        }
    )
    ##########################
    # Visualization settings #
    ##########################
    DATA = [ipMODEL, ieMODEL, MODEL]
    # Layout
    layout = Layout(
        title='RGB color model',
        margin={'l': 0, 'r': 0, 'b': 0, 't':0},
        scene={
            'xaxis': {'title': 'R'},
            'yaxis': {'title': 'G'},
            'zaxis': {'title': 'B'}
        },
        showlegend=False
    )
    # Figure
    fig = Figure(data=DATA, layout=layout)
    # Camera
    CAMERA = {
        'up': {'x': 0, 'y': 1, 'z': 0},
        'eye': {'x': 1.2, 'y': 1,'z': 1.5}
    }
    # Update visualization
    fig['layout'].update(scene={'camera': CAMERA})
    # Plot
    iplot(fig, filename='RGB_color', show_link=False)


def plotXYZ(points, colors, m):
    ##########################
    # Identity visualization #
    ##########################
    # Create identity points
    iRGB = np.array([
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1]
    ])
    # Identity point color
    ipColor = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in zip(*iRGB)]
    iRGB = np.dot(m, iRGB)
    # Identity point scatter
    ipMODEL = Scatter3d(
        x=iRGB[0],
        y=iRGB[1],
        z=iRGB[2],
        mode='markers',
        hovertext=[f'iPoint {e}' for e in range(8)],
        marker={
            'size': 8,
            'color': ipColor
        }
    )
    # Create identity edges
    edge_pairs = [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    x_lines, y_lines, z_lines, c_lines = [], [], [], []
    for p in edge_pairs:
        for i in range(2):
            x_lines.append(iRGB[0][p[i]])
            y_lines.append(iRGB[1][p[i]])
            z_lines.append(iRGB[2][p[i]])
            c_lines.append(ipColor[p[i]])
        x_lines.append(None)
        y_lines.append(None)
        z_lines.append(None)
        c_lines.append('rgb(1, 0, 0)')
    # Identity edge scatter
    ieMODEL = Scatter3d(
        x=x_lines,
        y=y_lines,
        z=z_lines,
        mode='lines',
        line={'color': c_lines, 'width': 4}
    )
    #############################
    # Point cloud visualization #
    #############################
    # Split channels
    X, Y, Z = points.T
    # Define point colors
    color = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in colors]
    MODEL = Scatter3d(
        x=X, y=Y, z=Z,
        name='XYZ color model',
        mode='markers',
        line={'dash': 'dot'},
        marker={
            'size': 1,
            'color': color
        }
    )
    ##########################
    # Visualization settings #
    ##########################
    DATA = [ipMODEL, ieMODEL, MODEL]
    # Layout
    layout = Layout(
        title='RGB color model',
        margin={'l': 0, 'r': 0, 'b': 0, 't':0},
        scene={
            'xaxis': {'title': 'X'},
            'yaxis': {'title': 'Y'},
            'zaxis': {'title': 'Z'}
        },
        showlegend=False
    )
    # Figure
    fig = Figure(data=DATA, layout=layout)
    # Camera
    CAMERA = {
        'up': {'x': 0, 'y': 1, 'z': 0},
        'eye': {'x': 1.2, 'y': 1,'z': 1.5}
    }
    # Update visualization
    fig['layout'].update(scene={'camera': CAMERA})
    # Plot
    iplot(fig, filename='XYZ_color', show_link=False)


def plotHSV(points, colors):
    ##########################
    # Identity visualization #
    ##########################
    # Create identity points
    h = np.array([0, 60, 120, 180, 240, 300, 0, 0])
    X = np.sin(2*np.pi*h/360); X[-1] = 0; X[-2] = 0
    Z = np.cos(2*np.pi*h/360); Z[-1] = 0; Z[-2] = 0
    Y = np.array([1, 1, 1, 1, 1, 1, 1, 0])
    iRGB = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
    # Identity point color
    ipColor = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in iRGB]
    # Identity point scatter
    ipMODEL = Scatter3d(
        x=X,
        y=Y,
        z=Z,
        mode='markers',
        hovertext=[f'iPoint {e}' for e in range(8)],
        marker={
            'size': 8,
            'color': ipColor
        }
    )
    # Create identity edges
    edge_pairs = []
    for i in range(5):
        edge_pairs += [i, i+1], [i, 6], [i, 7]
    else:
        edge_pairs += [5, 0], [5, 6], [5, 7]
    x_lines, y_lines, z_lines, c_lines = [], [], [], []
    for p in edge_pairs:
        for i in range(2):
            x_lines.append(X[p[i]])
            y_lines.append(Y[p[i]])
            z_lines.append(Z[p[i]])
            c_lines.append(ipColor[p[i]])
        x_lines.append(None)
        y_lines.append(None)
        z_lines.append(None)
        c_lines.append('rgb(1, 0, 0)')
    # Identity edge scatter
    ieMODEL = Scatter3d(
        x=x_lines,
        y=y_lines,
        z=z_lines,
        mode='lines',
        line={'color': c_lines, 'width': 4}
    )
    #############################
    # Point cloud visualization #
    #############################
    # Split channels
    H, S, V = points.T
    X = S*V*np.sin(2*np.pi*H/360)
    Z = S*V*np.cos(2*np.pi*H/360)
    # Define point colors
    color = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in colors]
    MODEL = Scatter3d(
        x=X, y=V, z=Z,
        name='HSV color model',
        mode='markers',
        line={'dash': 'dot'},
        marker={
            'size': 1,
            'color': color
        }
    )
    ##########################
    # Visualization settings #
    ##########################
    DATA = [ipMODEL, ieMODEL, MODEL]
    # Layout
    layout = Layout(
        title='RGB color model',
        margin={'l': 0, 'r': 0, 'b': 0, 't':0},
        scene={
            'xaxis': {'title': 'X'},
            'yaxis': {'title': 'Y'},
            'zaxis': {'title': 'Z'}
        },
        showlegend=False
    )
    # Figure
    fig = Figure(data=DATA, layout=layout)
    # Camera
    CAMERA = {
        'up': {'x': 0, 'y': 1, 'z': 0},
        'eye': {'x': 1.2, 'y': 1,'z': 1.5}
    }
    # Update visualization
    fig['layout'].update(scene={'camera': CAMERA})
    # Plot
    iplot(fig, filename='HSV_color', show_link=False)


def plotHSL(points, colors):
    ##########################
    # Identity visualization #
    ##########################
    # Create identity points
    h = np.array([0, 60, 120, 180, 240, 300, 0, 0])
    X = np.sin(2*np.pi*h/360); X[-1] = 0; X[-2] = 0
    Z = np.cos(2*np.pi*h/360); Z[-1] = 0; Z[-2] = 0
    Y = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0])
    iRGB = [[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 0]]
    # Identity point color
    ipColor = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in iRGB]
    # Identity point scatter
    ipMODEL = Scatter3d(
        x=X,
        y=Y,
        z=Z,
        mode='markers',
        hovertext=[f'iPoint {e}' for e in range(8)],
        marker={
            'size': 8,
            'color': ipColor
        }
    )
    # Create identity edges
    edge_pairs = []
    for i in range(5):
        edge_pairs += [i, i+1], [i, 6], [i, 7]
    else:
        edge_pairs += [5, 0], [5, 6], [5, 7]
    x_lines, y_lines, z_lines, c_lines = [], [], [], []
    for p in edge_pairs:
        for i in range(2):
            x_lines.append(X[p[i]])
            y_lines.append(Y[p[i]])
            z_lines.append(Z[p[i]])
            c_lines.append(ipColor[p[i]])
        x_lines.append(None)
        y_lines.append(None)
        z_lines.append(None)
        c_lines.append('rgb(1, 0, 0)')
    # Identity edge scatter
    ieMODEL = Scatter3d(
        x=x_lines,
        y=y_lines,
        z=z_lines,
        mode='lines',
        line={'color': c_lines, 'width': 4}
    )
    #############################
    # Point cloud visualization #
    #############################
    # Split channels
    H, S, V = points.T
    V2 = np.where(V <= 0.5, V, 1 - V)*2
    X = S*V2*np.sin(2*np.pi*H/360)
    Z = S*V2*np.cos(2*np.pi*H/360)
    # Define point colors
    color = [f'rgb({int(r*255)}, {int(g*255)}, {int(b*255)})' for r, g, b in colors]
    MODEL = Scatter3d(
        x=X, y=V, z=Z,
        name='HSL color model',
        mode='markers',
        line={'dash': 'dot'},
        marker={
            'size': 1,
            'color': color
        }
    )
    ##########################
    # Visualization settings #
    ##########################
    DATA = [ipMODEL, ieMODEL, MODEL]
    # Layout
    layout = Layout(
        title='HSL color model',
        margin={'l': 0, 'r': 0, 'b': 0, 't':0},
        scene={
            'xaxis': {'title': 'X'},
            'yaxis': {'title': 'Y'},
            'zaxis': {'title': 'Z'}
        },
        showlegend=False
    )
    # Figure
    fig = Figure(data=DATA, layout=layout)
    # Camera
    CAMERA = {
        'up': {'x': 0, 'y': 1, 'z': 0},
        'eye': {'x': 1.2, 'y': 1,'z': 1.5}
    }
    # Update visualization
    fig['layout'].update(scene={'camera': CAMERA})
    # Plot
    iplot(fig, filename='HSL_color', show_link=False)