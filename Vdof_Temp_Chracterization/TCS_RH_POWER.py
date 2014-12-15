from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 21:00:00', format='iso', scale='utc')
end = Time('2014-12-01 21:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

ITMY_RH_POWER = TimeSeries.fetch('L1:TCS-ITMY_RH_LOWERPOWER.mean, m-trend', start, end, verbose=True) 
print 'data fetched'

plot_power = ITMY_RH_POWER.plot()
ax = plot_power.gca()

ax.set_ylabel('Power []')
print ' plotting'

plot_power.show()
