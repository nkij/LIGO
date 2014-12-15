import matplotlib.pyplot as plt
from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pylab
print "Import Modules Success"

#Start-End Time 
start = Time('2014-03-24 00:00:00', format='iso', scale='utc')
end = Time('2014-03-30 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps


channels_M0 = []
channels_M1 = []
OPTICS_M0 = ['ETMX','ITMX','ITMY']
OPTICS_M1 = ['BS', 'MC1', 'MC2', 'MC3', 'PR2', 'PR3', 'PRM', 'SR2', 'SR3', 'SRM' ]
DOFS = ['P', 'R', 'Y']
TRENDS = ['min','mean','max']

#f=open('test.txt','wb')

# loop over list of optics                                                      
for optic_m0 in OPTICS_M0:
    # loop over list of degrees-of-freedom                                      
    for dof in DOFS:
        for trend in TRENDS:
            channels_M0.append('L1:SUS-%s_M0_DAMP_%s_INMON.%s,m-trend' % (optic_m0, dof, trend))

# loop over list of optics                                                      
for optic_m1 in OPTICS_M1:
    # loop over list of degrees-of-freedom                                      
    for dof in DOFS:
        for trend in TRENDS:
            channels_M1.append('L1:SUS-%s_M1_DAMP_%s_INMON.%s,m-trend' % (optic_m1, dof, trend))

data_m1 = TimeSeriesDict.fetch(channels_M1, start, end, verbose=True)

data_m1_MC1_Pmin = data_m1[channels_M1[9]]-data_m1[channels_M1[9]][[720]]
data_m1_MC1_Pmean = data_m1[channels_M1[10]]-data_m1[channels_M1[10]][[720]]
data_m1_MC1_Pmax = data_m1[channels_M1[11]]-data_m1[channels_M1[11]][[720]]
plot_MC1_Pmin = data_m1_MC1_Pmin.plot()
axMC1P = plot_MC1_Pmin.gca()
axMC1P.plot(data_m1_MC1_Pmean, label='Mean')
axMC1P.plot(data_m1_MC1_Pmax, label='Max')
axMC1P.set_ylabel('Amplitude (urad)')
pylab.ylim([-200,200])
L = axMC1P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC1P.yaxis.set_minor_locator(ml1)
axMC1P.xaxis.set_minor_locator(ml2)
plot_MC1_Pmin.save('L1-SUS-MC1_M1_DAMP_Pmmm_INMON.png')

data_m1_MC1_Rmin = data_m1[channels_M1[12]]-data_m1[channels_M1[12]][[720]]
data_m1_MC1_Rmean = data_m1[channels_M1[13]]-data_m1[channels_M1[13]][[720]]
data_m1_MC1_Rmax = data_m1[channels_M1[14]]-data_m1[channels_M1[14]][[720]]
plot_MC1_Rmin = data_m1_MC1_Rmin.plot()
axMC1R = plot_MC1_Rmin.gca()
axMC1R.plot(data_m1_MC1_Rmean, label='Mean')
axMC1R.plot(data_m1_MC1_Rmax, label='Max')
axMC1R.set_ylabel('Amplitude (urad)')
pylab.ylim([-200,200])
L = axMC1R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC1R.yaxis.set_minor_locator(ml1)
axMC1R.xaxis.set_minor_locator(ml2)
plot_MC1_Rmin.save('L1-SUS-MC1_M1_DAMP_Rmmm_INMON.png')


data_m1_MC1_Ymin = data_m1[channels_M1[15]]-data_m1[channels_M1[15]][[720]]
data_m1_MC1_Ymean = data_m1[channels_M1[16]]-data_m1[channels_M1[16]][[720]]
data_m1_MC1_Ymax = data_m1[channels_M1[17]]-data_m1[channels_M1[17]][[720]]
plot_MC1_Ymin = data_m1_MC1_Ymin.plot()
axMC1Y = plot_MC1_Ymin.gca()
axMC1Y.plot(data_m1_MC1_Ymean, label='Mean')
axMC1Y.plot(data_m1_MC1_Ymax, label='Max')
axMC1Y.set_ylabel('Amplitude (urad)')
pylab.ylim([-200,200])
L = axMC1Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC1Y.yaxis.set_minor_locator(ml1)
axMC1Y.xaxis.set_minor_locator(ml2)
plot_MC1_Ymin.save('L1-SUS-MC1_M1_DAMP_Ymmm_INMON.png')


