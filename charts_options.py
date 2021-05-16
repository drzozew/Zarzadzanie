import matplotlib.pyplot as plt


def wykres(time_list):
    time_list = time_list
    fig, ax = plt.subplots()
    ax.plot(time_list)
    plt.show()
