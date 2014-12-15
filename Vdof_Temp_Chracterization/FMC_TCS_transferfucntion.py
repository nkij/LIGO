from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 20:00:00', format='iso', scale='utc')
end = Time('2014-11-28 20:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

FMC = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE1_TP4', start, end, verbose=True)
TCS = TimeSeries.fetch('L1:TCS-ITMY_HWS_CHAMBERTEMPERATURESENSORA', start, end, verbose=True)

print 'data fetched'

FMC_C = (FMC-32)*(5.0/9)

FMC_asd = FMC.asd(1000,500)
TCS_asd = TCS.asd(1000,500)

ratio = FMC_asd/TCS_asd
ratio_plot = ratio.plot(color = 'black', label = 'FMC asd/TCS asd')

ax = ratio_plot.gca()
ax.plot(FMC_asd, label = 'FMC-CS\_LVEA\_ZONE1\_TP4')
ax.plot(TCS_asd, label = 'L1:TCS-ITMY\_HWS\_CHAMBERTEMPERATURESENSORA')
ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude [ ]')
ax.set_title('1000 FFT')

ratio_plot.show()

