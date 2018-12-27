import matplotlib.pyplot as plt

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=3, colspan=1)
ax2 = plt.subplot2grid((6,1), (3,0), rowspan=3, colspan=1,sharex=ax1)

ax1.plot(df['Temp, °C'])
# ax2.bar(df['RH, %'])
ax2.plot(df['RH, %'])