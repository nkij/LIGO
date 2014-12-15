#!/usr/bin/env python
#To run any python script: execfile("filemame.py")

import matplotlib.pyplot as plt
from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)

print "Import Modules Success"

#Start-End Time 
start = Time('2014-03-25 00:00:00', format='iso', scale='utc')
end = Time('2014-03-26 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

#f = open('20140402_driftmon.txt', 'wb')

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

#data_BS_P = data[channels[0]]
#plot_BS_P = data_BS_P.plot()
#ax = plot_BS_P.gca()
#ax.set_ylabel('Amplitude (urad)')
#plot_BS_P.save('L1-SUS-BS_M1_DAMP_P_INMON.png')


data_BS_P = data[channels[0]]
data_BS_R = data[channels[1]]
data_BS_Y = data[channels[2]]
plot_BS_P = data_BS_P.plot()
axBS = plot_BS_P.gca()
axBS.plot(data_BS_R)
axBS.plot(data_BS_Y)
axBS.set_ylabel('Amplitude (urad)')
plot_BS_P.save('L1-SUS-BS_M1_DAMP_PRY_INMON.png')


#data_BS_R = data[channels[1]]
#ax.plot(data_BS_R)
#plot_BS_R = data_BS_R.plot()
#ax = plot_BS_R.gca()
#ax.set_ylabel('Amplitude (urad)')
#plot_BS_R.save('L1-SUS-BS_M1_DAMP_R_INMON.png')


#data_BS_Y = data[channels[2]]
#ax.plot(data_BS_Y)
#plot_BS_Y = data_BS_Y.plot()
#ax = plot_BS_Y.gca()
#ax.set_ylabel('Amplitude (urad)')
#plot_BS_Y.save('L1-SUS-BS_M1_DAMP_Y_INMON.png')




data_ETMX_P = data[channels[3]]
data_ETMX_R = data[channels[4]]
data_ETMX_Y = data[channels[5]]
plot_ETMX_P = data_ETMX_P.plot()
axETMX = plot_ETMX_P.gca()
axETMX.plot(data_ETMX_R)
axETMX.plot(data_ETMX_Y)
axETMX.set_ylabel('Amplitude (urad)')
plot_ETMX_P.save('L1-SUS-ETMX_M0_DAMP_PRY_INMON.png')

#data_ETMX_P = data[channels[3]]
#plot_ETMX_P = data_ETMX_P.plot()
#ax = plot_ETMX_P.gca()
#ax.set_ylabel('Amplitude (urad)')
#plot_ETMX_P.save('L1-SUS-ETMX_M0_DAMP_P_INMON.png')


#data_ETMX_R = data[channels[4]]
#plot_ETMX_R = data_ETMX_R.plot()
#ax = plot_ETMX_R.gca()
#ax.set_ylabel('Amplitude (urad)')
#plot_ETMX_R.save('L1-SUS-ETMX_M0_DAMP_R_INMON.png')


#data_ETMX_Y = data[channels[5]]
#plot_ETMX_Y = data_ETMX_Y.plot()
#ax = plot_ETMX_Y.gca()
#ax.set_ylabel('Amplitude (urad)')
#plot_ETMX_Y.save('L1-SUS-ETMX_M0_DAMP_Y_INMON.png')

data_ITMX_P = data[channels[6]]
plot_ITMX_P = data_ITMX_P.plot()
ax = plot_ITMX_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_ITMX_P.save('L1-SUS-ITMX_M0_DAMP_P_INMON.png')

data_ITMX_R = data[channels[7]]
plot_ITMX_R = data_ITMX_R.plot()
ax = plot_ITMX_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_ITMX_R.save('L1-SUS-ITMX_M0_DAMP_R_INMON.png')

data_ITMX_Y = data[channels[8]]
plot_ITMX_Y = data_ITMX_Y.plot()
ax = plot_ITMX_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_ITMX_Y.save('L1-SUS-ITMX_M0_DAMP_Y_INMON.png')

data_ITMY_P = data[channels[9]]
plot_ITMY_P = data_ITMY_P.plot()
ax = plot_ITMY_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_ITMY_P.save('L1-SUS-ITMY_M0_DAMP_P_INMON.png')

data_ITMY_R = data[channels[10]]
plot_ITMY_R = data_ITMY_R.plot()
ax = plot_ITMY_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_ITMY_R.save('L1-SUS-ITMY_M0_DAMP_R_INMON.png')

data_ITMY_Y = data[channels[11]]
plot_ITMY_Y = data_ITMY_R.plot()
ax = plot_ITMY_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_ITMY_Y.save('L1-SUS-ITMY_M0_DAMP_Y_INMON.png')


data_MC1_P = data[channels[12]]
plot_MC1_P = data_MC1_P.plot()
ax = plot_MC1_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC1_P.save('L1-SUS-MC1_M1_DAMP_P_INMON.png')

data_MC1_R = data[channels[13]]
plot_MC1_R = data_MC1_R.plot()
ax = plot_MC1_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC1_R.save('L1-SUS-MC1_M1_DAMP_R_INMON.png')

data_MC1_Y = data[channels[14]]
plot_MC1_Y = data_MC1_Y.plot()
ax = plot_MC1_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC1_Y.save('L1-SUS-MC1_M1_DAMP_Y_INMON.png')

data_MC2_P = data[channels[15]]
plot_MC2_P = data_MC2_P.plot()
ax = plot_MC2_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC2_P.save('L1-SUS-MC2_M1_DAMP_P_INMON.png')

data_MC2_R = data[channels[16]]
plot_MC2_R = data_MC2_R.plot()
ax = plot_MC2_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC2_R.save('L1-SUS-MC2_M1_DAMP_R_INMON.png')

data_MC2_Y = data[channels[17]]
plot_MC2_Y = data_MC2_Y.plot()
ax = plot_MC2_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC2_Y.save('L1-SUS-MC2_M1_DAMP_Y_INMON.png')

data_MC3_P = data[channels[18]]
plot_MC3_P = data_MC3_P.plot()
ax = plot_MC3_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC3_P.save('L1-SUS-MC3_M1_DAMP_P_INMON.png')

data_MC3_R = data[channels[19]]
plot_MC3_R = data_MC3_R.plot()
ax = plot_MC3_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC3_R.save('L1-SUS-MC3_M1_DAMP_R_INMON.png')

data_MC3_Y = data[channels[20]]
plot_MC3_Y = data_MC3_Y.plot()
ax = plot_MC3_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_MC3_Y.save('L1-SUS-MC3_M1_DAMP_Y_INMON.png')

data_PR2_P = data[channels[21]]
plot_PR2_P = data_PR2_P.plot()
ax = plot_PR2_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PR2_P.save('L1-SUS-PR2_M1_DAMP_P_INMON.png')

data_PR2_R = data[channels[22]]
plot_PR2_R = data_PR2_R.plot()
ax = plot_PR2_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PR2_R.save('L1-SUS-PR2_M1_DAMP_R_INMON.png')

data_PR2_Y = data[channels[23]]
plot_PR2_Y = data_PR2_Y.plot()
ax = plot_PR2_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PR2_Y.save('L1-SUS-PR2_M1_DAMP_Y_INMON.png')

data_PR3_P = data[channels[24]]
plot_PR3_P = data_PR3_P.plot()
ax = plot_PR3_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PR3_P.save('L1-SUS-PR3_M1_DAMP_P_INMON.png')

data_PR3_R = data[channels[25]]
plot_PR3_R = data_PR3_R.plot()
ax = plot_PR3_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PR3_R.save('L1-SUS-PR3_M1_DAMP_R_INMON.png')

data_PR3_Y = data[channels[26]]
plot_PR3_Y = data_PR3_Y.plot()
ax = plot_PR3_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PR3_Y.save('L1-SUS-PR3_M1_DAMP_Y_INMON.png')

data_PRM_P = data[channels[27]]
plot_PRM_P = data_PRM_P.plot()
ax = plot_PRM_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PRM_P.save('L1-SUS-PRM_M1_DAMP_P_INMON.png')

data_PRM_R = data[channels[28]]
plot_PRM_R = data_PRM_R.plot()
ax = plot_PRM_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PRM_R.save('L1-SUS-PRM_M1_DAMP_R_INMON.png')

data_PRM_Y = data[channels[29]]
plot_PRM_Y = data_PRM_Y.plot()
ax = plot_PRM_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_PRM_Y.save('L1-SUS-PRM_M1_DAMP_Y_INMON.png')

data_SR2_P = data[channels[30]]
plot_SR2_P = data_SR2_P.plot()
ax = plot_SR2_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SR2_P.save('L1-SUS-SR2_M1_DAMP_P_INMON.png')

data_SR2_R = data[channels[31]]
plot_SR2_R = data_SR2_R.plot()
ax = plot_SR2_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SR2_R.save('L1-SUS-SR2_M1_DAMP_R_INMON.png')

data_SR2_Y = data[channels[32]]
plot_SR2_Y = data_SR2_Y.plot()
ax = plot_SR2_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SR2_Y.save('L1-SUS-SR2_M1_DAMP_Y_INMON.png')

data_SR3_P = data[channels[33]]
plot_SR3_P = data_SR3_P.plot()
ax = plot_SR3_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SR3_P.save('L1-SUS-SR3_M1_DAMP_P_INMON.png')

data_SR3_R = data[channels[34]]
plot_SR3_R = data_SR3_R.plot()
ax = plot_SR3_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SR3_R.save('L1-SUS-SR3_M1_DAMP_R_INMON.png')

data_SR3_Y = data[channels[35]]
plot_SR3_Y = data_SR3_Y.plot()
ax = plot_SR3_Y.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SR3_Y.save('L1-SUS-SR3_M1_DAMP_Y_INMON.png')

data_SRM_P = data[channels[36]]
plot_SRM_P = data_SRM_P.plot()
ax = plot_SRM_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SRM_P.save('L1-SUS-SRM_M1_DAMP_P_INMON.png')

data_SRM_R = data[channels[37]]
plot_SRM_R = data_SRM_R.plot()
ax = plot_SRM_R.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SRM_R.save('L1-SUS-SRM_M1_DAMP_R_INMON.png')

data_SRM_Y = data[channels[38]]
plot_SRM_Y = data_SRM_Y.plot()
ax = plot_SRM_P.gca()
ax.set_ylabel('Amplitude (urad)')
plot_SRM_Y.save('L1-SUS-SRM_M1_DAMP_Y_INMON.png')

#Fetch Data
#dataP=TimeSeries.fetch('L1:SUS-BS_M1_DAMP_P_INMON.rms,m-trend', start, end, verbose=True)
#print "Fetch DataP Success"
#dataR=TimeSeries.fetch('L1:SUS-BS_M1_DAMP_R_INMON.rms,m-trend', start, end, verbose=True)
#print "Fetch DataR Success"
#dataY=TimeSeries.fetch('L1:SUS-BS_M1_DAMP_Y_INMON.rms,m-trend', start, end, verbose=True)
#print "Fetch DataY Success"


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

#f.writelines([str(data_BS_P.mean()),';', str(data_BS_P.std()),';',str(data_BS_R.mean()),';',str(data_BS_R.std()),';',str(data_BS_Y.mean()),';', str(data_BS_Y.std()), ';', str(data_ETMX_P.mean()),';',str(data_ETMX_P.std() ),';',str( data_ETMX_R.mean()),';', str(data_ETMX_R.std() ),';', str(data_ETMX_Y.mean()),';', str(data_ETMX_Y.std() ),';',str(data_ITMX_P.mean()),';', str(data_ITMX_P.std()),';', str(data_ITMX_R.mean() ), ';', str(data_ITMX_R.std()),';', str(data_ITMX_Y.mean()),';',str(data_ITMX_Y.std()),';', str(data_ITMY_P.mean()),';',str( data_ITMY_P.std() ),';', str(data_ITMY_R.mean()),';', str(data_ITMY_R.std()),';',str(data_ITMY_Y.mean()),';',str(data_ITMY_Y.std()),';',str(data_MC1_P.mean()),';',str( data_MC1_P.std() ),';',str(data_MC1_R.mean()),';',str(data_MC1_R.std()),';',str(data_MC1_Y.mean()),';',str(data_MC1_Y.std()),';', str(data_MC2_P.mean()),';',str(data_MC2_P.std() ),';',str(data_MC2_R.mean()),';',str(data_MC2_R.std() ),';',str(data_MC2_Y.mean() ),';',str(data_MC2_Y.std()),';',str(data_MC3_P.mean()),';',str(data_MC3_P.std()),';',str(data_MC3_R.mean() ),';',str(data_MC3_R.std()),';',str(data_MC3_Y.mean()),';',str(data_MC3_Y.std()),';',str(data_PR2_P.mean()),';',str(data_PR2_P.std()),';',str(data_PR2_R.mean() ),';',str(data_PR2_R.std()),';',str(data_PR2_Y.mean() ),';',str(data_PR2_Y.std()),';',str(data_PR3_P.mean()),';',str(data_PR3_P.std()),';',str(data_PR3_R.mean() ),';',str(data_PR3_R.std()),';',str( data_PR3_Y.mean()),';',str(data_PR3_Y.std()),';',str(data_PRM_P.mean()),';',str(data_PRM_P.std()),';',str(data_PRM_R.mean()),';',str(data_PRM_R.std()),';',str(data_PRM_Y.mean()),';',str(data_PRM_Y.std()),';',str(data_SR2_P.mean()),';',str(data_SR2_P.std()),';',str(data_SR2_R.mean()),';',str(data_SR2_R.std()),';',str(data_SR2_Y.mean() ),';',str(data_SR2_Y.std()),';',str( data_SR3_P.mean()),';',str(data_SR3_P.std()),';',str(data_SR3_R.mean() ),';',str(data_SR3_R.std()),';',str(data_SR3_Y.mean()),';',str(data_SR3_Y.std()),';',str(data_SRM_P.mean()),';',str(data_SRM_P.std()),';',str(data_SRM_R.mean()),';',str(data_SRM_R.std()),';',str(data_SRM_Y.mean()),';',str(data_SRM_Y.std())])

#f.close()

print "JOB DONE"
