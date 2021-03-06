from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

#Start-End Time  
 
start = Time('2014-06-11 21:00:00', format='iso', scale='utc')
end = Time('2014-06-15 07:36:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

data = TimeSeries.fetch('L1:ALS-C_TRX_A_LF_OUT_DQ.mean,m-trend', start, end, verbose=True)

plot_data = data.plot()
ax = plot_data.gca()
#plot_data.show()

ax.set_epoch(start.gps)
ax.set_xlim(start.gps, end.gps)
ax.set_ylabel('Counts')
ax.set_title(data.channel.texname)
#ax.set_ylim([15000,25000])              

plot_data.save('L1-ALS-C_TRX_A_LF_OUT_DQ_HEPI-ON.png')
print "PLOT SAVED"

# Channel List
# L1:ALS-C_TRY_A_LF_OUT_DQ - Green Laser Y
# L1:ALS-C_TRX_A_LF_OUT_DQ - Green Laser X
# L1:LSC-X_TR_A_LF_OUT_DQ - Red Laser X
# L1:LSC-Y_TR_A_LF_OUT_DQ - Red Laser Y
