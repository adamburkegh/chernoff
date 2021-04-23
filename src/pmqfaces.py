
import matplotlib
import matplotlib.pyplot as plt
from chernoff import *


# PMQ Defaults

PMQ_DEFAULT_VEC = [0.6 for x in range(19)]
PMQ_DEFAULT_VEC[UPPER_FACE] = 0.9
PMQ_DEFAULT_VEC[NOSE_LENGTH] = 0
PMQ_DEFAULT_VEC[EYE_VERTICAL] = 0.2
PMQ_DEFAULT_VEC[EYEBROW_SLANT] = 0.45
PMQ_DEFAULT_VEC[EYEBROW_SIZE] = 0.5 
PMQ_DEFAULT_VEC[HAIR_SIZE] = 0


def init_fig():
    return plt.figure(figsize=(11,11),frameon=False)

def pmq_face(fig,fitness,precision,simplicity,offset=0):
    vec = PMQ_DEFAULT_VEC.copy()
    vec[MOUTH_CURVE] = fitness
    vec[MOUTH_WIDTH] = fitness
    vec[EYE_SIZE] = precision
    # vec[HAIR_SIZE] = 1-simplicity
    vec[EYEBROW_SLANT] = simplicity
    ax = fig.add_subplot(5,5,1+offset,aspect='equal')
    cface(ax, *vec)
    ax.axis([-1.2,1.2,-1.2,1.2])
    ax.set_axis_off()
    ax.set_xticks([])
    ax.set_yticks([])
    fig.subplots_adjust(hspace=0, wspace=0)


class PMQFace:
    def __init__(self):
        self.faces = 0
        self.fig = init_fig()

    def add_model(self,fitness,precision,simplicity):
        pmq_face(self.fig,fitness,precision,simplicity,self.faces)
        self.faces += 1


def main():
    matplotlib.use('svg',force=True)
    pmf = PMQFace()
    pmf.add_model(0.9,0.9,0.9)
    pmf.add_model(0.1,0.3,0.2)
    pmf.add_model(0.8,0.4,0.5)
    pmf.add_model(0.9,0.1,0.9)
    pmf.add_model(0.1,0.9,0.1)
    pmf.add_model(1.0,1.0,0.1)
    pmf.add_model(0.1,0.1,1.0)
    plt.savefig("face.svg")
    print("Output to face.svg")


if __name__ == "__main__":
    main()

