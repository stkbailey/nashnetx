import matplotlib.pyplot as plt

def setup_graph_plot(**kwargs):
    fig, ax = plt.subplots(1,1, **kwargs)

    # Other graph settings
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_aspect(1)
    ax.set_frame_on(False)
    
    return fig, ax