from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-30 00:00:00', format='iso', scale='utc')
end = Time('2014-12-01 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

LF = TimeSeries.fetch('L1:SUS-ITMY_M0_OSEMINF_LF_OUT_DQ.mean,m-trend', start, end, verbose=True)
RT = TimeSeries.fetch('L1:SUS-ITMY_M0_OSEMINF_RT_OUT_DQ.mean,m-trend', start, end, verbose=True)
F1 = TimeSeries.fetch('L1:SUS-ITMY_M0_OSEMINF_F1_OUT_DQ.mean,m-trend', start, end, verbose=True)
F2 = TimeSeries.fetch('L1:SUS-ITMY_M0_OSEMINF_F2_OUT_DQ.mean,m-trend', start, end, verbose=True)
F3 = TimeSeries.fetch('L1:SUS-ITMY_M0_OSEMINF_F3_OUT_DQ.mean,m-trend', start, end, verbose=True)
SD = TimeSeries.fetch('L1:SUS-ITMY_M0_OSEMINF_SD_OUT_DQ.mean,m-trend', start, end, verbose=True)

print 'data fetched'

plot_LF = LF.plot()
ax = plot_LF.gca()

ax.plot(RT, label = 'L1:SUS-ITMY\_M0\_OSEMINF\_RT\_OUT\_DQ.mean')
ax.plot(F1, label = 'L1:SUS-ITMY\_M0\_OSEMINF\_F1\_OUT\_DQ.mean')
ax.plot(F2, label = 'L1:SUS-ITMY\_M0\_OSEMINF\_F2\_OUT\_DQ.mean')
ax.plot(F3, label = 'L1:SUS-ITMY\_M0\_OSEMINF\_F3\_OUT\_DQ.mean')
ax.plot(SD, label = 'L1:SUS-ITMY\_M0\_OSEMINF\_SD\_OUT\_DQ.mean')

ax.set_ylabel('um')
ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)

print 'plotting'

plot_LF.show()
