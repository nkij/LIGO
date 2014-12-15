#!/usr/bin/env python
#To run any python script: execfile("filemame.py")

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

f = open('20140406_driftmon.txt', 'wb')

channels = ['L1:SUS-BS_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-BS_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-BS_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-ETMX_M0_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-ETMX_M0_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-ETMX_M0_DAMP_Y_INMON.rms,m-trend', 
            'L1:SUS-ITMX_M0_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-ITMX_M0_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-ITMX_M0_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-ITMY_M0_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-ITMY_M0_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-ITMY_M0_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-MC1_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-MC1_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-MC1_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-MC2_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-MC2_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-MC2_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-MC3_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-MC3_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-MC3_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-PR2_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-PR2_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-PR2_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-PR3_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-PR3_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-PR3_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-PRM_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-PRM_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-PRM_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-SR2_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-SR2_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-SR2_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-SR3_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-SR3_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-SR3_M1_DAMP_Y_INMON.rms,m-trend',
            'L1:SUS-SRM_M1_DAMP_P_INMON.rms,m-trend',
            'L1:SUS-SRM_M1_DAMP_R_INMON.rms,m-trend',
            'L1:SUS-SRM_M1_DAMP_Y_INMON.rms,m-trend']

data = TimeSeriesDict.fetch(channels, start, end, verbose=True)

data_BS_P = data[channels[0]]
data_BS_R = data[channels[1]]
data_BS_Y = data[channels[2]]
plot_BS_P = data_BS_P.plot()
axBS = plot_BS_P.gca()
axBS.plot(data_BS_R, label='Roll (x10)')
axBS.plot(data_BS_Y, label='Yaw (x10)')
axBS.set_ylabel('Amplitude (urad)')
L = axBS.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axBS.yaxis.set_minor_locator(ml1)
axBS.xaxis.set_minor_locator(ml2)
plot_BS_P.save('L1-SUS-BS_M1_DAMP_PRY_INMON.png')

data_ETMX_P = data[channels[3]]
data_ETMX_R = data[channels[4]]
data_ETMX_Y = data[channels[5]]
plot_ETMX_P = data_ETMX_P.plot()
axETMX = plot_ETMX_P.gca()
axETMX.plot(data_ETMX_R, label='Roll (x10)')
axETMX.plot(data_ETMX_Y, label='Yaw (x10)')
axETMX.set_ylabel('Amplitude (urad)')
L = axETMX.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axETMX.yaxis.set_minor_locator(ml1)
axETMX.xaxis.set_minor_locator(ml2)
plot_ETMX_P.save('L1-SUS-ETMX_M0_DAMP_PRY_INMON.png')

data_ITMX_P = data[channels[6]]
data_ITMX_R = data[channels[7]]
data_ITMX_Y = data[channels[8]]
plot_ITMX_P = data_ITMX_P.plot()
axITMX = plot_ITMX_P.gca()
axITMX.plot(data_ITMX_R, label='Roll (x10)')
axITMX.plot(data_ITMX_Y, label='Yaw (x10)')
axITMX.set_ylabel('Amplitude (urad)')
L = axITMX.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axITMX.yaxis.set_minor_locator(ml1)
axITMX.xaxis.set_minor_locator(ml2)
plot_ITMX_P.save('L1-SUS-ITMX_M0_DAMP_PRY_INMON.png')

data_ITMY_P = data[channels[9]]
data_ITMY_R = data[channels[10]]
data_ITMY_Y = data[channels[11]]
plot_ITMY_P = data_ITMY_P.plot()
axITMY = plot_ITMY_P.gca()
axITMY.plot(data_ITMY_R, label='Roll (x10)')
axITMY.plot(data_ITMY_Y, label='Yaw (x10)')
axITMY.set_ylabel('Amplitude (urad)')
L = axITMY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axITMY.yaxis.set_minor_locator(ml1)
axITMY.xaxis.set_minor_locator(ml2)
plot_ITMY_P.save('L1-SUS-ITMY_M0_DAMP_PRY_INMON.png')

data_MC1_P = data[channels[12]]
data_MC1_R = data[channels[13]]
data_MC1_Y = data[channels[14]]
plot_MC1_P = data_MC1_P.plot()
axMC1 = plot_MC1_P.gca()
axMC1.plot(data_MC1_R, label='Roll (x10)')
axMC1.plot(data_MC1_Y, label='Yaw (x10)')
axMC1.set_ylabel('Amplitude (urad)')
L = axMC1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axMC1.yaxis.set_minor_locator(ml1)
axMC1.xaxis.set_minor_locator(ml2)
plot_MC1_P.save('L1-SUS-MC1_M1_DAMP_PRY_INMON.png')

