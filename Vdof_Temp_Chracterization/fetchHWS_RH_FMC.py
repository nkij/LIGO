from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 21:00:00', format='iso', scale='utc')
end = Time('2014-12-01 21:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

FMC = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE1_TP2.mean,m-trend', start, end, verbose=True) #closest to ITMX and HAM4
HWS = TimeSeries.fetch('L1:TCS-ITMY_HWS_CHAMBERTEMPERATURESENSORB.mean,m-trend', start, end, verbose=True) #HAM4
RH = TimeSeries.fetch('L1:TCS-ITMX_RH_LOWERRTD.mean,m-trend', start, end, verbose=True) #assume that ITMX means ITMX

print "data-fetched"

FMC_C = (FMC-32)*(5.0/9)
plot = FMC_C.plot()
ax = plot.gca()
ax.plot(HWS, label='L1:TCS-ITMY\_HWS\_CHAMBERTEMPERATURESENSORB.mean')
ax.plot(RH, label = 'L1:TCS-ITMX\_RH\_LOWERRTD.mean')
#ax.set_ylim()
ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)

print ' plotting'

plot.show()
