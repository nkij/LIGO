#This program fetches m-trend data of the top stages of all the optics.
import sys

from matplotlib import use
use('agg')

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

args = sys.argv
optic = args[1]

#Start-End Time 
start = Time('2014-06-14 00:00:00', format='iso', scale='utc')
end = Time('2014-06-15 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

QUAD = ['ETMX','ETMY','ITMX','ITMY']
TRIPLE = ['BS', 'MC1', 'MC2', 'MC3', 'PR2', 'PR3', 'PRM', 'SR2', 'SR3', 'SRM' ]

if optic in QUAD:
    topstage = 'M0'
elif optic in TRIPLE:
    topstage = 'M1'
else:
    raise ValueError("Unknown optic %r" % optic)

TOPSTAGE_DOFS = ['P', 'R', 'Y']
OTHER_DOFS = ['P', 'Y']
DEGREE_OF_FREEDOM = ['PIT', 'YAW']
TRENDS = ['min','mean','max']

m1_channels = []
m2_channels = []
m3_channels = []
l1_channels = []
l2_channels = []
l3_channels = []

for dof in TOPSTAGE_DOFS:
    print dof,'M0'
    for trend in TRENDS:
        print trend,'M0'
        m1_channels.append('L1:SUS-%s_%s_DAMP_%s_INMON.%s,m-trend' % (optic, topstage, dof, trend)) 
        print m1_channels

if optic in TRIPLE:
    print optic,'TRIPLE'
    for dof2 in OTHER_DOFS:
        print dof2,'TRIPLE'
        for trend in TRENDS:
            m2_channels.append('L1:SUS-%s_M2_WIT_%s_DQ.%s,m-trend' % (optic, dof2, trend))
            m3_channels.append('L1:SUS-%s_M3_WIT_%s_DQ.%s,m-trend' % (optic, dof2, trend))
            print m2_channels
            print m3_channels

else:
    for dof2 in OTHER_DOFS:
        print dof2,'QUAD'
        for trend in TRENDS:
            print trend,'QUAD'
            l1_channels.append('L1:SUS-%s_L1_WIT_%s_DQ.%s,m-trend' % (optic, dof2, trend))
            l2_channels.append('L1:SUS-%s_L2_WIT_%s_DQ.%s,m-trend' % (optic, dof2, trend))
            print l1_channels
            print l2_channels
    for dof3 in DEGREE_OF_FREEDOM:
        print dof3, 'QUAD'
        for trend in TRENDS:
            print trend, 'QUAD'
            l3_channels.append('L1:SUS-%s_L3_OPLEV_%s_OUT_DQ.%s,m-trend' % (optic, dof3, trend))
            print l3_channels

data = dict()
data[topstage] = TimeSeriesDict.fetch(m1_channels, start, end, verbose=True)

if optic in TRIPLE:
    data['M2'] = TimeSeriesDict.fetch(m2_channels, start, end, verbose=True)
    data['M3'] = TimeSeriesDict.fetch(m3_channels, start, end, verbose=True)

else:
    data['L1'] = TimeSeriesDict.fetch(l1_channels, start, end, verbose=True)
    data['L2'] = TimeSeriesDict.fetch(l2_channels, start, end, verbose=True)
    data['L3'] = TimeSeriesDict.fetch(l3_channels, start, end, verbose=True)


for dof in TOPSTAGE_DOFS:
    if optic in QUAD:
        print "%s  QUAD" %(dof)
        stub = 'L1:SUS-%s_%s_DAMP_%s_INMON.%s,m-trend' % (optic, topstage, dof, '%s')
        data_mean = data[topstage][stub % 'mean']-data[topstage][stub % 'mean'].median().value
        data_min = data[topstage][stub % 'min']-data[topstage][stub % 'min'].median().value
        data_min.name = 'Min'
        data_max = data[topstage][stub % 'max']-data[topstage][stub % 'max'].median().value
        plot_min = data_min.plot()
        ax = plot_min.gca()
        ax.plot(data_mean, label='Mean')
        ax.plot(data_max, label='Max')
        ax.set_epoch(start.gps)
        ax.set_xlim(start.gps, end.gps)
        ax.set_ylabel('Amplitude - Median Value (urad)')
        ax.set_title(r'L1:SUS-%s\_%s\_DAMP\_%s\_INMON (LOCKED)' %(optic, topstage, dof))
#       ax.set_ylim([-200,200])
        ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
       
        plot_min.save('L1-SUS-%s_M0_DAMP_%smmm_INMON.png' % (optic,  dof))
        print "QUAD PLOT SAVED"

    else:
        print "%s TRIP M1" %(dof)
        stub = 'L1:SUS-%s_%s_DAMP_%s_INMON.%s,m-trend' % (optic, topstage, dof, '%s')
        data_mean = data[topstage][stub % 'mean']-data[topstage][stub % 'mean'].median().value
        data_min = data[topstage][stub % 'min']-data[topstage][stub % 'min'].median().value
        data_min.name = 'Min'
        data_max = data[topstage][stub % 'max']-data[topstage][stub % 'max'].median().value
        plot_min = data_min.plot()
        ax = plot_min.gca()
        ax.plot(data_mean, label='Mean')
        ax.plot(data_max, label='Max')
        ax.set_epoch(start.gps)
        ax.set_xlim(start.gps, end.gps)
        ax.set_ylabel('Amplitude - Median Value (urad)')
        ax.set_title(r'L1:SUS-%s\_%s\_DAMP\_%s\_INMON (LOCKED)' %(optic, topstage, dof))
#        ax.set_ylim([-200,200])
        ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)
 
        plot_min.save('L1-SUS-%s_M1_DAMP_%smmm_INMON.png' % (optic, dof))
        print "TRIPLE PLOT SAVED"