data_MC2_P = data[channels[15]]
data_MC2_R = data[channels[16]]
data_MC2_Y = data[channels[17]]
plot_MC2_P = data_MC2_P.plot()
axMC2 = plot_MC2_P.gca()
axMC2.plot(data_MC2_R, label='Roll (x10)')
axMC2.plot(data_MC2_Y, label='Yaw (x10)')
axMC2.set_ylabel('Amplitude (urad)')
L = axMC2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axMC2.yaxis.set_minor_locator(ml1)
axMC2.xaxis.set_minor_locator(ml2)
plot_MC2_P.save('L1-SUS-MC2_M1_DAMP_PRY_INMON.png')


data_MC3_P = data[channels[18]]
data_MC3_R = data[channels[19]]
data_MC3_Y = data[channels[20]]
plot_MC3_P = data_MC3_P.plot()
axMC3 = plot_MC3_P.gca()
axMC3.plot(data_MC3_R, label='Roll (x10)')
axMC3.plot(data_MC3_Y, label='Yaw (x10)')
axMC3.set_ylabel('Amplitude (urad)')
L = axMC3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axMC3.yaxis.set_minor_locator(ml1)
axMC3.xaxis.set_minor_locator(ml2)
plot_MC3_P.save('L1-SUS-MC3_M1_DAMP_PRY_INMON.png')


data_PR2_P = data[channels[21]]
data_PR2_R = data[channels[22]]
data_PR2_Y = data[channels[23]]
plot_PR2_P = data_PR2_P.plot()
axPR2 = plot_PR2_P.gca()
axPR2.plot(data_PR2_R, label='Roll (x10)')
axPR2.plot(data_PR2_Y, label='Yaw (x10)')
axPR2.set_ylabel('Amplitude (urad)')
L = axPR2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axPR2.yaxis.set_minor_locator(ml1)
axPR2.xaxis.set_minor_locator(ml2)
plot_PR2_P.save('L1-SUS-PR2_M1_DAMP_PRY_INMON.png')


data_PR3_P = data[channels[24]]
data_PR3_R = data[channels[25]]
data_PR3_Y = data[channels[26]]
plot_PR3_P = data_PR3_P.plot()
axPR3 = plot_PR3_P.gca()
axPR3.plot(data_PR3_R, label='Roll (x10)')
axPR3.plot(data_PR3_Y, label='Yaw (x10)')
axPR3.set_ylabel('Amplitude (urad)')
L = axPR3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axPR3.yaxis.set_minor_locator(ml1)
axPR3.xaxis.set_minor_locator(ml2)
plot_PR3_P.save('L1-SUS-PR3_M1_DAMP_PRY_INMON.png')


data_PRM_P = data[channels[27]]
data_PRM_R = data[channels[28]]
data_PRM_Y = data[channels[29]]
plot_PRM_P = data_PRM_P.plot()
axPRM = plot_PRM_P.gca()
axPRM.plot(data_PRM_R, label='Roll (x10)')
axPRM.plot(data_PRM_Y, label='Yaw (x10)')
axPRM.set_ylabel('Amplitude (urad)')
L = axPRM.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axPRM.yaxis.set_minor_locator(ml1)
axPRM.xaxis.set_minor_locator(ml2)
plot_PRM_P.save('L1-SUS-PRM_M1_DAMP_PRY_INMON.png')


data_SR2_P = data[channels[30]]
data_SR2_R = data[channels[31]]
data_SR2_Y = data[channels[32]]
plot_SR2_P = data_SR2_P.plot()
axSR2 = plot_SR2_P.gca()
axSR2.plot(data_SR2_R, label='Roll (x10)')
axSR2.plot(data_SR2_Y, label='Yaw (x10)')
axSR2.set_ylabel('Amplitude (urad)')
L = axSR2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axSR2.yaxis.set_minor_locator(ml1)
axSR2.xaxis.set_minor_locator(ml2)
plot_SR2_P.save('L1-SUS-SR2_M1_DAMP_PRY_INMON.png')


data_SR3_P = data[channels[33]]
data_SR3_R = data[channels[34]]
data_SR3_Y = data[channels[35]]
plot_SR3_P = data_SR3_P.plot()
axSR3 = plot_SR3_P.gca()
axSR3.plot(data_SR3_R, label='Roll (x10)')
axSR3.plot(data_SR3_Y, label='Yaw (x10)')
axSR3.set_ylabel('Amplitude (urad)')
L = axSR3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axSR3.yaxis.set_minor_locator(ml1)
axSR3.xaxis.set_minor_locator(ml2)
plot_SR3_P.save('L1-SUS-SR3_M1_DAMP_PRY_INMON.png')


