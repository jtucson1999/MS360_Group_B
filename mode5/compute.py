from ms360.settings import BASE_DIR
import matplotlib.pyplot as plt
import math
import os
def compute(epsilon_x, epsilon_y, gamma_xy):
    epsilon_avg = (float(epsilon_x) + float(epsilon_y)) / 2  # center of the Mohr's circle
    radius = math.sqrt(((float(epsilon_x) - float(epsilon_y)) / 2) ** 2 + (float(gamma_xy) / 2) ** 2)  # radius of the Mohr's circle
    principal_strain_max = epsilon_avg + math.sqrt(((float(epsilon_x) - float(epsilon_y)) / 2) ** 2 + (float(gamma_xy) / 2) ** 2)
    principal_strain_min = epsilon_avg - math.sqrt(((float(epsilon_x) - float(epsilon_y)) / 2) ** 2 + (float(gamma_xy) / 2) ** 2)
    gamma_max = 2 * (math.sqrt(((float(epsilon_x) - float(epsilon_y)) / 2) ** 2 + (float(gamma_xy) / 2) ** 2))

    ## 2-Picture : Direction/Sign and Mohr Circle
    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)

    ax1.set_xlim(left=-15, right=15)
    ax1.set_ylim(bottom=-15, top=15)

    ax1.plot([-5, 5], [5, 5], color='black')
    ax1.plot([-5, 5], [-5, -5], color='black')
    ax1.plot([-5, -5], [-5, 5], color='black')
    ax1.plot([5, 5], [-5, 5], color='black')

    ax1.annotate('(-)', xy=(7.5, 0), xytext=(11, 0.1), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(+)', xy=(0, 12), xytext=(0, 7.5), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(-)', xy=(-7.5, 0), xytext=(-12, 0.1), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(+)', xy=(0, -12), xytext=(0, -7.5), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))

    ax1.annotate('(+)', xy=(5.8, 4.5), xytext=(5.8, -4.5), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(+)', xy=(4.5, 5.7), xytext=(-4.5, 5.8), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(+)', xy=(-4.5, -5.9), xytext=(4.5, -5.77), fontweight='bold',
                 arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(+)', xy=(-6.1, -4.5), xytext=(-6.1, 4.5), fontweight='bold',
                 arrowprops=dict(fc='black', lw=0.001))

    ax1.grid(False)
    ax1.set_aspect('equal')
    ax1.set_xticks([])
    ax1.set_yticks([])

    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')

    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax2 = fig.add_subplot(1, 2, 2)

    x_range = max(abs(epsilon_avg - radius), abs(epsilon_avg + radius))
    ax2.set_xlim(left=-x_range - 1, right=x_range + 1)
    ax2.set_ylim(bottom=2 * radius - 1, top=-2 * radius + 1)

    ax2.plot([float(epsilon_x), float(epsilon_y)], [float(gamma_xy)/2, -float(gamma_xy)/2], marker='o', color='black',
             label='original')  # Drawing the line which connects current stress points

    ax2.spines['bottom'].set_position(('data', 0))  # Axis arrangement
    ax2.spines['left'].set_position(('data', 0))
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.set_title('< plane stress condition, x axis = epsilon, y axis = gamma/2 >', fontsize= 7 )

    c = plt.Circle((epsilon_avg, 0), radius, fc='gray', ec='black')
    ax2.add_patch(c)

    if gamma_xy == 0:
        setta_principal = 0
    elif (float(epsilon_x) - float(epsilon_y)) == 0:
        setta_principal = 45
    else:
        setta_principal = ((math.atan(float(gamma_xy) / (float(epsilon_x) - float(epsilon_y)))) / 2) * 180 / math.pi


    # Draw Mohr's circle by using above value
    ax2.plot([epsilon_avg - radius, epsilon_avg + radius], [0, 0], marker='o', color='blue', label='principal')
    ax2.annotate((str(round(epsilon_avg + radius, 2)) + ', 0'), xy=(epsilon_avg + radius, 0),
                 xytext=(1.2 * (epsilon_avg + radius), 1), arrowprops=dict(fc='blue', lw=0.001))
    ax2.annotate((str(round(epsilon_avg - radius, 2)) + ', 0'), xy=(epsilon_avg - radius, 0),
                 xytext=(1.2 * (epsilon_avg - radius), 1), arrowprops=dict(fc='blue', lw=0.001))

    plt.legend(loc='lower left')
    ax2.set_aspect('equal')
    #plt.show()
    
    # Save img and deliver it to mode1.html
    if not os.path.isdir(BASE_DIR+'/mode5/static'):
        os.mkdir(BASE_DIR+'/mode5/static')
    else:
        # Remove old plot files
        filename = os.path.join(BASE_DIR, 'mode5', 'static', 'mode5.png')
        os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    figdata_png = os.path.join(BASE_DIR, 'mode5', 'static', 'mode5.png')
    plt.savefig(figdata_png)
    plt.close('all')


    return [str(round(setta_principal, 3)), str(round(setta_principal + 90, 3)), str(round(principal_strain_max, 3)), str(round(principal_strain_min, 3))] 