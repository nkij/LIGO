#This program plots ISI_ITMX CPS spectrum around 1099109374.275391 (Nov 3 2014 20:08:51 PST/Nov 4 2014 04:08:51)
#Before trips 253-373
#After trips 374-494

from gwpy.timeseries import TimeSeries



print "Import Module Success"

H1CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_H1_IN1_DQ', 1099109253.275391, 1099109373.275391)
H2CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_H2_IN1_DQ', 1099109253.275391, 1099109373.275391)
V1CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_V1_IN1_DQ', 1099109253.275391, 1099109373.275391)
V2CPS = TimeSeries.fetch('H1:ISI-ITMX_ST1_CPSINF_V2_IN1_DQ', 1099109253.275391, 1099109373.275391)

print "Data Fetched"

H1CPSASD = H1CPS.asd(40, 20)
H2CPSASD = H1CPS.asd(40, 20)
V1CPSASD = V1CPS.asd(40, 20)
V2CPSASD = H1CPS.asd(40, 20)

plot_H1 = H1CPSASD.plot(color='b', label='H1:ISI-ITMX\_ST1\_CPSINF\_H1\_IN1\_DQ-2minBeforetrips')
ax = plot_H1.gca()
#ax.set_xlim(1,100)
ax.set_ylim(1,120)
ax.plot(V1CPSASD, color='g', label='H1:ISI-ITMX\_ST1\_CPSINF\_V1\_IN1\_DQ-2minBeforetrips')
ax.plot(H2CPSASD, color='r', label='H1:ISI-ITMX\_ST1\_CPSINF\_H2\_IN1\_DQ-2minBeforetrips')
ax.plot(V2CPSASD, color='k', label='H1:ISI-ITMX\_ST1\_CPSINF\_V2\_IN1\_DQ-2minBeforetrips')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel(r'Noise ASD [1/$\sqrt{\mathrm{Hz}}$]')
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_right()
ax.grid(True, which='both', axis='both')

print 'plotting'

plot_H1.show()
#plot_H1.save('120s_spectrum40-20_aftertrips.png')
