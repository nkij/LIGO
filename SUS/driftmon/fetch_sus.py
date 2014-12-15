from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

#Start-End Time                                                                                                                                     
start = Time('2014-06-29 00:00:00', format='iso', scale='utc')
end = Time('2014-07-02 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

data1 = TimeSeries.fetch('L1:SUS-ITMX_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
data2 = TimeSeries.fetch('L1:SUS-ITMY_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)


plot_SUS = data1.plot()
ax = plot_SUS.gca()
ax.plot(data2, label = 'L1:SUS-ITMY\_M0\_DAMP\_V\_IN1\_DQ.mean')
#plot_data.show() 

ax.set_epoch(start.gps)
ax.set_xlim(start.gps, end.gps)
ax.set_ylabel('Amplitude (um)')
ax.set_title('SUS CS Vertical Position trends')
#ax.set_ylim([-1,1])
ax.legend(loc='lower left', ncol=1, fancybox=True, shadow=True)
plot_SUS.save('SUS-CS-Vertical-3days.png')

print "PLOT SAVED"


# Channel name format
# QUAD first stage L1:SUS-ITMX_M0_DAMP_Y_IN1_DQ
# QUAD final stage L1:SUS-ITMX_L3_OPLEV_PIT_OUT_DQ