data_SRM_P = data[channels[36]]
data_SRM_R = data[channels[37]]
data_SRM_Y = data[channels[38]]
plot_SRM_P = data_SRM_P.plot()
axSRM = plot_SRM_P.gca()
axSRM.plot(data_SRM_R, label='Roll (x10)')
axSRM.plot(data_SRM_Y, label='Yaw (x10)')
axSRM.set_ylabel('Amplitude (urad)')
L = axSRM.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Pitch')
axSRM.yaxis.set_minor_locator(ml1)
axSRM.xaxis.set_minor_locator(ml2)
plot_SRM_P.save('L1-SUS-SRM_M1_DAMP_PRY_INMON.png')

print "data_BS_P = %s" % data_BS_P.mean() 
print "std = %s" % data_BS_P.std()
print "data_BS_R = %s" % data_BS_R.mean()
print "std = %s" % data_BS_R.std()
print "data_BS_Y = %s" % data_BS_Y.mean() 
print "std = %s" % data_BS_Y.std()
print "-----------------------------------------"
print "data_ETMX_P = %s" % data_ETMX_P.mean()
print "std = %s" % data_ETMX_P.std() 
print "data_ETMX_R = %s" % data_ETMX_R.mean()
print "std = %s" % data_ETMX_R.std() 
print "data_ETMX_Y = %s" % data_ETMX_Y.mean()
print "std = %s" % data_ETMX_Y.std() 
print "-----------------------------------------"
print "data_ITMX_P = %s" % data_ITMX_P.mean()
print "std = %s" % data_ITMX_P.std()
print "data_ITMX_R = %s" % data_ITMX_R.mean() 
print "std = %s" % data_ITMX_R.std()
print "data_ITMX_Y = %s" % data_ITMX_Y.mean()
print "std = %s" % data_ITMX_Y.std()
print "-----------------------------------------"
print "data_ITMY_P = %s" % data_ITMY_P.mean()
print "std = %s" % data_ITMY_P.std() 
print "data_ITMY_R = %s" % data_ITMY_R.mean() 
print "std = %s" % data_ITMY_R.std()
print "data_ITMY_Y = %s" % data_ITMY_Y.mean()
print "std = %s" % data_ITMY_Y.std()
print "-----------------------------------------"
print "data_MC1_P = %s" % data_MC1_P.mean()
print "std = %s" % data_MC1_P.std() 
print "data_MC1_R = %s" % data_MC1_R.mean() 
print "std = %s" % data_MC1_R.std()
print "data_MC1_Y = %s" % data_MC1_Y.mean()
print "std = %s" % data_MC1_Y.std()
print "-----------------------------------------"
print "data_MC2_P = %s" % data_MC2_P.mean()
print "std = %s" % data_MC2_P.std() 
print "data_MC2_R = %s" % data_MC2_R.mean()
print "std = %s" % data_MC2_R.std() 
print "data_MC2_Y = %s" % data_MC2_Y.mean() 
print "std = %s" % data_MC2_Y.std()
print "-----------------------------------------"
print "data_MC3_P = %s" % data_MC3_P.mean()
print "std = %s" % data_MC3_P.std()
print "data_MC3_R = %s" % data_MC3_R.mean() 
print "std = %s" % data_MC3_R.std()
print "data_MC3_Y = %s" % data_MC3_Y.mean() 
print "std = %s" % data_MC3_Y.std()
print "-----------------------------------------"
print "data_PR2_P = %s" % data_PR2_P.mean()
print "std = %s" % data_PR2_P.std()
print "data_PR2_R = %s" % data_PR2_R.mean() 
print "std = %s" % data_PR2_R.std()
print "data_PR2_Y = %s" % data_PR2_Y.mean() 
print "std = %s" % data_PR2_Y.std()
print "-----------------------------------------"
print "data_PR3_P = %s" % data_PR3_P.mean()
print "std = %s" % data_PR3_P.std()
print "data_PR3_R = %s" % data_PR3_R.mean() 
print "std = %s" % data_PR3_R.std()
print "data_PR3_Y = %s" % data_PR3_Y.mean() 
print "std = %s" % data_PR3_Y.std()
print "-----------------------------------------"
print "data_PRM_P = %s" % data_PRM_P.mean()
print "std = %s" % data_PRM_P.std()
print "data_PRM_R = %s" % data_PRM_R.mean()
print "std = %s" % data_PRM_R.std()
print "data_PRM_Y = %s" % data_PRM_Y.mean()
print "std = %s" % data_PRM_Y.std()
print "-----------------------------------------"
print "data_SR2_P = %s" % data_SR2_P.mean()
print "std = %s" % data_SR2_P.std()
print "data_SR2_R = %s" % data_SR2_R.mean() 
print "std = %s" % data_SR2_R.std()
print "data_SR2_Y = %s" % data_SR2_Y.mean() 
print "std = %s" % data_SR2_Y.std()
print "-----------------------------------------"
print "data_SR3_P = %s" % data_SR3_P.mean()
print "std = %s" % data_SR3_P.std()
print "data_SR3_R = %s" % data_SR3_R.mean() 
print "std = %s" % data_SR3_R.std()
print "data_SR3_Y = %s" % data_SR3_Y.mean()
print "std = %s" % data_SR3_Y.std()
print "-----------------------------------------" 
print "data_SRM_P = %s" % data_SRM_P.mean()
print "std = %s" % data_SRM_P.std()
print "data_SRM_R = %s" % data_SRM_R.mean() 
print "std = %s" % data_SRM_R.std()
print "data_SRM_Y = %s" % data_SRM_Y.mean()
print "std = %s" % data_SRM_Y.std()

