import init
import matplotlib.pyplot as plt

def run_expr(filename, h, d, total_time):
    X, y = init.data_params(filename)

    # 10s
    kat_loss = katyusha(total_time, h, d, X, y)
    storc_loss = storc(total_time, h, d, X, y)
    svrf_loss = svrf(total_time, h, d, X, y)

    plt.ylabel('Loss')
    plt.xlabel('Time(s)')

    xaxis = range(total_time)
    plt.plot(xaxis, kat_loss, 'r-', label = 'Katyusha')
    plt.plot(xaxis, storc_loss, 'b-', label = 'STORC')
    plt.plot(xaxis, svrf_loss, 'g-', label = 'SVRF')

    plt.legend()
    plt.savefig(filename + '/loss_' + filename + '.png')
    plt.show()
