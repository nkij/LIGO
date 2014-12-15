#This program fetches m-trend data of the top stages of all the optics. Subtract the value by its own mean value.
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


channels_M0 = []
channels_M1 = []
channels_M2 = []
channels_M3 = []
OPTICS_M0 = ['ETMX','ITMX','ITMY']
OPTICS_M1 = ['BS', 'MC1', 'MC2', 'MC3', 'PR2', 'PR3', 'PRM', 'SR2', 'SR3', 'SRM' ]
OPTICS_M2 = ['MC1']
DOFS = ['P', 'R', 'Y']
DOFS2 = ['P', 'Y']
TRENDS = ['min','mean','max']


for optic_m0 in OPTICS_M0:
    for dof in DOFS:
        for trend in TRENDS:
            channels_M0.append('L1:SUS-%s_M0_DAMP_%s_INMON.%s,m-trend' % (optic_m0, dof, trend))

for optic_m1 in OPTICS_M1:
    for dof in DOFS:
        for trend in TRENDS:
            channels_M1.append('L1:SUS-%s_M1_DAMP_%s_INMON.%s,m-trend' % (optic_m1, dof, trend))

for optic_m2 in OPTICS_M2:
    for dof2 in DOFS2:
        for trend in TRENDS:
            channels_M2.append('L1:SUS-%s_M2_WIT_%s_DQ.%s,m-trend' % (optic_m2, dof2, trend))
            channels_M3.append('L1:SUS-%s_M3_WIT_%s_DQ.%s,m-trend' % (optic_m2, dof2, trend))



data_m0 = TimeSeriesDict.fetch(channels_M0, start, end, verbose=True)
data_m1 = TimeSeriesDict.fetch(channels_M1, start, end, verbose=True)
data_m2 = TimeSeriesDict.fetch(channels_M2, start, end, verbose=True)
data_m3 = TimeSeriesDict.fetch(channels_M3, start, end, verbose=True)

#x=0
#xlist=[]
#while x <= 87:
#    xlist.append(x)
#    x+=3

for optic_m1 in OPTICS_M1:
    print "%s " %(optic_m1)
    for dof in DOFS:
        print "%s  " %(dof)
        data_m1_mean = data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.mean,m-trend' % (optic_m1, dof)]
        data_m1_min = data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.min,m-trend' % (optic_m1, dof)]-data_m1_mean
        data_m1_max = data_m1['L1:SUS-%s_M1_DAMP_%s_INMON.max,m-trend' % (optic_m1, dof)]-data_m1_mean
        plot_m1_min = data_m1_min.plot()
        axP = plot_m1_min.gca()
        axP.plot(data_m1_mean-data_m1_mean, label='Mean')
        axP.plot(data_m1_max, label='Max')
        axP.set_ylabel('Amplitude - Mean Value (urad)')
        axP.set_title('%s %s' %(optic_m1, dof))
        pylab.ylim([-200,200])
        L = axP.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
        L.get_texts()[0].set_text('Min')
        ml1 = MultipleLocator(10)
        ml2 = MultipleLocator(3600)
        axP.yaxis.set_minor_locator(ml1)
        axP.xaxis.set_minor_locator(ml2)
        plot_m1_min.save('L1-SUS-%s_M1_DAMP_%smmm_INMON.png' % (optic_m1, dof))
        print "PLOT SAVED"


