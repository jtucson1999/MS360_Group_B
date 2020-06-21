from ms360.settings import BASE_DIR
import matplotlib.pyplot as plt
import math
import os


def compute(sigma_x, sigma_y, tau_xy):
    sigma_avg = (float(sigma_x) + float(sigma_y)) / 2  # center of the Mohr's circle
    radius = math.sqrt(((float(sigma_x) - float(sigma_y)) / 2) ** 2 + (float(tau_xy)) ** 2)  # radius of the Mohr's circle
    #if radius == 0:
        #print("\nYou can't draw Mohr's circle if radius = 0. \n")
        #continue
    principal_stress_max = sigma_avg + math.sqrt(((float(sigma_x) - float(sigma_y)) / 2) ** 2 + (float(tau_xy)) ** 2)
    principal_stress_min = sigma_avg - math.sqrt(((float(sigma_x) - float(sigma_y)) / 2) ** 2 + (float(tau_xy)) ** 2)
    tau_max = math.sqrt(((float(sigma_x) - float(sigma_y)) / 2) ** 2 + (float(tau_xy)) ** 2)

    ## 1-Picture : Direction/sign , Mohr Circle
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
    ax1.annotate('(+)', xy=(-4.5, -5.9), xytext=(4.5, -5.77), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))
    ax1.annotate('(+)', xy=(-6.1, -4.5), xytext=(-6.1, 4.5), fontweight='bold', arrowprops=dict(fc='black', lw=0.001))

    ax1.grid(False)
    ax1.set_aspect('equal')
    ax1.set_xticks([])
    ax1.set_yticks([])

    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')

    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    ax2 = fig.add_subplot(1, 2, 2)

    x_range = max(abs(sigma_avg - radius), abs(sigma_avg + radius))
    ax2.set_xlim(left= -1.3 * x_range, right=1.3 * x_range)
    ax2.set_ylim(bottom= 1.8*radius, top= -1.8*radius)

    ax2.plot([float(sigma_x), float(sigma_y)],[float(tau_xy), -float(tau_xy)], marker='o', color='black', label='original')  # Drawing the line which connects current stress points

    ax2.spines['bottom'].set_position(('data', 0)) #Axis arrangement
    ax2.spines['left'].set_position(('data', 0))
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.set_title('< plane stress condition, x axis = sigma, y axis = tau >', fontsize= 7 )

    # Drawing Circle
    c = plt.Circle((sigma_avg, 0), radius, fc='gray', ec='black')
    ax2.add_patch(c)

    if tau_xy == 0:
        setta_tau_max = 45
    else:
        setta_tau_max = ((math.atan(-(float(sigma_x) - float(sigma_y)) / (2 * float(tau_xy)))) / 2) * 180 / math.pi
    # Draw Mohr's circle by using above value
    ax2.plot([sigma_avg, sigma_avg], [radius, -radius], marker='o', color='blue', label='maximum shear')

    ax2.annotate((str(round(sigma_avg, 2)) + ',' +str(round(radius,2))), xy=(sigma_avg, radius), xytext=(sigma_avg, 1.2 * radius), arrowprops=dict(fc='blue', lw=0.001))
    ax2.annotate((str(round(sigma_avg, 2)) + ',' +str(round(-radius,2))), xy=(sigma_avg, -radius), xytext=(sigma_avg, 1.2 * (-radius)), arrowprops=dict(fc='blue', lw=0.001))

    plt.legend(loc='lower left')
    ax2.set_aspect('equal')
    #plt.show()
    
    # Save img and deliver it to mode1.html
    if not os.path.isdir(BASE_DIR+'/mode3/static'):
        os.mkdir(BASE_DIR+'/mode3/static')
    else:
        # Remove old plot files
        filename = os.path.join(BASE_DIR, 'mode3', 'static', 'mode3.png')
        os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    figdata_png = os.path.join(BASE_DIR, 'mode3', 'static', 'mode3.png')
    plt.savefig(figdata_png)
    plt.close('all')


    return [str(round(setta_tau_max, 3)), str(round(setta_tau_max + 90, 3)), str(round(tau_max, 3))]
