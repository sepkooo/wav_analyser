from scipy.io.wavfile import read
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    fs, x = read('extracted.wav')
    duration = x.size / float(fs)
    t = np.arange(x.size) / float(fs)
    range_from = 46000
    range_to = 48000
    range_from_z = 200
    range_to_z = 2200
    y = x[range_from:range_to]
    z = x[range_from_z:range_to_z]
    plt.plot(y)
    plt.plot(z)
    max_y = np.max(y)
    max_z = np.max(z)
    count = 0
    count_items = 0
    for item in y:
        count_items += 1
        if max_y == np.max(item):
            count += 1
            break
    count_z = 0
    count_items_z = 0
    for item in z:
        count_items_z += 1
        if max_z == np.max(item):
            count_z += 1
            break
    phase = abs(count_items_z - count_items)
    print('index of maximum Y: {}'.format(count_items))
    print('index of maximum Z: {}'.format(count_items_z))
    print('phase is: {} samples'.format(phase))
    # this loops will shift one of the ranges (y or z) so the 2 plots will be synced
    # - phase -> shift right
    # + phase -> shift left
    if count_items_z >= count_items:
        range_from = range_from - phase
        range_to = range_to - phase
        y = x[range_from:range_to]
    else:
        range_from_z = range_from_z - phase
        range_to_z = range_to_z - phase
        z = x[range_from_z:range_to_z]
    # close currently opened plot
    plt.close()
    plt.plot(y)
    plt.plot(z)
    # select range of values, this time we select range from y and z intervals rather than x
    y = y[0:100]
    z = z[0:100]
    plt.close()
    plt.plot(y)
    plt.plot(z)
    # this will calculate sin from stored values
    sin_y = np.sin(y)
    sin_z = np.sin(z)
    # this converts [[a,b]....[v,w]] to np.array and compares them, result of comparison is stored
    # again as np.array with all results: [[True, True, ..., True, True]]
    comparison = np.array(sin_z) == np.array(sin_y)
    result = comparison.all()
    print(result)
    print(sin_y, sin_z)
    write('dumped.wav', fs, y)
    pass