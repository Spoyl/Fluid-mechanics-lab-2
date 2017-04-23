import math as m
import matplotlib.pyplot as plt
import numpy as np

gamma = 1.4
five_p = [1., 1.43, 1.52, 1.67, 1.72, 1.92, 2.94, 4.55]
fiveptwo_p = [1.04, 1.49, 1.53, 1.68, 1.86, 1.93, 2.89, 3.47]

bestdat = [1.14, 1.32, 1.3, 1.2, 1.16, 1.12, 1.11, 1.11]

Mfive = [2*(m.exp(((m.log(p)*0.4)/gamma))-1)/(0.4) for p in five_p]
Mfiveptwo =[2*(m.exp(((m.log(p)*0.4)/gamma))-1)/(0.4) for p in fiveptwo_p]
bdy = [2*(m.exp(((m.log(p)*0.4)/gamma))-1)/(0.4) for p in bestdat]

x = [0.75, 1.5, 2.25, 3., 3.75, 4.5, 5.25, 6.]

rho = 1.225
cp = 0.001
T = 298.
gamma = 1.4
A = [0.02, 0.04, 0.06]
xData = np.linspace(0, 1, 50)


def mach_vs_x_plot():
    plt.plot(x, Mfive, 'b-o', label = '$\ P_0 =$ 5 Bar')
    plt.plot(x, Mfiveptwo, "g-o", label = '$\ P_0 =$ 5.2 Bar')
    plt.plot(x, bdy, 'r-o', label = '$\dot m = $3.2 g/s')
    plt.grid(which = 'minor')
    plt.grid(which = 'major')
    plt.minorticks_on()
    
    plt.title("Graph 3: Mach number distribution")
    plt.xlabel("X(mm)")
    plt.ylabel("M")
    plt.legend(loc = 2, fontsize = "small")
    
    plt.savefig("Lab 2 Mach vs x.png")
    plt.show()


def theory_plot():
    mdot = []
    for a in A:
        for i in xData:
            m = rho*a*((2.*cp*T)**0.5)*(i**(1/gamma))*(1-(i**(0.4/gamma)))**0.5
            mdot.append(m)
        plt.plot(xData, mdot, label = "A = "+str(a)+" m")
        mdot = []
    plt.grid()
    plt.legend(loc=2, fontsize = "small")
    plt.xlabel("$\ P_2 / P_0$")
    plt.ylabel("Mass flow rate ($\ g/s $ )")
    plt.title("Theoretical mass flow rate against pressure \nratio for a section of the duct")
    
    plt.savefig("theory graph1.png")
    plt.show()