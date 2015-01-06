from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from gwpy.plotter import TimeSeriesPlot
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 21:00:00', format='iso', scale='utc')
end = Time('2014-12-01 21:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

#TCS = TimeSeries.fetch('L1:TCS-ITMY_HWS_CHAMBERTEMPERATURESENSORB.mean,m-trend', start, end, verbose=True)
RH = TimeSeries.fetch('L1:TCS-ITMY_RH_LOWERRTD.mean,m-trend', start, end, verbose=True)
ITMY = TimeSeries.fetch('L1:SUS-ITMY_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)

print 'data fetched'

plot = TimeSeriesPlot(RH, ITMY, sep=True)

ax2 = plot.axes[0]
ax2.set_ylim(18.4,19.4)
ax2.set_ylabel('C')
ax2.legend(loc='upper right',  ncol=1, fancybox=True, shadow=True)
ax2.grid(True, which='both', axis='both') # add more grid
ax2.set_title('(RH) Temperature vs. ITMY\_V (4 days)')
mj  = MultipleLocator(0.1)
ml2 = MultipleLocator(0.1)
#ax1.yaxis.set_major_locator(mj)
ax2.yaxis.set_minor_locator(ml2)

ax1 = plot.axes[1]
ax1.set_ylim(-90,-55)
ax1.set_ylabel('um')
ax1.lines[0].set_color('red')
ax1.legend(loc='upper right',  ncol=1, fancybox=True, shadow=True)
ax1.grid(True, which='both', axis='both') # add more grid                                                                                         
#mj  = MultipleLocator(2)                                                                                                                         
ml1 = MultipleLocator(1)
#ax1.yaxis.set_major_locator(mj)                                                                                                                  
ax1.yaxis.set_minor_locator(ml1)

print 'plotting'

plot.show()
