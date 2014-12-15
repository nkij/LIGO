import matplotlib.pyplot as plt
from gwpy.time import Time
from gwpy.timeseries import (TimeSeries, TimeSeriesDict)
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

print "Import Modules Success"

#Start-End Time 
start = Time('2014-04-05 00:00:00', format='iso', scale='utc')
end = Time('2014-04-06 00:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps


channels_M0 = []
channels_M1 = []
OPTICS_M0 = ['ETMX','ITMX','ITMY']
OPTICS_M1 = ['BS', 'MC1', 'MC2', 'MC3', 'PR2', 'PR3', 'PRM', 'SR2', 'SR3', 'SRM' ]
DOFS = ['P', 'R', 'Y']
TRENDS = ['min','mean','max']

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

data_m0 = TimeSeriesDict.fetch(channels_M0, start, end, verbose=True)
data_m1 = TimeSeriesDict.fetch(channels_M1, start, end, verbose=True)

data_m1_BS_Pmin = data_m1[channels_M1[0]]
data_m1_BS_Pmean = data_m1[channels_M1[1]]
data_m1_BS_Pmax = data_m1[channels_M1[2]]
plot_BS_Pmin = data_m1_BS_Pmin.plot()
axBSP = plot_BS_Pmin.gca()
axBSP.plot(data_m1_BS_Pmean, label='Mean')
axBSP.plot(data_m1_BS_Pmax, label='Max')
axBSP.set_ylabel('Amplitude (urad)')
L = axBSP.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axBSP.yaxis.set_minor_locator(ml1)
axBSP.xaxis.set_minor_locator(ml2)
plot_BS_Pmin.save('L1-SUS-BS_M1_DAMP_Pmmm_INMON.png')

data_m1_BS_Rmin = data_m1[channels_M1[3]]
data_m1_BS_Rmean = data_m1[channels_M1[4]]
data_m1_BS_Rmax = data_m1[channels_M1[5]]
plot_BS_Rmin = data_m1_BS_Rmin.plot()
axBSR = plot_BS_Rmin.gca()
axBSR.plot(data_m1_BS_Rmean, label='Mean')
axBSR.plot(data_m1_BS_Rmax, label='Max')
axBSR.set_ylabel('Amplitude (urad)')
L = axBSR.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axBSR.yaxis.set_minor_locator(ml1)
axBSR.xaxis.set_minor_locator(ml2)
plot_BS_Rmin.save('L1-SUS-BS_M1_DAMP_Rmmm_INMON.png')

data_m1_BS_Ymin = data_m1[channels_M1[6]]
data_m1_BS_Ymean = data_m1[channels_M1[7]]
data_m1_BS_Ymax = data_m1[channels_M1[8]]
plot_BS_Ymin = data_m1_BS_Ymin.plot()
axBSY = plot_BS_Ymin.gca()
axBSY.plot(data_m1_BS_Ymean, label='Mean')
axBSY.plot(data_m1_BS_Ymax, label='Max')
axBSY.set_ylabel('Amplitude (urad)')
L = axBSY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axBSY.yaxis.set_minor_locator(ml1)
axBSY.xaxis.set_minor_locator(ml2)
plot_BS_Ymin.save('L1-SUS-BS_M1_DAMP_Ymmm_INMON.png')



data_m1_MC1_Pmin = data_m1[channels_M1[9]]
data_m1_MC1_Pmean = data_m1[channels_M1[10]]
data_m1_MC1_Pmax = data_m1[channels_M1[11]]
plot_MC1_Pmin = data_m1_MC1_Pmin.plot()
axMC1P = plot_MC1_Pmin.gca()
axMC1P.plot(data_m1_MC1_Pmean, label='Mean')
axMC1P.plot(data_m1_MC1_Pmax, label='Max')
axMC1P.set_ylabel('Amplitude (urad)')
L = axMC1P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC1P.yaxis.set_minor_locator(ml1)
axMC1P.xaxis.set_minor_locator(ml2)
plot_MC1_Pmin.save('L1-SUS-MC1_M1_DAMP_Pmmm_INMON.png')

data_m1_MC1_Rmin = data_m1[channels_M1[12]]
data_m1_MC1_Rmean = data_m1[channels_M1[13]]
data_m1_MC1_Rmax = data_m1[channels_M1[14]]
plot_MC1_Rmin = data_m1_MC1_Rmin.plot()
axMC1R = plot_MC1_Rmin.gca()
axMC1R.plot(data_m1_MC1_Rmean, label='Mean')
axMC1R.plot(data_m1_MC1_Rmax, label='Max')
axMC1R.set_ylabel('Amplitude (urad)')
L = axMC1R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC1R.yaxis.set_minor_locator(ml1)
axMC1R.xaxis.set_minor_locator(ml2)
plot_MC1_Rmin.save('L1-SUS-MC1_M1_DAMP_Rmmm_INMON.png')


data_m1_MC1_Ymin = data_m1[channels_M1[15]]
data_m1_MC1_Ymean = data_m1[channels_M1[16]]
data_m1_MC1_Ymax = data_m1[channels_M1[17]]
plot_MC1_Ymin = data_m1_MC1_Ymin.plot()
axMC1Y = plot_MC1_Ymin.gca()
axMC1Y.plot(data_m1_MC1_Ymean, label='Mean')
axMC1Y.plot(data_m1_MC1_Ymax, label='Max')
axMC1Y.set_ylabel('Amplitude (urad)')
L = axMC1Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC1Y.yaxis.set_minor_locator(ml1)
axMC1Y.xaxis.set_minor_locator(ml2)
plot_MC1_Ymin.save('L1-SUS-MC1_M1_DAMP_Ymmm_INMON.png')



data_m1_MC2_Pmin = data_m1[channels_M1[18]]
data_m1_MC2_Pmean = data_m1[channels_M1[19]]
data_m1_MC2_Pmax = data_m1[channels_M1[20]]
plot_MC2_Pmin = data_m1_MC2_Pmin.plot()
axMC2P = plot_MC2_Pmin.gca()
axMC2P.plot(data_m1_MC2_Pmean, label='Mean')
axMC2P.plot(data_m1_MC2_Pmax, label='Max')
axMC2P.set_ylabel('Amplitude (urad)')
L = axMC2P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC2P.yaxis.set_minor_locator(ml1)
axMC2P.xaxis.set_minor_locator(ml2)
plot_MC2_Pmin.save('L1-SUS-MC2_M1_DAMP_Pmmm_INMON.png')

data_m1_MC2_Rmin = data_m1[channels_M1[21]]
data_m1_MC2_Rmean = data_m1[channels_M1[22]]
data_m1_MC2_Rmax = data_m1[channels_M1[23]]
plot_MC2_Rmin = data_m1_MC2_Rmin.plot()
axMC2R = plot_MC2_Rmin.gca()
axMC2R.plot(data_m1_MC2_Rmean, label='Mean')
axMC2R.plot(data_m1_MC2_Rmax, label='Max')
axMC2R.set_ylabel('Amplitude (urad)')
L = axMC2R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC2R.yaxis.set_minor_locator(ml1)
axMC2R.xaxis.set_minor_locator(ml2)
plot_MC2_Rmin.save('L1-SUS-MC2_M1_DAMP_Rmmm_INMON.png')

data_m1_MC2_Ymin = data_m1[channels_M1[24]]
data_m1_MC2_Ymean = data_m1[channels_M1[25]]
data_m1_MC2_Ymax = data_m1[channels_M1[26]]
plot_MC2_Ymin = data_m1_MC2_Ymin.plot()
axMC2Y = plot_MC2_Ymin.gca()
axMC2Y.plot(data_m1_MC2_Ymean, label='Mean')
axMC2Y.plot(data_m1_MC2_Ymax, label='Max')
axMC2Y.set_ylabel('Amplitude (urad)')
L = axMC2Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC2Y.yaxis.set_minor_locator(ml1)
axMC2Y.xaxis.set_minor_locator(ml2)
plot_MC2_Ymin.save('L1-SUS-MC2_M1_DAMP_Ymmm_INMON.png')


data_m1_MC3_Pmin = data_m1[channels_M1[27]]
data_m1_MC3_Pmean = data_m1[channels_M1[28]]
data_m1_MC3_Pmax = data_m1[channels_M1[29]]
plot_MC3_Pmin = data_m1_MC3_Pmin.plot()
axMC3P = plot_MC3_Pmin.gca()
axMC3P.plot(data_m1_MC3_Pmean, label='Mean')
axMC3P.plot(data_m1_MC3_Pmax, label='Max')
axMC3P.set_ylabel('Amplitude (urad)')
L = axMC3P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC3P.yaxis.set_minor_locator(ml1)
axMC3P.xaxis.set_minor_locator(ml2)
plot_MC3_Pmin.save('L1-SUS-MC3_M1_DAMP_Pmmm_INMON.png')

data_m1_MC3_Rmin = data_m1[channels_M1[30]]
data_m1_MC3_Rmean = data_m1[channels_M1[31]]
data_m1_MC3_Rmax = data_m1[channels_M1[32]]
plot_MC3_Rmin = data_m1_MC3_Rmin.plot()
axMC3R = plot_MC3_Rmin.gca()
axMC3R.plot(data_m1_MC3_Rmean, label='Mean')
axMC3R.plot(data_m1_MC3_Rmax, label='Max')
axMC3R.set_ylabel('Amplitude (urad)')
L = axMC3R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC3R.yaxis.set_minor_locator(ml1)
axMC3R.xaxis.set_minor_locator(ml2)
plot_MC3_Rmin.save('L1-SUS-MC3_M1_DAMP_Rmmm_INMON.png')

data_m1_MC3_Ymin = data_m1[channels_M1[33]]
data_m1_MC3_Ymean = data_m1[channels_M1[34]]
data_m1_MC3_Ymax = data_m1[channels_M1[35]]
plot_MC3_Ymin = data_m1_MC3_Ymin.plot()
axMC3Y = plot_MC3_Ymin.gca()
axMC3Y.plot(data_m1_MC3_Ymean, label='Mean')
axMC3Y.plot(data_m1_MC3_Ymax, label='Max')
axMC3Y.set_ylabel('Amplitude (urad)')
L = axMC3Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axMC3Y.yaxis.set_minor_locator(ml1)
axMC3Y.xaxis.set_minor_locator(ml2)
plot_MC3_Ymin.save('L1-SUS-MC3_M1_DAMP_Ymmm_INMON.png')


data_m1_PR2_Pmin = data_m1[channels_M1[36]]
data_m1_PR2_Pmean = data_m1[channels_M1[37]]
data_m1_PR2_Pmax = data_m1[channels_M1[38]]
plot_PR2_Pmin = data_m1_PR2_Pmin.plot()
axPR2P = plot_PR2_Pmin.gca()
axPR2P.plot(data_m1_PR2_Pmean, label='Mean')
axPR2P.plot(data_m1_PR2_Pmax, label='Max')
axPR2P.set_ylabel('Amplitude (urad)')
L = axPR2P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPR2P.yaxis.set_minor_locator(ml1)
axPR2P.xaxis.set_minor_locator(ml2)
plot_PR2_Pmin.save('L1-SUS-PR2_M1_DAMP_Pmmm_INMON.png')

data_m1_PR2_Rmin = data_m1[channels_M1[39]]
data_m1_PR2_Rmean = data_m1[channels_M1[40]]
data_m1_PR2_Rmax = data_m1[channels_M1[41]]
plot_PR2_Rmin = data_m1_PR2_Rmin.plot()
axPR2R = plot_PR2_Rmin.gca()
axPR2R.plot(data_m1_PR2_Rmean, label='Mean')
axPR2R.plot(data_m1_PR2_Rmax, label='Max')
axPR2R.set_ylabel('Amplitude (urad)')
L = axPR2R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPR2R.yaxis.set_minor_locator(ml1)
axPR2R.xaxis.set_minor_locator(ml2)
plot_PR2_Rmin.save('L1-SUS-PR2_M1_DAMP_Rmmm_INMON.png')

data_m1_PR2_Ymin = data_m1[channels_M1[42]]
data_m1_PR2_Ymean = data_m1[channels_M1[43]]
data_m1_PR2_Ymax = data_m1[channels_M1[44]]
plot_PR2_Ymin = data_m1_PR2_Ymin.plot()
axPR2Y = plot_PR2_Ymin.gca()
axPR2Y.plot(data_m1_PR2_Ymean, label='Mean')
axPR2Y.plot(data_m1_PR2_Ymax, label='Max')
axPR2Y.set_ylabel('Amplitude (urad)')
L = axPR2Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPR2Y.yaxis.set_minor_locator(ml1)
axPR2Y.xaxis.set_minor_locator(ml2)
plot_PR2_Ymin.save('L1-SUS-PR2_M1_DAMP_Ymmm_INMON.png')


data_m1_PR3_Pmin = data_m1[channels_M1[45]]
data_m1_PR3_Pmean = data_m1[channels_M1[46]]
data_m1_PR3_Pmax = data_m1[channels_M1[47]]
plot_PR3_Pmin = data_m1_PR3_Pmin.plot()
axPR3P = plot_PR3_Pmin.gca()
axPR3P.plot(data_m1_PR3_Pmean, label='Mean')
axPR3P.plot(data_m1_PR3_Pmax, label='Max')
axPR3P.set_ylabel('Amplitude (urad)')
L = axPR3P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPR3P.yaxis.set_minor_locator(ml1)
axPR3P.xaxis.set_minor_locator(ml2)
plot_PR3_Pmin.save('L1-SUS-PR3_M1_DAMP_Pmmm_INMON.png')

data_m1_PR3_Rmin = data_m1[channels_M1[48]]
data_m1_PR3_Rmean = data_m1[channels_M1[49]]
data_m1_PR3_Rmax = data_m1[channels_M1[50]]
plot_PR3_Rmin = data_m1_PR3_Rmin.plot()
axPR3R = plot_PR3_Rmin.gca()
axPR3R.plot(data_m1_PR3_Rmean, label='Mean')
axPR3R.plot(data_m1_PR3_Rmax, label='Max')
axPR3R.set_ylabel('Amplitude (urad)')
L = axPR3R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPR3R.yaxis.set_minor_locator(ml1)
axPR3R.xaxis.set_minor_locator(ml2)
plot_PR3_Rmin.save('L1-SUS-PR3_M1_DAMP_Rmmm_INMON.png')

data_m1_PR3_Ymin = data_m1[channels_M1[51]]
data_m1_PR3_Ymean = data_m1[channels_M1[52]]
data_m1_PR3_Ymax = data_m1[channels_M1[53]]
plot_PR3_Ymin = data_m1_PR3_Ymin.plot()
axPR3Y = plot_PR3_Ymin.gca()
axPR3Y.plot(data_m1_PR3_Ymean, label='Mean')
axPR3Y.plot(data_m1_PR3_Ymax, label='Max')
axPR3Y.set_ylabel('Amplitude (urad)')
L = axPR3Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPR3Y.yaxis.set_minor_locator(ml1)
axPR3Y.xaxis.set_minor_locator(ml2)
plot_PR3_Ymin.save('L1-SUS-PR3_M1_DAMP_Ymmm_INMON.png')



data_m1_PRM_Pmin = data_m1[channels_M1[54]]
data_m1_PRM_Pmean = data_m1[channels_M1[55]]
data_m1_PRM_Pmax = data_m1[channels_M1[56]]
plot_PRM_Pmin = data_m1_PRM_Pmin.plot()
axPRMP = plot_PRM_Pmin.gca()
axPRMP.plot(data_m1_PRM_Pmean, label='Mean')
axPRMP.plot(data_m1_PRM_Pmax, label='Max')
axPRMP.set_ylabel('Amplitude (urad)')
L = axPRMP.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPRMP.yaxis.set_minor_locator(ml1)
axPRMP.xaxis.set_minor_locator(ml2)
plot_PRM_Pmin.save('L1-SUS-PRM_M1_DAMP_Pmmm_INMON.png')

data_m1_PRM_Rmin = data_m1[channels_M1[57]]
data_m1_PRM_Rmean = data_m1[channels_M1[58]]
data_m1_PRM_Rmax = data_m1[channels_M1[59]]
plot_PRM_Rmin = data_m1_PRM_Rmin.plot()
axPRMR = plot_PRM_Rmin.gca()
axPRMR.plot(data_m1_PRM_Rmean, label='Mean')
axPRMR.plot(data_m1_PRM_Rmax, label='Max')
axPRMR.set_ylabel('Amplitude (urad)')
L = axPRMR.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPRMR.yaxis.set_minor_locator(ml1)
axPRMR.xaxis.set_minor_locator(ml2)
plot_PRM_Rmin.save('L1-SUS-PRM_M1_DAMP_Rmmm_INMON.png')

data_m1_PRM_Ymin = data_m1[channels_M1[60]]
data_m1_PRM_Ymean = data_m1[channels_M1[61]]
data_m1_PRM_Ymax = data_m1[channels_M1[62]]
plot_PRM_Ymin = data_m1_PRM_Ymin.plot()
axPRMY = plot_PRM_Ymin.gca()
axPRMY.plot(data_m1_PRM_Ymean, label='Mean')
axPRMY.plot(data_m1_PRM_Ymax, label='Max')
axPRMY.set_ylabel('Amplitude (urad)')
L = axPRMY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axPRMY.yaxis.set_minor_locator(ml1)
axPRMY.xaxis.set_minor_locator(ml2)
plot_PRM_Ymin.save('L1-SUS-PRM_M1_DAMP_Ymmm_INMON.png')


data_m1_SR2_Pmin = data_m1[channels_M1[63]]
data_m1_SR2_Pmean = data_m1[channels_M1[64]]
data_m1_SR2_Pmax = data_m1[channels_M1[65]]
plot_SR2_Pmin = data_m1_SR2_Pmin.plot()
axSR2P = plot_SR2_Pmin.gca()
axSR2P.plot(data_m1_SR2_Pmean, label='Mean')
axSR2P.plot(data_m1_SR2_Pmax, label='Max')
axSR2P.set_ylabel('Amplitude (urad)')
L = axSR2P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSR2P.yaxis.set_minor_locator(ml1)
axSR2P.xaxis.set_minor_locator(ml2)
plot_SR2_Pmin.save('L1-SUS-SR2_M1_DAMP_Pmmm_INMON.png')

data_m1_SR2_Rmin = data_m1[channels_M1[66]]
data_m1_SR2_Rmean = data_m1[channels_M1[67]]
data_m1_SR2_Rmax = data_m1[channels_M1[68]]
plot_SR2_Rmin = data_m1_SR2_Rmin.plot()
axSR2R = plot_SR2_Rmin.gca()
axSR2R.plot(data_m1_SR2_Rmean, label='Mean')
axSR2R.plot(data_m1_SR2_Rmax, label='Max')
axSR2R.set_ylabel('Amplitude (urad)')
L = axSR2R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSR2R.yaxis.set_minor_locator(ml1)
axSR2R.xaxis.set_minor_locator(ml2)
plot_SR2_Rmin.save('L1-SUS-SR2_M1_DAMP_Rmmm_INMON.png')

data_m1_SR2_Ymin = data_m1[channels_M1[69]]
data_m1_SR2_Ymean = data_m1[channels_M1[70]]
data_m1_SR2_Ymax = data_m1[channels_M1[71]]
plot_SR2_Ymin = data_m1_SR2_Ymin.plot()
axSR2Y = plot_SR2_Ymin.gca()
axSR2Y.plot(data_m1_SR2_Ymean, label='Mean')
axSR2Y.plot(data_m1_SR2_Ymax, label='Max')
axSR2Y.set_ylabel('Amplitude (urad)')
L = axSR2Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSR2Y.yaxis.set_minor_locator(ml1)
axSR2Y.xaxis.set_minor_locator(ml2)
plot_SR2_Ymin.save('L1-SUS-SR2_M1_DAMP_Ymmm_INMON.png')


data_m1_SR3_Pmin = data_m1[channels_M1[72]]
data_m1_SR3_Pmean = data_m1[channels_M1[73]]
data_m1_SR3_Pmax = data_m1[channels_M1[74]]
plot_SR3_Pmin = data_m1_SR3_Pmin.plot()
axSR3P = plot_SR3_Pmin.gca()
axSR3P.plot(data_m1_SR3_Pmean, label='Mean')
axSR3P.plot(data_m1_SR3_Pmax, label='Max')
axSR3P.set_ylabel('Amplitude (urad)')
L = axSR3P.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSR3P.yaxis.set_minor_locator(ml1)
axSR3P.xaxis.set_minor_locator(ml2)
plot_SR3_Pmin.save('L1-SUS-SR3_M1_DAMP_Pmmm_INMON.png')

data_m1_SR3_Rmin = data_m1[channels_M1[75]]
data_m1_SR3_Rmean = data_m1[channels_M1[76]]
data_m1_SR3_Rmax = data_m1[channels_M1[77]]
plot_SR3_Rmin = data_m1_SR3_Rmin.plot()
axSR3R = plot_SR3_Rmin.gca()
axSR3R.plot(data_m1_SR3_Rmean, label='Mean')
axSR3R.plot(data_m1_SR3_Rmax, label='Max')
axSR3R.set_ylabel('Amplitude (urad)')
L = axSR3R.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSR3R.yaxis.set_minor_locator(ml1)
axSR3R.xaxis.set_minor_locator(ml2)
plot_SR3_Rmin.save('L1-SUS-SR3_M1_DAMP_Rmmm_INMON.png')

data_m1_SR3_Ymin = data_m1[channels_M1[78]]
data_m1_SR3_Ymean = data_m1[channels_M1[79]]
data_m1_SR3_Ymax = data_m1[channels_M1[80]]
plot_SR3_Ymin = data_m1_SR3_Ymin.plot()
axSR3Y = plot_SR3_Ymin.gca()
axSR3Y.plot(data_m1_SR3_Ymean, label='Mean')
axSR3Y.plot(data_m1_SR3_Ymax, label='Max')
axSR3Y.set_ylabel('Amplitude (urad)')
L = axSR3Y.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSR3Y.yaxis.set_minor_locator(ml1)
axSR3Y.xaxis.set_minor_locator(ml2)
plot_SR3_Ymin.save('L1-SUS-SR3_M1_DAMP_Ymmm_INMON.png')



data_m1_SRM_Pmin = data_m1[channels_M1[81]]
data_m1_SRM_Pmean = data_m1[channels_M1[82]]
data_m1_SRM_Pmax = data_m1[channels_M1[83]]
plot_SRM_Pmin = data_m1_SRM_Pmin.plot()
axSRMP = plot_SRM_Pmin.gca()
axSRMP.plot(data_m1_SRM_Pmean, label='Mean')
axSRMP.plot(data_m1_SRM_Pmax, label='Max')
axSRMP.set_ylabel('Amplitude (urad)')
L = axSRMP.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSRMP.yaxis.set_minor_locator(ml1)
axSRMP.xaxis.set_minor_locator(ml2)
plot_SRM_Pmin.save('L1-SUS-SRM_M1_DAMP_Pmmm_INMON.png')

data_m1_SRM_Rmin = data_m1[channels_M1[84]]
data_m1_SRM_Rmean = data_m1[channels_M1[85]]
data_m1_SRM_Rmax = data_m1[channels_M1[86]]
plot_SRM_Rmin = data_m1_SRM_Rmin.plot()
axSRMR = plot_SRM_Rmin.gca()
axSRMR.plot(data_m1_SRM_Rmean, label='Mean')
axSRMR.plot(data_m1_SRM_Rmax, label='Max')
axSRMR.set_ylabel('Amplitude (urad)')
L = axSRMR.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSRMR.yaxis.set_minor_locator(ml1)
axSRMR.xaxis.set_minor_locator(ml2)
plot_SRM_Rmin.save('L1-SUS-SRM_M1_DAMP_Rmmm_INMON.png')

data_m1_SRM_Ymin = data_m1[channels_M1[87]]
data_m1_SRM_Ymean = data_m1[channels_M1[88]]
data_m1_SRM_Ymax = data_m1[channels_M1[89]]
plot_SRM_Ymin = data_m1_SRM_Ymin.plot()
axSRMY = plot_SRM_Ymin.gca()
axSRMY.plot(data_m1_SRM_Ymean, label='Mean')
axSRMY.plot(data_m1_SRM_Ymax, label='Max')
axSRMY.set_ylabel('Amplitude (urad)')
L = axSRMY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axSRMY.yaxis.set_minor_locator(ml1)
axSRMY.xaxis.set_minor_locator(ml2)
plot_SRM_Ymin.save('L1-SUS-SRM_M1_DAMP_Ymmm_INMON.png')



#data_M0

data_m0_ETMX_Pmin = data_m0[channels_M0[0]]
data_m0_ETMX_Pmean = data_m0[channels_M0[1]]
data_m0_ETMX_Pmax = data_m0[channels_M0[2]]
plot_ETMX_Pmin = data_m0_ETMX_Pmin.plot()
axETMXP = plot_ETMX_Pmin.gca()
axETMXP.plot(data_m0_ETMX_Pmean, label='Mean')
axETMXP.plot(data_m0_ETMX_Pmax, label='Max')
axETMXP.set_ylabel('Amplitude (urad)')
L = axETMXP.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axETMXP.yaxis.set_minor_locator(ml1)
axETMXP.xaxis.set_minor_locator(ml2)
plot_ETMX_Pmin.save('L1-SUS-ETMX_M0_DAMP_Pmmm_INMON.png')

data_m0_ETMX_Rmin = data_m0[channels_M0[3]]
data_m0_ETMX_Rmean = data_m0[channels_M0[4]]
data_m0_ETMX_Rmax = data_m0[channels_M0[5]]
plot_ETMX_Rmin = data_m0_ETMX_Rmin.plot()
axETMXR = plot_ETMX_Rmin.gca()
axETMXR.plot(data_m0_ETMX_Rmean, label='Mean')
axETMXR.plot(data_m0_ETMX_Rmax, label='Max')
axETMXR.set_ylabel('Amplitude (urad)')
L = axETMXR.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axETMXR.yaxis.set_minor_locator(ml1)
axETMXR.xaxis.set_minor_locator(ml2)
plot_ETMX_Rmin.save('L1-SUS-ETMX_M0_DAMP_Rmmm_INMON.png')

data_m0_ETMX_Ymin = data_m0[channels_M0[6]]
data_m0_ETMX_Ymean = data_m0[channels_M0[7]]
data_m0_ETMX_Ymax = data_m0[channels_M0[8]]
plot_ETMX_Ymin = data_m0_ETMX_Ymin.plot()
axETMXY = plot_ETMX_Ymin.gca()
axETMXY.plot(data_m0_ETMX_Ymean, label='Mean')
axETMXY.plot(data_m0_ETMX_Ymax, label='Max')
axETMXY.set_ylabel('Amplitude (urad)')
L = axETMXY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axETMXY.yaxis.set_minor_locator(ml1)
axETMXY.xaxis.set_minor_locator(ml2)
plot_ETMX_Ymin.save('L1-SUS-ETMX_M0_DAMP_Ymmm_INMON.png')


data_m0_ITMX_Pmin = data_m0[channels_M0[9]]
data_m0_ITMX_Pmean = data_m0[channels_M0[10]]
data_m0_ITMX_Pmax = data_m0[channels_M0[11]]
plot_ITMX_Pmin = data_m0_ITMX_Pmin.plot()
axITMXP = plot_ITMX_Pmin.gca()
axITMXP.plot(data_m0_ITMX_Pmean, label='Mean')
axITMXP.plot(data_m0_ITMX_Pmax, label='Max')
axITMXP.set_ylabel('Amplitude (urad)')
L = axITMXP.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axITMXP.yaxis.set_minor_locator(ml1)
axITMXP.xaxis.set_minor_locator(ml2)
plot_ITMX_Pmin.save('L1-SUS-ITMX_M0_DAMP_Pmmm_INMON.png')

data_m0_ITMX_Rmin = data_m0[channels_M0[12]]
data_m0_ITMX_Rmean = data_m0[channels_M0[13]]
data_m0_ITMX_Rmax = data_m0[channels_M0[14]]
plot_ITMX_Rmin = data_m0_ITMX_Rmin.plot()
axITMXR = plot_ITMX_Rmin.gca()
axITMXR.plot(data_m0_ITMX_Rmean, label='Mean')
axITMXR.plot(data_m0_ITMX_Rmax, label='Max')
axITMXR.set_ylabel('Amplitude (urad)')
L = axITMXR.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axITMXR.yaxis.set_minor_locator(ml1)
axITMXR.xaxis.set_minor_locator(ml2)
plot_ITMX_Rmin.save('L1-SUS-ITMX_M0_DAMP_Rmmm_INMON.png')

data_m0_ITMX_Ymin = data_m0[channels_M0[15]]
data_m0_ITMX_Ymean = data_m0[channels_M0[16]]
data_m0_ITMX_Ymax = data_m0[channels_M0[17]]
plot_ITMX_Ymin = data_m0_ITMX_Ymin.plot()
axITMXY = plot_ITMX_Ymin.gca()
axITMXY.plot(data_m0_ITMX_Ymean, label='Mean')
axITMXY.plot(data_m0_ITMX_Ymax, label='Max')
axITMXY.set_ylabel('Amplitude (urad)')
L = axITMXY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axITMXY.yaxis.set_minor_locator(ml1)
axITMXY.xaxis.set_minor_locator(ml2)
plot_ITMX_Ymin.save('L1-SUS-ITMX_M0_DAMP_Ymmm_INMON.png')


data_m0_ITMY_Pmin = data_m0[channels_M0[18]]
data_m0_ITMY_Pmean = data_m0[channels_M0[19]]
data_m0_ITMY_Pmax = data_m0[channels_M0[20]]
plot_ITMY_Pmin = data_m0_ITMY_Pmin.plot()
axITMYP = plot_ITMY_Pmin.gca()
axITMYP.plot(data_m0_ITMY_Pmean, label='Mean')
axITMYP.plot(data_m0_ITMY_Pmax, label='Max')
axITMYP.set_ylabel('Amplitude (urad)')
L = axITMYP.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axITMYP.yaxis.set_minor_locator(ml1)
axITMYP.xaxis.set_minor_locator(ml2)
plot_ITMY_Pmin.save('L1-SUS-ITMY_M0_DAMP_Pmmm_INMON.png')

data_m0_ITMY_Rmin = data_m0[channels_M0[21]]
data_m0_ITMY_Rmean = data_m0[channels_M0[22]]
data_m0_ITMY_Rmax = data_m0[channels_M0[23]]
plot_ITMY_Rmin = data_m0_ITMY_Rmin.plot()
axITMYR = plot_ITMY_Rmin.gca()
axITMYR.plot(data_m0_ITMY_Rmean, label='Mean')
axITMYR.plot(data_m0_ITMY_Rmax, label='Max')
axITMYR.set_ylabel('Amplitude (urad)')
L = axITMYR.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axITMYR.yaxis.set_minor_locator(ml1)
axITMYR.xaxis.set_minor_locator(ml2)
plot_ITMY_Rmin.save('L1-SUS-ITMY_M0_DAMP_Rmmm_INMON.png')

data_m0_ITMY_Ymin = data_m0[channels_M0[24]]
data_m0_ITMY_Ymean = data_m0[channels_M0[25]]
data_m0_ITMY_Ymax = data_m0[channels_M0[26]]
plot_ITMY_Ymin = data_m0_ITMY_Ymin.plot()
axITMYY = plot_ITMY_Ymin.gca()
axITMYY.plot(data_m0_ITMY_Ymean, label='Mean')
axITMYY.plot(data_m0_ITMY_Ymax, label='Max')
axITMYY.set_ylabel('Amplitude (urad)')
L = axITMYY.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
L.get_texts()[0].set_text('Min')
ml1 = MultipleLocator(10)
ml2 = MultipleLocator(3600)
axITMYY.yaxis.set_minor_locator(ml1)
axITMYY.xaxis.set_minor_locator(ml2)
plot_ITMY_Ymin.save('L1-SUS-ITMY_M0_DAMP_Ymmm_INMON.png')
