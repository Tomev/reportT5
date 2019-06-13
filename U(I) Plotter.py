import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Get paths to images
### Room temperature
#folder_path = "./data/U(I)/Pokojowa/"
#file_names = ['-1.5T.txt', '-1.0T.txt', '-0.5T.txt', '0T.txt', '0.5T.txt', '1.0T.txt', '1.5T.txt']
### Nitrogen temperature
folder_path = "./data/U(I)/Azot/"
file_names = ['-1.5T.txt', '-1.0T.txt', '-0.75T.txt', '-0.5T.txt', '-0.25T.txt', '0T.txt', '0.5T.txt',
              '1.0T.txt', '1.25T.txt', '1.5T.txt']

for file_name in file_names:

    print(f"Processing file {0}.", file_name)

    file_path = folder_path + file_name

    B = float(file_name.split('T')[0])

    # Get xs values in wavelength
    f = open(file_path, "r")

    # Omit headers
    for i in range(3):
        f.readline()

    line = f.readline()

    I = []
    U = []

    while(line):
        line_parts = line.split('\t')
        I.append(float(line_parts[0]))
        U.append(float(line_parts[1]))
        line = f.readline()

    print('Data gathered. Plotting.')

    # Plot settings
    #plot_title = "U(I), T = 25 [deg C], B = " + str(B) + " [T]"
    plot_title = "U(I), T = - 196 [deg C], B = " + str(B) + " [T]"
    y_label = "Napięcie prądu U [V]"
    x_label = "Natężenie prądu I [A]"
    x = I
    y = U

    plt.plot(x, y, 'ro')#, x, line)
    plt.title(plot_title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.xticks(rotation='60')
    plt.locator_params(nbins=40)
    plt.savefig("figs/" + str(B) + ".png")
    plt.show()
