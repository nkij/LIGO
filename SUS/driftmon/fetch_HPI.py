from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

#Start-End Time                                                                 

start = Time('2014-06-17 04:00:00', format='iso', scale='utc')
end = Time('2014-06-17 15:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

data = TimeSeries.fetch('L1:HPI-ETMY_BLND_IPS_Z_IN1_DQ.mean,m-trend', start, end, verbose=True)

plot_data = data.plot()
ax = plot_data.gca()
#plot_data.show()                                                               

ax.set_epoch(start.gps)
ax.set_xlim(start.gps, end.gps)
ax.set_ylabel('Amplitude[ ]')
ax.set_title(data.channel.texname)
#ax.set_ylim([20000,30000])
                                                                                

plot_data.save('L1-HPI-ETMY_BLND_IPS_Z_IN1_DQ_JUN14.png')
print "PLOT SAVED"



#L1:HPI-ITMX_BLND_IPS_HP_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_RX_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_RY_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_RZ_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_VP_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_X_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_Y_IN1_DQ - PLOT SAVED
#L1:HPI-ITMX_BLND_IPS_Z_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_HP_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_RX_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_RY_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_RZ_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_VP_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_X_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_Y_IN1_DQ - PLOT SAVED
#L1:HPI-ITMY_BLND_IPS_Z_IN1_DQ - PLT SAVED
#L1:HPI-ETMX_BLND_IPS_HP_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_RX_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_RY_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_RZ_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_VP_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_X_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_Y_IN1_DQ 
#L1:HPI-ETMX_BLND_IPS_Z_IN1_DQ 
#L1:HPI-ETMY_BLND_IPS_HP_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_RX_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_RY_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_RZ_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_VP_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_X_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_Y_IN1_DQ
#L1:HPI-ETMY_BLND_IPS_Z_IN1_DQ
