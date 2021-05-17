import matplotlib.pyplot as plt


def wykres(time_list, data_list):
    d1 = data_list[0]
    dlas = data_list[-1]
    x = range(1, len(time_list)+1)
    y = []
    for z in range(len(time_list)):
        zz = z
        y.append(180)
    yy = []
    for z in range(len(time_list)):
        zz = z
        yy.append(300)
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x, time_list, s=75, c='red')
    ax.plot(x, time_list, linewidth=3)
    ax.plot(x, y, linewidth=3, c='red')
    ax.plot(x, yy, linewidth=3, c='green')
    # mozna dodac daty od do co sie same imporuja
    ax.set_title(f"Wykres czasu nauki Pythona od {d1} do {dlas}", fontsize=24)
    ax.set_xlabel("Dni", fontsize=14)
    ax.set_ylabel("Czas w minutach", fontsize=20)
    ax.tick_params(axis='both', labelsize=20)
    plt.xticks(rotation=45)

    plt.show()
