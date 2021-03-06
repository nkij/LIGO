from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-30 00:00:00', format='iso', scale='utc')
end = Time('2014-12-01 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

ITMY = TimeSeries.fetch('L1:SUS-ITMY_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)

print "data fetched"

plot_ITMY = ITMY.plot()

ax = plot_ITMY.gca()

#ax.set_ylim(-90,-50)
ax.set_ylabel('um')
#ax.set_title('SUS-ITMY\_M0\_DAMP\_V\_IN1\_DQ (4 days)')
ax.legend(loc='upper right',  ncol=1, fancybox=True, shadow=True)
ax.grid(True, which='both', axis='both')

print 'plotting'

plot_ITMY.show()
