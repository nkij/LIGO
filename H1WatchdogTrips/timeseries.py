#This program plots ISI_ITMX CPS spectrum around 1099109374.275391 (Nov 3 2014 20:08:51 PST/Nov 4 2014 04:08:51)                                                                                                   
#Before trips 253-373                                                                                                                                                                                              
#After trips 374-494                                                                                                                                                                                               

from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


print "Import Module Success"

H1CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_H1_IN1_DQ', 1099109347.275391, 1099109347.575391)
H2CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_H2_IN1_DQ', 1099109347.275391, 1099109347.575391)
V1CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_V1_IN1_DQ', 1099109347.275391, 1099109347.575391)
V2CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_V2_IN1_DQ', 1099109347.275391, 1099109347.575391)

print "Data Fetched"

plot_H1 = H1CPS.plot()
ax = plot_H1.gca()
ax.plot(H2CPS, label='H1:ISI-ITMX\_ST1\_CPSINF\_H2\_IN1\_DQ')
ax.plot(V1CPS, label='H1:ISI-ITMX\_ST1\_CPSINF\_V1\_IN1\_DQ')
ax.plot(V2CPS, label='H1:ISI-ITMX\_ST1\_CPSINF\_V2\_IN1\_DQ')
ax.set_ylim(-25000,10000)
mj  = MultipleLocator(2000)
ml1 = MultipleLocator(50)
ml2 = MultipleLocator(1000)
ax.yaxis.set_major_locator(mj)
ax.yaxis.set_minor_locator(ml2)
ax.xaxis.set_minor_locator(ml1)

L = ax.legend(loc='upper right',  ncol=1, fancybox=True, shadow=True)
ax.grid(True, which='both', axis='both')

print 'plotting'

plot_H1.show()
