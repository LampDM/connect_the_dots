import matplotlib.pyplot as plt

segments = []

def plot_rezF(rezults):
    for a, b in rezults:
        store_plots([a.x, b.x], [a.y, b.y])

def plot_rez(rezults):
    for k in range(len(rezults)-1):
        store_plots([rezults[k].x,rezults[k+1].x],[rezults[k].y,rezults[k+1].y])

def points_rez(rezults):
    for p in rezults:
        plt.scatter(p.x, p.y, s=10)
    plt.show()

def store_plots(xs,ys):
    segments.append((xs,ys))

def render_plots():
    for xs,ys in segments:
        plt.plot(xs, ys)
    plt.show()