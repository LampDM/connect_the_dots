import matplotlib.pyplot as plt

segments = []

def store_plots(xs,ys):
    segments.append((xs,ys))

def render_plots():
    #plt.plot(5, 25, 'go')  # Additional point
    #plt.plot(6, 36, 'yo')  # Additional point
    for xs,ys in segments:
        plt.plot(xs, ys)
    plt.show()