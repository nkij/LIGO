from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

#Start-End Time                                                                 
start = Time('2014-06-14 04:00:00', format='iso', scale='utc')
end = Time('2014-06-14 06:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

channels = ['L1:HPI-ITMX_BLND_IPS_HP_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_RX_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_RY_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_RZ_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_VP_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_X_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_Y_IN1_DQ.mean, m-trend',
'L1:HPI-ITMX_BLND_IPS_Z_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_HP_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_RX_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_RY_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_RZ_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_VP_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_X_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_Y_IN1_DQ.mean, m-trend',
'L1:HPI-ITMY_BLND_IPS_Z_IN1_DQ.mean, m-trend',
'L1:HPI-ETMX_BLND_IPS_HP_IN1_DQ.mean, m-trend',
'L1:HPI-ETMX_BLND_IPS_RX_IN1_DQ.mean, m-trend',
'L1:HPI-ETMX_BLND_IPS_RY_IN1_DQ.mean, m-trend', 
'L1:HPI-ETMX_BLND_IPS_RZ_IN1_DQ.mean, m-trend',
'L1:HPI-ETMX_BLND_IPS_VP_IN1_DQ.mean, m-trend',
'L1:HPI-ETMX_BLND_IPS_X_IN1_DQ.mean, m-trend', 
'L1:HPI-ETMX_BLND_IPS_Y_IN1_DQ.mean, m-trend',
'L1:HPI-ETMX_BLND_IPS_Z_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_HP_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_RX_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_RY_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_RZ_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_VP_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_X_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_Y_IN1_DQ.mean, m-trend',
'L1:HPI-ETMY_BLND_IPS_Z_IN1_DQ.mean, m-trend']

#data = dict()
data = TimeSeriesDict.fetch(channels, start, end, verbose=True)

print "DONE"

#for data in channles:
#    plot_data = data.plot()
#    ax = plot_data.gca()

#    ax.set_epoch(start.gps)
#    ax.set_xlim(start.gps, end.gps)
#    ax.set_ylabel('Amplitude[ ]')
#    ax.set_title(data.channel.texname)
#    ax.set_ylim([20000,30000])
 
#    print "DONE"
#    plot_data.save(data.channel.text)
#    print "PLOT SAVED"
 
