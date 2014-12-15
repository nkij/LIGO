#This program fetches m-trend data of MC1 MC2 and MC3 and overplot.
import matplotlib.pyplot as plt
from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pylab
print "Import Modules Success"

#Start-End Time 
start = Time('2014-03-24 00:00:00', format='iso', scale='utc')
end = Time('2014-03-29 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps



channels_M1 = []
OPTICS_M1 = ['MC1', 'MC2', 'MC3']
DOFS = ['P', 'R', 'Y']


for optic_m1 in OPTICS_M1:
    for dof in DOFS:
        channels_M1.append('L1:SUS-%s_M1_DAMP_%s_INMON.mean,m-trend' % (optic_m1, dof))



data_m1 = TimeSeriesDict.fetch(channels_M1, start, end, verbose=True)


for dof in DOFS:
    print "DOF = %s  " %(dof)
    data_mc1_mean = data_m1['L1:SUS-MC1_M1_DAMP_%s_INMON.mean,m-trend' % (dof)]-data_m1['L1:SUS-MC1_M1_DAMP_%s_INMON.mean,m-trend' % (dof)].mean().value
    data_mc2_mean = data_m1['L1:SUS-MC2_M1_DAMP_%s_INMON.mean,m-trend' % (dof)]-data_m1['L1:SUS-MC2_M1_DAMP_%s_INMON.mean,m-trend' % (dof)].mean().value
    data_mc3_mean = data_m1['L1:SUS-MC3_M1_DAMP_%s_INMON.mean,m-trend' % (dof)]-data_m1['L1:SUS-MC3_M1_DAMP_%s_INMON.mean,m-trend' % (dof)].mean().value
    plot_mc1_mean = data_mc1_mean.plot()
    ax = plot_mc1_mean.gca()
    ax.plot(data_mc2_mean, label='MC2')
    ax.plot(data_mc3_mean, label='MC3')
    ax.set_ylabel('Mean amplitude - Mean Value (urad)')
    ax.set_title('%s' %(dof))
    pylab.ylim([-200,200])
    L = ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
    L.get_texts()[0].set_text('MC1')
    ml1 = MultipleLocator(10)
    ml2 = MultipleLocator(3600)
    ax.yaxis.set_minor_locator(ml1)
    ax.xaxis.set_minor_locator(ml2)
    plot_mc1_mean.save('L1-SUS-MC1_MC2_MC3_M1_DAMP_%smmm_INMON.png' % (dof))
    print "PLOT SAVED"