if optic in TRIPLE:
    for stage in ['M2', 'M3']:
        for dof in OTHER_DOFS:
            print "%s TRIP M2 M3" %(dof)
            stub = 'L1:SUS-%s_%s_WIT_%s_DQ.%s,m-trend' % (optic, stage, dof, '%s')
            data_mean = data[stage][stub % 'mean']-data[stage][stub % 'mean'].median().value
            data_min = data[stage][stub % 'min']-data[stage][stub % 'min'].median().value
            data_min.name = 'Min'
            data_max = data[stage][stub % 'max']-data[stage][stub % 'max'].median().value
            plot_min = data_min.plot()
            ax = plot_min.gca()
            ax.plot(data_mean, label='Mean')
            ax.plot(data_max, label='Max')
            ax.set_epoch(start.gps)
            ax.set_xlim(start.gps, end.gps)
            ax.set_ylabel('Amplitude - Median Value (urad)')
            ax.set_title(r'L1:SUS-%s\_%s\_WIT\_%s\_DQ (LOCKED)' %(optic, stage, dof))
#            ax.set_ylim([-200,200])
            ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)

            plot_min.save('L1-SUS-%s_%s_WIT_%smmm_DQ.png' % (optic, stage, dof))
            print "TRIPLE PLOT SAVED"

else:
    for stage in ['L1', 'L2']:
        for dof in OTHER_DOFS:
            print "%s  L1 L2" %(dof)
            stub = 'L1:SUS-%s_%s_WIT_%s_DQ.%s,m-trend' % (optic, stage, dof, '%s')
            data_mean = data[stage][stub % 'mean']-data[stage][stub % 'mean'].median().value
            data_min = data[stage][stub % 'min']-data[stage][stub % 'min'].median().value
            data_min.name = 'Min'
            data_max = data[stage][stub % 'max']-data[stage][stub % 'max'].median().value
            plot_min = data_min.plot()
            ax = plot_min.gca()
            ax.plot(data_mean, label='Mean')
            ax.plot(data_max, label='Max')
            ax.set_epoch(start.gps)
            ax.set_xlim(start.gps, end.gps)
            ax.set_ylabel('Amplitude - Median Value (urad)')
            ax.set_title(r'L1:SUS-%s\_%s\_WIT\_%s\_DQ' %(optic, stage, dof))
#            ax.set_ylim([-200,200])
            ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)

            plot_min.save('L1-SUS-%s_%s_WIT_%smmm_DQ.png' % (optic, stage, dof))
            print "PLOT SAVED"

    for stage in ['L3']:
        for dof in DEGREE_OF_FREEDOM:
            print "%s  L3" %(dof)
            stub = 'L1:SUS-%s_%s_OPLEV_%s_OUT_DQ.%s,m-trend' % (optic, stage, dof, '%s')
            data_mean = data[stage][stub % 'mean']-data[stage][stub % 'mean'].median().value
            data_min = data[stage][stub % 'min']-data[stage][stub % 'min'].median().value
            data_min.name = 'Min'
            data_max = data[stage][stub % 'max']-data[stage][stub % 'max'].median().value
            plot_min = data_min.plot()
            ax = plot_min.gca()
            ax.plot(data_mean, label='Mean')
            ax.plot(data_max, label='Max')
            ax.set_epoch(start.gps)
            ax.set_xlim(start.gps, end.gps)
            ax.set_ylabel('Amplitude - Median Value (urad)')
            ax.set_title(r'L1:SUS-%s\_%s\_OPLEV\_%s\_INMON' %(optic, stage, dof))
#            ax.set_ylim([-200,200])                                                                                                                                                                               
            ax.legend(loc='upper right', ncol=1, fancybox=True, shadow=True)

            plot_min.save('L1-SUS-%s_%s_OPLEV_%smmm_OUT_DQ.png' % (optic, stage, dof))
            print "PLOT SAVED"
