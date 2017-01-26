#include <windows.h>	// Sleep(), etc
#include <conio.h>		// _kbhit(), _getch(), _putch()
#include <time.h>		// clock(), etc
#include <math.h>		// sqrt()
#include <stdio.h>
#include <iostream>
#include <string>
#include "C:/Tektronix/RSA_API/include/RSA_API.h"

#define RECORDLENGTH 10000

using namespace RSA_API;
using namespace std;

/*
TODO:
Learn how to use C++
*/

ReturnStatus search_connect(ReturnStatus rs)
{
	//Required variables for every script
	int SNLENGTH = 7;
	int numFound = 0;
	int deviceIDs[10];
	char deviceSerial[100];
	char deviceType[20];
	rs = DEVICE_Search(&numFound, deviceIDs, &deviceSerial, &deviceType);
	rs = DEVICE_Connect(deviceIDs[0]);
	if (rs == noError)
	{
		for (int i = 0; i < numFound; i++)
		{
			printf("Device ID: %d\nDevice Serial Number: ", deviceIDs[i]);
			for (int j = 0; j < SNLENGTH; j++)
			{
				printf("%c", deviceSerial[j]);
				if (j == (SNLENGTH - 1))
					printf("\n");
			}
			printf("Device Type: ");
			for (int k = 0; k < SNLENGTH; k++)
			{
				printf("%c", deviceType[k]);
				if (k == (SNLENGTH - 1))
				{
					printf("\n");
				}
			}
		}
	}
	return rs;
}

int* pulse_width_finder(double* data, float thresh, int startIndex, int recordLength, int* risingIndex, int* fallingIndex)
{
	//find max value in data
	double max = 0;
	for (int i = 0; i < recordLength; i++)
	{
		if (data[i] > max)
			max = data[i];
	}
	double dPoint = max - thresh;
	double saved = data[startIndex];
	int rIndex = startIndex;
	int endIndex = recordLength;
	int fIndex = endIndex - 1;

	for (int j = startIndex; j < endIndex; j++)
	{
		if (data[j] <= dPoint)
			saved = data[j];
		else
		{
			if (saved <= dPoint)
			{
				saved = data[j];
				rIndex = j;
				break;
			}
		}
	}
	for (int k = rIndex; k < endIndex; k++)
	{
		if (data[k] >= dPoint)
			saved = data[k];
		else
		{
			if (saved >= dPoint)
			{
				saved = data[k];
				fIndex = k;
				break;
			}
		}
	}
	*risingIndex = rIndex;
	*fallingIndex = fIndex;
	return 0;
}

int main()
{
	ReturnStatus rs;

	//Setup variables
	char apiVersion[200];
	
	double cf = 1e9;
	double refLevel = 0;
	double iqBandwidth = 40e6;
	double acqTime = 100.0e-6;
	float iData[RECORDLENGTH];
	float qData[RECORDLENGTH];
	/*
	NB: Record length is set below because it depends on the IQ sample rate.
		Consequently, the iqArray data type is set below place for the same reason
	*/

	int actLength = 0;
	TriggerMode trigMode = triggered;
	TriggerSource trigSource = TriggerSourceIFPowerLevel;
	double trigLevel = -10;
	double trigPosition = 10;
	double iqSampleRate = 0.0;
	bool runMode = 0;
	int timeoutMsec = 1000;
	bool ready = 0;


	rs = DEVICE_GetAPIVersion(apiVersion);
	printf("API Version: %s\n", apiVersion);
	
	rs = search_connect(rs);

	CONFIG_Preset();
	CONFIG_SetCenterFreq(cf);
	CONFIG_SetReferenceLevel(refLevel);
	IQBLK_SetIQBandwidth(iqBandwidth);
	IQBLK_GetIQSampleRate(&iqSampleRate);
	int recordLength = iqSampleRate*acqTime;
	IQBLK_SetIQRecordLength(recordLength);
	TRIG_SetTriggerMode(trigMode);
	TRIG_SetIFPowerTriggerLevel(trigLevel);
	TRIG_SetTriggerSource(trigSource);
	TRIG_SetTriggerPositionPercent(trigPosition);
	
	/*ACQUIRE/PROCESS DATA*/
	DEVICE_Run();

	if (trigMode == triggered)
		printf("Waiting for trigger.\n");

	IQBLK_AcquireIQData();
	while (!ready)
		rs = IQBLK_WaitForIQDataReady(timeoutMsec, &ready);
	IQBLK_GetIQDataDeinterleaved(iData, qData, &actLength, recordLength);
	if (actLength != recordLength)
		printf("Requested and actual data length mismatch.\n");
	printf("Got IQ data. Processing pulse widths, please wait.\n");
	DEVICE_Stop();
	
	//Convert from IQ voltage to power in dBm. This is way easier in Python.
	double avt[RECORDLENGTH];
	for (int i = 0; i < recordLength; i++)
	{
		avt[i] = 10 * log10((pow(iData[i], 2.0) + pow(qData[i], 2.0)) / (2 * 50 * 1e-3));
	}

	//create time vector
	double timeVector[RECORDLENGTH];
	for (int j = 0; j < recordLength; j++)
	{
		if (j == 0)
			timeVector[j] = 0;
		else
			timeVector[j] = (timeVector[j - 1] + (recordLength / iqSampleRate));
	}
	//collect all pulse widths and indices
	float thresh = 10;
	int risingIndex, fallingIndex = 0;
	int pwIndex = 0;
	double pulseWidth[20];
	int pwRisingIndices[1024];
	int pwFallingindices[1024];
	
	while (fallingIndex < (recordLength - 1))
	{
		pulse_width_finder(avt, thresh, fallingIndex, recordLength, &risingIndex, &fallingIndex);
		pwRisingIndices[pwIndex] = risingIndex;
		pwFallingindices[pwIndex] = fallingIndex;
		pulseWidth[pwIndex] = timeVector[pwFallingindices[pwIndex]] - timeVector[pwRisingIndices[pwIndex]];
	}
	
	for (int l = 0; l < (sizeof(pulseWidth) / sizeof(*pulseWidth)); l++)
	{
		printf("Pulse %i width: %f\n", l, pulseWidth[l]);
	}

	DEVICE_Disconnect();
	string throwaway;
	getline(cin, throwaway);

	return 0;
}