for optic_m0 in OPTICS_M0:
    print "%s " %(optic_m0)
    for dof in DOFS:
        print "%s  " %(dof)
        data_m0_mean = data_m0['L1:SUS-%s_M0_DAMP_%s_INMON.mean,m-trend' % (optic_m0, dof)]
        data_m0_min = data_m0['L1:SUS-%s_M0_DAMP_%s_INMON.min,m-trend' % (optic_m0, dof)]-data_m0_mean
        data_m0_max = data_m0['L1:SUS-%s_M0_DAMP_%s_INMON.max,m-trend' % (optic_m0, dof)]-data_m0_mean
        plot_m0_min = data_m0_min.plot()
        axP0 = plot_m0_min.gca()
        axP0.plot(data_m0_mean-data_m0_mean, label='Mean')
        axP0.plot(data_m0_max, label='Max')
        axP0.set_ylabel('Amplitude - Mean value (urad)')
        axP0.set_title('%s %s' %(optic_m0, dof))
        pylab.ylim([-200,200])
        L = axP0.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
        L.get_texts()[0].set_text('Min')
        ml1 = MultipleLocator(10)
        ml2 = MultipleLocator(3600)
        axP0.yaxis.set_minor_locator(ml1)
        axP0.xaxis.set_minor_locator(ml2)
        plot_m0_min.save('L1-SUS-%s_M0_DAMP_%smmm_INMON.png' % (optic_m0, dof))
        print "PLOT SAVED"


for optic_m2 in OPTICS_M2:
    print "%s " %(optic_m2)
    for dof2 in DOFS2:
        print "%s  " %(dof2)
        data_m2_mean = data_m2['L1:SUS-%s_M2_WIT_%s_DQ.mean,m-trend' % (optic_m2, dof)]
        data_m2_min = data_m2['L1:SUS-%s_M2_WIT_%s_DQ.min,m-trend' % (optic_m2, dof)]-data_m2_mean
        data_m2_max = data_m2['L1:SUS-%s_M2_WIT_%s_DQ.max,m-trend' % (optic_m2, dof)]-data_m2_mean
        plot_m2_min = data_m2_min.plot()
        axP2 = plot_m2_min.gca()
        axP2.plot(data_m2_mean-data_m2_mean, label='Mean')
        axP2.plot(data_m2_max, label='Max')
        axP2.set_ylabel('Amplitude - Mean value (urad)')
        axP2.set_title('%s %s' %(optic_m2, dof))
        pylab.ylim([-200,200])
        L = axP2.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
        L.get_texts()[0].set_text('Min')
        ml1 = MultipleLocator(10)
        ml2 = MultipleLocator(3600)
        axP2.yaxis.set_minor_locator(ml1)
        axP2.xaxis.set_minor_locator(ml2)
        plot_m2_min.save('L1-SUS-%s_M2_WIT_%smmm_DQ.png' % (optic_m2, dof2))
        print "PLOT SAVED"


for optic_m2 in OPTICS_M2:
    print "%s " %(optic_m2)
    for dof2 in DOFS2:
        print "%s  " %(dof2)
        data_m3_mean = data_m3['L1:SUS-%s_M3_WIT_%s_DQ.mean,m-trend' % (optic_m2, dof2)]
        data_m3_min = data_m3['L1:SUS-%s_M3_WIT_%s_DQ.min,m-trend' % (optic_m2, dof2)]-data_m3_mean
        data_m3_max = data_m3['L1:SUS-%s_M3_WIT_%s_DQ.max,m-trend' % (optic_m2, dof2)]-data_m3_mean
        plot_m3_min = data_m3_min.plot()
        axP3 = plot_m3_min.gca()
        axP3.plot(data_m3_mean-data_m3_mean, label='Mean')
        axP3.plot(data_m3_max, label='Max')
        axP3.set_ylabel('Amplitude - Mean value (urad)')
        axP3.set_title('%s %s' %(optic_m2, dof2))
        pylab.ylim([-200,200])
        L = axP3.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
        L.get_texts()[0].set_text('Min')
        ml1 = MultipleLocator(10)
        ml2 = MultipleLocator(3600)
        axP3.yaxis.set_minor_locator(ml1)
        axP3.xaxis.set_minor_locator(ml2)
        plot_m3_min.save('L1-SUS-%s_M3_WIT_%smmm_DQ.png' % (optic_m2, dof2))
        print "PLOT SAVED"

