from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# Ux_residual = []
# Uy_residual = []
# Uz_residual = []
# p_residual = []
# global_residual = []
# iterations = []

# iteration = 0
# with open('log.foamRun', 'r') as foamRunLog:
#     foamRunLogLines = foamRunLog.readlines()
#     for line in foamRunLogLines:
#         if line.startswith('Time = '):
#             iteration = int(line.lstrip('Time = ').rstrip('s\n'))
#             iterations.append(iteration)
#         # if line.startswith('SIMPLE: Iteration '):
#         #     iteration += 1
#         #     iterations.append(iteration)
#         # if line.startswith('GAMG:  Solving for Ux'):
#         if line.startswith('smoothSolver:  Solving for Ux'):
#             line_partida = line.split(',')
#             line_Ux_residual =  float( line_partida[2].lstrip(' Final residual = ') )
#             Ux_residual.append(line_Ux_residual)
#         if line.startswith('smoothSolver:  Solving for Uy'):
#             line_partida = line.split(',')
#             line_Uy_residual =  float( line_partida[2].lstrip(' Final residual = ') )
#             Uy_residual.append(line_Uy_residual)
#         if line.startswith('smoothSolver:  Solving for Uz'):
#             line_partida = line.split(',')
#             line_Uz_residual =  float( line_partida[2].lstrip(' Final residual = ') )
#             Uz_residual.append(line_Uz_residual)
#         if line.startswith('GAMG:  Solving for p'):
#             line_partida = line.split(',')
#             line_Ux_residual =  float( line_partida[2].lstrip(' Final residual = ') )
#             try:
#                 p_residual[iteration-1] = line_Ux_residual
#             except:
#                 p_residual.append(line_Ux_residual)
#         if line.startswith('time step continuity errors :'):
#             line_partida = line.split(',')
#             line_global_residual = abs( float( line_partida[1].lstrip('global = ').rstrip('\n')) )
#             global_residual.append(line_global_residual)
# global = -3.029491e-06


# try:
#     plt.plot(iterations, p_residual)
# except:
#     plt.plot(iterations[:-1], p_residual)
# plt.yscale('log')
# plt.title('p residuals')
# plt.show()
# plt.clf()

# # plt.plot(iterations, Ux_residual)
# try:
#     plt.plot(iterations, Ux_residual)
# except:
#     plt.plot(iterations[:-1], Ux_residual)
# plt.yscale('log')
# plt.title('Ux residuals')
# plt.show()
# plt.clf()
# try:
#     plt.plot(iterations, global_residual)
# except:
#     plt.plot(iterations[:-1], global_residual)
# plt.yscale('log')
# plt.title('global residuals')
# plt.show()
fig, axs = plt.subplots(3,figsize=(8,12))
def animate(i):
    Ux_residual = []
    Uy_residual = []
    Uz_residual = []
    p_residual = []
    global_residual = []
    iterations = []

    iteration = 0
    with open('log.foamRun', 'r') as foamRunLog:
        foamRunLogLines = foamRunLog.readlines()
        for line in foamRunLogLines:
            if line.startswith('Time = '):
                iteration = int(line.lstrip('Time = ').rstrip('s\n'))
                iterations.append(iteration)
            # if line.startswith('SIMPLE: Iteration '):
            #     iteration += 1
            #     iterations.append(iteration)
            # if line.startswith('GAMG:  Solving for Ux'):
            if line.startswith('smoothSolver:  Solving for Ux'):
                line_partida = line.split(',')
                line_Ux_residual =  float( line_partida[2].lstrip(' Final residual = ') )
                Ux_residual.append(line_Ux_residual)
            if line.startswith('smoothSolver:  Solving for Uy'):
                line_partida = line.split(',')
                line_Uy_residual =  float( line_partida[2].lstrip(' Final residual = ') )
                Uy_residual.append(line_Uy_residual)
            if line.startswith('smoothSolver:  Solving for Uz'):
                line_partida = line.split(',')
                line_Uz_residual =  float( line_partida[2].lstrip(' Final residual = ') )
                Uz_residual.append(line_Uz_residual)
            if line.startswith('GAMG:  Solving for p'):
                line_partida = line.split(',')
                line_Ux_residual =  float( line_partida[2].lstrip(' Final residual = ') )
                try:
                    p_residual[iteration-1] = line_Ux_residual
                except:
                    p_residual.append(line_Ux_residual)
            if line.startswith('time step continuity errors :'):
                line_partida = line.split(',')
                line_global_residual = abs( float( line_partida[1].lstrip('global = ').rstrip('\n')) )
                global_residual.append(line_global_residual)
    axs[0].clear()
    axs[1].clear()
    axs[2].clear()

    try:
        axs[0].plot(iterations, global_residual)
    except:
        axs[0].plot(iterations[:-1], global_residual)
    axs[0].set_title('global residuals')
    axs[0].set_yscale('log')

    try:
        axs[1].plot(iterations, Ux_residual, label = 'Ux')
        axs[1].plot(iterations, Uy_residual, label = 'Uy')
        axs[1].plot(iterations, Uz_residual, label = 'Uz')
    except:
        max_len_Ux = max([len(iterations), len(Ux_residual)])
        axs[1].plot(iterations[:max_len_Ux-1], Ux_residual[:max_len_Ux-1], label = 'Ux')
        max_len_Uy = max([len(iterations), len(Uy_residual)])
        axs[1].plot(iterations[:max_len_Uy-1], Uy_residual[:max_len_Uy-1], label = 'Uy')
        max_len_Uz = max([len(iterations), len(Uz_residual)])
        axs[1].plot(iterations[:max_len_Uz-1], Uz_residual[:max_len_Uz-1], label = 'Uz')
    axs[1].set_title('velocity residuals')
    axs[1].set_yscale('log')
    axs[1].legend()

    try:
        axs[2].plot(iterations, p_residual)
    except:
        axs[2].plot(iterations[:-1], p_residual)
    axs[2].set_title('pressure residuals')
    axs[2].set_yscale('log')
    plt.show()
# for j in range(100):
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()