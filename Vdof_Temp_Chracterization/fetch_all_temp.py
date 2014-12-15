from gwpy.time import Time
from gwpy.timeseries import TimeSeries
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

start = Time('2014-11-27 21:00:00', format='iso', scale='utc')
end = Time('2014-12-01 21:00:00', format='iso', scale='utc')
print start.iso, start.gps
print end.iso, end.gps

#total 12 channels

BSC = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE1_TP1.mean,m-trend', start, end, verbose=True)
HAM2_d = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE5_TP6.mean,m-trend', start, end, verbose=True)
HAM2_u = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE5_TP2.mean,m-trend', start, end, verbose=True)
HAM1_u = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE5_TP3.mean,m-trend', start, end, verbose=True)
HAM1_d = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE5_TP7.mean,m-trend', start, end, verbose=True)
HAM3_4 = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE1_TP3.mean,m-trend', start, end, verbose=True)
HAM5 = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE4_TP2.mean,m-trend', start, end, verbose=True)
HAM6 = TimeSeries.fetch('L0:FMC-CS_LVEA_ZONE4_TP3.mean,m-trend', start, end, verbose=True)

 
BSC_C = (BSC-32)*(5.0/9)
HAM2_d_C = (HAM2_d-32)*(5.0/9)
HAM2_u_C = (HAM2_u-32)*(5.0/9)
HAM1_u_C = (HAM1_u-32)*(5.0/9)
HAM1_d_C = (HAM1_d-32)*(5.0/9)
HAM3_4_C = (HAM3_4-32)*(5.0/9)
HAM5_C = (HAM5-32)*(5.0/9)
HAM6_C = (HAM6-32)*(5.0/9)


print 'data fetched'

# plot the BSC_C TimeSeries and return the resulting 'Figure'
plot_BSC = BSC_C.plot()
# get current Axes (gca) of this Figure
ax_temp = plot_BSC.gca()

ax_temp.plot(HAM2_d_C, label = 'L0:FMC-CS\_LVEA\_ZONE5\_TP6.mean')
ax_temp.plot(HAM2_u_C, label = 'L0:FMC-CS\_LVEA\_ZONE5\_TP2.mean')
ax_temp.plot(HAM1_u_C, label = 'L0:FMC-CS\_LVEA\_ZONE5\_TP3.mean')
ax_temp.plot(HAM1_d_C, label = 'L0:FMC-CS\_LVEA\_ZONE5\_TP7.mean')
ax_temp.plot(HAM3_4_C, label = 'L0:FMC-CS\_LVEA\_ZONE1\_TP3.mean')
ax_temp.plot(HAM5_C, label = 'L0:FMC-CS\_LVEA\_ZONE4\_TP2.mean')
ax_temp.plot(HAM6_C, label = 'L0:FMC-CS\_LVEA\_ZONE4\_TP3.mean')

ax_temp.set_ylim(17,20)
ax_temp.set_ylabel('Temperature (C)')
ax_temp.set_title('FMC Temp (4 days)')
ax_temp.legend(loc='upper right', ncol=2, fancybox=True, shadow=True)
#mj  = MultipleLocator(1)
ml1 = MultipleLocator(0.1)
#ax1.yaxis.set_major_locator(mj)
ax_temp.yaxis.set_minor_locator(ml1)

print ' plotting'

plot_BSC.show()
