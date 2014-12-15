#This program fetch data MC1 only
#Repeat and change date manually as necessary
import matplotlib.pyplot as plt
from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pylab
print "Import Modules Success"

#Start-End Time 
start = Time('2014-04-05 00:00:00', format='iso', scale='utc')
end = Time('2014-04-10 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps


channels_M1 = []
OPTICS_M1 = ['MC1']
DOFS = ['P', 'R', 'Y']
TRENDS = ['min','mean','max']


for optic_m1 in OPTICS_M1:
    for dof in DOFS:
        for trend in TRENDS:
            channels_M1.append('L1:SUS-%s_M1_DAMP_%s_INMON.%s,m-trend' % (optic_m1, dof, trend))


data_m1 = TimeSeriesDict.fetch(channels_M1, start, end, verbose=True)

for optic_m1 in OPTICS_M1:
    print "%s " %(optic_m1)
    for dof in DOFS:
        print "%s  " %(dof)
        data_m1_mean = data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.mean,m-trend' % (optic_m1, dof)]-data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.mean,m-trend' % (optic_m1, dof)][[720]]
        data_m1_min = data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.min,m-trend' % (optic_m1, dof)]-data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.min,m-trend' % (optic_m1, dof)][[720]]
        data_m1_max = data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.max,m-trend' % (optic_m1, dof)]-data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.max,m-trend' % (optic_m1, dof)][[720]]
        plot_m1_min = data_m1_min.plot()
        axP = plot_m1_min.gca()
        axP.plot(data_m1_mean, label='Mean')
        axP.plot(data_m1_max, label='Max')
        axP.set_ylabel('Amplitude - 12th hour Value (urad)')
        axP.set_title('05 April - 10 April 2014 %s %s' %(optic_m1, dof))
        pylab.ylim([-200,200])
        L = axP.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
        L.get_texts()[0].set_text('Min')
        ml1 = MultipleLocator(10)
        ml2 = MultipleLocator(3600)
        axP.yaxis.set_minor_locator(ml1)
        axP.xaxis.set_minor_locator(ml2)
        plot_m1_min.save('L1-SUS-%s_M1_DAMP_%smmm_INMON_05-10.png' % (optic_m1, dof))
        print "PLOT SAVED"



