import csv

x = ['yar, this is a string and also a number: ', 3.1415]

fName = 'C:\\users\\mallison\\Desktop\\yar.csv'
with open(fName, 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(x)

# def export_header_data(self):
# 		# Experimental
# 		# This function exports header data to a csv file
# 		fName = self.outFile + '.csv'
# 		with open(fName, 'w') as csvfile:
# 			hWriter = csv.writer(csvfile)
# 			hWriter.writerow('\nFILE INFO')
# 			hWriter.writerow('FileID: {}'.format(self.vInfo.fileid.decode()))
# 			hWriter.writerow('Endian Check: {:#x}'.format(self.vInfo.endian[0]))
# 			hWriter.writerow('File Format Version: {0[0]}.{0[1]}.{0[2]}.{0[3]}'.format(
# 				self.vInfo.fFormatVer))
# 			hWriter.writerow('API Version: {0[0]}.{0[1]}.{0[2]}.{0[3]}'.format(
# 				self.vInfo.apiVersion))
# 			hWriter.writerow('FX3 Version: {0[0]}.{0[1]}.{0[2]}.{0[3]}'.format(
# 				self.vInfo.fx3Version))
# 			hWriter.writerow('FPGA Version: {0[0]}.{0[1]}.{0[2]}.{0[3]}'.format(
# 				self.vInfo.fpgaVersion))
# 			hWriter.writerow('Device Serial Number: {}'.format(self.vInfo.deviceSN.decode()))

# 			hWriter.writerow('\nINSTRUMENT STATE')
# 			hWriter.writerow('Reference Level: {:.2f} dBm'.format(
# 				self.instState.refLevel[0]))
# 			hWriter.writerow('Center Frequency: {} Hz'.format(
# 				self.instState.cf[0]))
# 			hWriter.writerow('temp: {} C'.format(self.instState.temp[0]))
# 			hWriter.writerow('Alignment status: {}'.format(self.instState.alignment[0]))
# 			hWriter.writerow('Frequency Reference: {}'.format(self.instState.freqRef[0]))
# 			hWriter.writerow('Trigger mode: {}'.format(self.instState.trigMode[0]))
# 			hWriter.writerow('Trigger Source: {}'.format(self.instState.trigSource[0]))
# 			hWriter.writerow('Trigger Transition: {}'.format(self.instState.trigTrans[0]))
# 			hWriter.writerow('Trigger Level: {} dBm'.format(self.instState.trigLevel[0]))

# 			hWriter.writerow('\nDATA FORMAT')
# 			hWriter.writerow('Data Type: {} bytes per sample'.format(self.dFormat.dataType))
# 			hWriter.writerow('Offset to first frame (bytes): {}'.format(self.dFormat.frameOffset[0]))
# 			hWriter.writerow('Frame Size (bytes): {}'.format(self.dFormat.frameSize[0]))
# 			hWriter.writerow('Offset to sample data (bytes): {}'.format(self.dFormat.sampleOffset[0]))
# 			hWriter.writerow('Samples in Frame: {}'.format(self.dFormat.sampleSize[0]))
# 			hWriter.writerow('Offset to non-sample data: {}'.format(self.dFormat.nonsampleOffset[0]))
# 			hWriter.writerow('Size of non-sample data: {}'.format(self.dFormat.nonSampleSize[0]))
# 			hWriter.writerow('IF Center Frequency: {} Hz'.format(
# 				self.dFormat.ifcf[0]))
# 			hWriter.writerow('Sample Rate: {} S/sec'.format(self.dFormat.sRate[0]))
# 			hWriter.writerow('Bandwidth: {} Hz'.format(self.dFormat.bandwidth[0]))
# 			hWriter.writerow('Corrected data status: {}'.format(self.dFormat.corrected[0]))
# 			hWriter.writerow('Time Type (0=local, 1=remote): {}'.format(self.dFormat.timeType[0]))
# 			hWriter.writerow('Reference Time: {0[1]}/{0[2]}/{0[0]} at {0[3]}:{0[4]}:{0[5]}.{0[6]}'.format(self.dFormat.refTime))
# 			hWriter.writerow('Clock sample count: {}'.format(self.dFormat.clockSamples[0]))
# 			hWriter.writerow('Sample ticks per second: {}'.format(self.dFormat.timeSampleRate[0]))
# 			hWriter.writerow('UTC Time: {0[1]}/{0[2]}/{0[0]} at {0[3]}:{0[4]}:{0[5]}.{0[6]}\n'.format(self.dFormat.utcTime))

# 			hWriter.writerow('\nCHANNEL AND SIGNAL PATH CORRECTION')
# 			hWriter.writerow('ADC Scale Factor: {}'.format(self.chCorr.adcScale[0]))
# 			hWriter.writerow('Correction Type (0=LF, 1=IF): {}'.format(self.chCorr.corrType[0]))
# 			hWriter.writerow('Signal Path Delay: {} nsec'.format(self.chCorr.pathDelay[0]*1e9))