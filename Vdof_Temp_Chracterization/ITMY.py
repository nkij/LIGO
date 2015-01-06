from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from gwpy.plotter import TimeSeriesPlot
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-29 00:00:00', format='iso', scale='utc')
end = Time('2014-11-30 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

#TCS = TimeSeries.fetch('L1:TCS-ITMY_HWS_CHAMBERTEMPERATURESENSORB.mean,m-trend', start, end, verbose=True)
RH = TimeSeries.fetch('L1:TCS-ITMY_RH_LOWERRTD.mean,m-trend', start, end, verbose=True)
ITMY = TimeSeries.fetch('L1:SUS-ITMY_M0_DAMP_V_IN1_DQ.mean,m-trend', start, end, verbose=True)
