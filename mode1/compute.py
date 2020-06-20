import matplotlib.pyplot as plt
import math
import os, time, glob



def compute(sigma_x, sigma_y, tau_xy, setta):
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

    # 1-3. Mode 1: How much angle wanna to be rotate in counter-clockwise
    sigma_xr = sigma_avg + ((float(sigma_x) - float(sigma_y)) / 2) * math.cos(2 * float(setta) * math.pi / 180) + float(tau_xy) * math.sin(2 * float(setta) * math.pi / 180)
    sigma_yr = 2 * sigma_avg - sigma_xr
    tau_xyr = -((float(sigma_x) - float(sigma_y)) / 2) * math.sin(2 * float(setta) * math.pi / 180) + float(tau_xy) * math.cos(2 * float(setta) * math.pi / 180)

    # Draw Mohr's circle by using above value

    ax2.plot([sigma_xr, sigma_yr], [tau_xyr, -tau_xyr], marker='o', color='blue', label='After rotation')
    plt.legend(loc='lower left')

    ax2.annotate(str(round(sigma_xr, 2)) + ',' + str(round(tau_xyr, 2)), xy=(sigma_xr, tau_xyr), xytext=(1.2 * sigma_xr, 1.2 * (tau_xyr)), arrowprops = dict(fc='blue', lw=0.001))
    ax2.annotate(str(round(sigma_yr, 2)) + ',' + str(round(-tau_xyr, 2)), xy=(sigma_yr, -tau_xyr), xytext=(1.2 * sigma_yr, 1.2 * (-tau_xyr)), arrowprops = dict(fc='blue', lw=0.001))

    ax2.set_aspect('equal')
    fig.show()
    # Save img and deliver it to mode1.html
    # run plt.plot, plt.title, etc.
    from io import BytesIO
    figfile = BytesIO()
    fig.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    import base64
    figdata_png = base64.b64encode(figfile.getvalue())


    return figdata_png, [str(round(sigma_xr, 3)), str(round(sigma_yr, 3)), str(round(tau_xyr, 3))]
