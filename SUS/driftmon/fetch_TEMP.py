from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

#Start-End Time 
start = Time('2014-06-29 00:00:00', format='iso', scale='utc')
end = Time('2014-07-02 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

data1 = TimeSeries.fetch('L0:FMC-EY_VEA_202A_TEMP.mean,m-trend', start, end, verbose=True)
data2 = TimeSeries.fetch('L0:FMC-EY_VEA_202B_TEMP.mean,m-trend', start, end, verbose=True)
data3 = TimeSeries.fetch('L0:FMC-EY_VEA_202C_TEMP.mean,m-trend', start, end, verbose=True)
data4 = TimeSeries.fetch('L0:FMC-EY_VEA_202D_TEMP.mean,m-trend', start, end, verbose=True)
data5 = TimeSeries.fetch('L0:FMC-EY_VEA_202_AVTEMP.mean,m-trend', start, end, verbose=True)
#data6 = TimeSeries.fetch('L0:FMC-EX_VEA_AVTEMP.mean,m-trend', start, end, verbose=True)

plot_TEMP = data1.plot()
ax = plot_TEMP.gca()
ax.plot(data2, label = 'L0:FMC-EY\_VEA\_202B\_AVTEMP.mean')
ax.plot(data3, label = 'L0:FMC-EY\_VEA\_202C\_AVTEMP.mean')
ax.plot(data4, label = 'L0:FMC-EY\_VEA\_202D\_AVTEMP.mean')
ax.plot(data5, label = 'L0:FMC-EY\_VEA\_AVTEMP.mean')
#ax.plot(data6, label = 'L0:FMC-EX\_VEA\_AVTEMP.mean')

ax.set_epoch(start.gps)
ax.set_xlim(start.gps, end.gps)
ax.set_ylabel('Temperature (F)')
ax.set_title('EY Temperature')
ax.set_ylim([62,64.5])
ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
plot_TEMP.save('L0-FMC-EY_VEA_TEMP_3days.png')
print "PLOT SAVED"

#TEMP CHANNEL LIST
#[EX]
#L0:FMC-EX_VEA_302A_TEMP
#L0:FMC-EX_VEA_302B_TEMP
#L0:FMC-EX_VEA_302C_TEMP 
#L0:FMC-EX_VEA_302D_TEMP 
#L0:FMC-EX_VEA_302_AVTEMP

#[EY]
#L0:FMC-EY_VEA_202A_TEMP 16
#L0:FMC-EY_VEA_202B_TEMP 16
#L0:FMC-EY_VEA_202C_TEMP 16
#L0:FMC-EY_VEA_202D_TEMP 16
#L0:FMC-EY_VEA_202_AVTEMP 16 

#[CS]
#L0:FMC-CS_LVEA_ZONE1_AVTEMP 
#L0:FMC-CS_LVEA_ZONE2_AVTEMP
#L0:FMC-CS_LVEA_ZONE3_AVTEMP
#L0:FMC-CS_LVEA_ZONE4_AVTEMP
#L0:FMC-CS_LVEA_ZONE5_AVTEMP
#L0:FMC-CS_LVEA_AVTEMP