f.writelines([str(data_BS_P.mean()),';', str(data_BS_P.std()),';',str(data_BS_R.mean()),';',str(data_BS_R.std()),';',str(data_BS_Y.mean()),';', str(data_BS_Y.std()), ';', str(data_ETMX_P.mean()),';',str(data_ETMX_P.std() ),';',str( data_ETMX_R.mean()),';', str(data_ETMX_R.std() ),';', str(data_ETMX_Y.mean()),';', str(data_ETMX_Y.std() ),';',str(data_ITMX_P.mean()),';', str(data_ITMX_P.std()),';', str(data_ITMX_R.mean() ), ';', str(data_ITMX_R.std()),';', str(data_ITMX_Y.mean()),';',str(data_ITMX_Y.std()),';', str(data_ITMY_P.mean()),';',str( data_ITMY_P.std() ),';', str(data_ITMY_R.mean()),';', str(data_ITMY_R.std()),';',str(data_ITMY_Y.mean()),';',str(data_ITMY_Y.std()),';',str(data_MC1_P.mean()),';',str( data_MC1_P.std() ),';',str(data_MC1_R.mean()),';',str(data_MC1_R.std()),';',str(data_MC1_Y.mean()),';',str(data_MC1_Y.std()),';', str(data_MC2_P.mean()),';',str(data_MC2_P.std() ),';',str(data_MC2_R.mean()),';',str(data_MC2_R.std() ),';',str(data_MC2_Y.mean() ),';',str(data_MC2_Y.std()),';',str(data_MC3_P.mean()),';',str(data_MC3_P.std()),';',str(data_MC3_R.mean() ),';',str(data_MC3_R.std()),';',str(data_MC3_Y.mean()),';',str(data_MC3_Y.std()),';',str(data_PR2_P.mean()),';',str(data_PR2_P.std()),';',str(data_PR2_R.mean() ),';',str(data_PR2_R.std()),';',str(data_PR2_Y.mean() ),';',str(data_PR2_Y.std()),';',str(data_PR3_P.mean()),';',str(data_PR3_P.std()),';',str(data_PR3_R.mean() ),';',str(data_PR3_R.std()),';',str( data_PR3_Y.mean()),';',str(data_PR3_Y.std()),';',str(data_PRM_P.mean()),';',str(data_PRM_P.std()),';',str(data_PRM_R.mean()),';',str(data_PRM_R.std()),';',str(data_PRM_Y.mean()),';',str(data_PRM_Y.std()),';',str(data_SR2_P.mean()),';',str(data_SR2_P.std()),';',str(data_SR2_R.mean()),';',str(data_SR2_R.std()),';',str(data_SR2_Y.mean() ),';',str(data_SR2_Y.std()),';',str( data_SR3_P.mean()),';',str(data_SR3_P.std()),';',str(data_SR3_R.mean() ),';',str(data_SR3_R.std()),';',str(data_SR3_Y.mean()),';',str(data_SR3_Y.std()),';',str(data_SRM_P.mean()),';',str(data_SRM_P.std()),';',str(data_SRM_R.mean()),';',str(data_SRM_R.std()),';',str(data_SRM_Y.mean()),';',str(data_SRM_Y.std())])

f.close()

print "JOB DONE"
