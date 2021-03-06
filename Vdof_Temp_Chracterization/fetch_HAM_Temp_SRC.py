#This script compares HAM4 (SR2), HAM5 (SR3, SRM) in-chamber temp to V dof SR2 (HSTS), SRM (HSTS), SR3 (HLTS)

from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from gwpy.plotter import TimeSeriesPlot
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 21:00:00', format='iso', scale='utc')
end = Time('2014-12-01 21:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

SR2 = TimeSeries.fetch('L1:SUS-SR2_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
SR3 = TimeSeries.fetch('L1:SUS-SR3_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
SRM = TimeSeries.fetch('L1:SUS-SRM_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
TCS_HAM4 = TimeSeries.fetch('L1:TCS-ITMY_HWS_CHAMBERTEMPERATURESENSORA.mean,m-trend', start, end, verbose=True)
TCS_HAM5 = TimeSeries.fetch('L1:TCS-ITMX_HWS_CHAMBERTEMPERATURESENSORA.mean,m-trend', start, end, verbose=True)

print 'data fetched'

plot_HAM4 = TimeSeriesPlot(TCS_HAM4, SR2, sep=True)
ax1 = plot_HAM4.axes[0]  #plot TCS_HAM4
ax1.plot(TCS_HAM5, label='L1:TCS-ITMX\_HWS\_CHAMBERTEMPERATURESENSORA.mean') #plot TCS_HAM5
#ax1.lines[0].set_color('red')
ax1.set_ylim(18,18.6)
ax1.set_ylabel('C')
ax1.set_title('(HWS) Temperature vs. SRC (4 days)')
ax1.legend(loc='upper right',  ncol=1, fancybox=True, shadow=True) 
ax1.grid(True, which='both', axis='both') # add more grid   
#mj  = MultipleLocator(1)
ml1 = MultipleLocator(0.1)
#ax1.yaxis.set_major_locator(mj)
ax1.yaxis.set_minor_locator(ml1)

ax2 = plot_HAM4.axes[1]  #plotSR2
ax2.plot(SR3, label = 'L1:SUS-SR3\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax2.plot(SRM, label = 'L1:SUS-SRM\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax2.set_ylim(-30,100)
ax2.set_ylabel('um')
ax2.legend(loc='upper right',  ncol=2, fancybox=True, shadow=True)
ax2.grid(True, which='both', axis='both') # add more grid
#mj  = MultipleLocator(1)
#ml2 = MultipleLocator(0.1)
#ax1.yaxis.set_major_locator(mj)
#ax2.yaxis.set_minor_locator(ml1)

print 'plotting'

plot_HAM4.show()
