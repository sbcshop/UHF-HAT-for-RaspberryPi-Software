'''
region represents the regulatory region that the device will operate in. Supported values are:
"NA", North America/FCC
"NA2", Reduced FCC region
"NA3", 5MHZ FCC band
"EU", European Union/ETSI EN 302 208
"EU2", European Union/ETSI EN 300 220
"EU3", European Union/ETSI Revised EN 302 208
"EU4", 4 channels (916.3MHz, 917.5MHz, 918.7MHz)
"IS", Israel
"IN", India
"JP", Japan
"JP2", Japan 24dBm with 13 channels
"JP3", Japan 24dBm with 6 channels
"KR", Korea MIC
"KR2", Korea KCC
"PRC", China
`"PRC2", China 840MHZ
"AU", Australia/AIDA LIPD Variation 2011
"NZ", New Zealand
'''

import mercury
import time

time.sleep(2)

reader = mercury.Reader("tmr:///dev/ttyS0")

reader.set_region("EU3")
reader.set_read_plan([1], "GEN2")



# Lists supported regions for the connected device.
print("Support Regions = ",reader.get_supported_regions())


# Lists supported radio power range, in centidBm.
print("supported radio power range = ",reader.get_power_range())


# Gets the frequencies for the reader to use, in kHz.
print("frequencies for the reader to use = ",reader.get_hop_table())


# Sets the frequencies for the reader to use, in kHz.
#reader.set_hop_table(list)


# Gets the frequency hop time, in milliseconds.
print("frequency hop time",str(reader.get_hop_time())+" ms")


# Sets the frequency hop time, in milliseconds.
#reader.set_hop_time(num)


# Lists available antennas.
print("Anteena Available = ",reader.get_antennas())

