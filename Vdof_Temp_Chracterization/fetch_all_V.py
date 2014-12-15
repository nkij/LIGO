from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 21:00:00', format='iso', scale='utc')
end = Time('2014-12-01 21:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

ITMY = TimeSeries.fetch('L1:SUS-ITMY_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
ITMX = TimeSeries.fetch('L1:SUS-ITMX_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
MC1 = TimeSeries.fetch('L1:SUS-MC1_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
MC2 = TimeSeries.fetch('L1:SUS-MC2_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
MC3 = TimeSeries.fetch('L1:SUS-MC3_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
BS = TimeSeries.fetch('L1:SUS-BS_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
PR2 = TimeSeries.fetch('L1:SUS-PR2_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
PR3 = TimeSeries.fetch('L1:SUS-PR3_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
PRM = TimeSeries.fetch('L1:SUS-PRM_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
SR2 = TimeSeries.fetch('L1:SUS-SR2_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
SR3 = TimeSeries.fetch('L1:SUS-SR3_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
SRM = TimeSeries.fetch('L1:SUS-SRM_M1_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)

print "data fetched"

plot_ITMY = ITMY.plot()

ax = plot_ITMY.gca()

ax.set_ylim(-100,120)
ax.plot(ITMX, label = 'L1:SUS-ITMX\_M0\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(MC1, label = 'L1:SUS-MC1\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(MC2, label = 'L1:SUS-MC2\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(MC3, label = 'L1:SUS-MC3\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(BS, label = 'L1:SUS-BS\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(PR2, label = 'L1:SUS-PR2\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(PR3, label = 'L1:SUS-PR3\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(PRM, label = 'L1:SUS-PRM\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(SR2, label = 'L1:SUS-SR2\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(SR3, label = 'L1:SUS-SR3\_M1\_DAMP\_V\_IN1\_DQ.mean')
ax.plot(SRM, label = 'L1:SUS-SRM\_M1\_DAMP\_V\_IN1\_DQ.mean')


ax.set_title('SUS Vdof (4 days)')
ax.legend(loc='upper center',  ncol=3, fancybox=True, shadow=True)
ax.grid(True, which='both', axis='both')

print 'plotting'

plot_ITMY.show()
