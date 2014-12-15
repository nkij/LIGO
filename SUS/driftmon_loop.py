import matplotlib.pyplot as plt
from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

print "Import Modules Success"

#Start-End Time 
start = Time('2014-04-06 00:00:00', format='iso', scale='utc')
end = Time('2014-04-07 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

channels_M0 = []
channels_M1 = []
OPTICS_M0 = ['ETMX','ITMX','ITMY']
OPTICS_M1 = ['BS', 'MC1', 'MC2', 'MC3', 'PR2', 'PR3', 'PRM', 'SR2', 'SR3', 'SRM' ]
DOFS = ['P', 'R', 'Y']

# loop over list of optics
for optic_m0 in OPTICS_M0:
    # loop over list of degrees-of-freedom
    for dof in DOFS:
        channels_M0.append('L1:SUS-%s_M0_DAMP_%s_INMON.rms,m-trend' % (optic_m0, dof))

# loop over list of optics
for optic_m1 in OPTICS_M1:
    # loop over list of degrees-of-freedom
    for dof in DOFS:
        channels_M1.append('L1:SUS-%s_M1_DAMP_%s_INMON.rms,m-trend' % (optic_m1, dof))

data_m0 = TimeSeriesDict.fetch(channels_M0, start, end, verbose=True)
data_m1 = TimeSeriesDict.fetch(channels_M1, start, end, verbose=True)


data_m1_BS_P = data_m1[channels_M1[0]]
data_m1_BS_R = data_m1[channels_M1[1]]
data_m1_BS_Y = data_m1[channels_M1[2]]
plot_BS_P = data_m1_BS_P.plot()
axBS = plot_BS_P.gca()
axBS.plot(data_m1_BS_R, label='Roll (x10)')
axBS.plot(data_m1_BS_Y, label='Yaw (x10)')
axBS.set_ylabel('Amplitude (urad)')
L = axBS.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axBS.yaxis.set_minor_locator(ml1)
axBS.xaxis.set_minor_locator(ml2)
plot_BS_P.save('L1-SUS-BS_M1_DAMP_PRY_INMON.png')
