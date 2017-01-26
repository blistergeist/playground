#include <iostream>
#include <stdio.h>
#include <visa.h>
#include <string>

using namespace std;

#define BUFFER 1024
#define HEADERLENGTH 1024
#define SWLENGTH 128
#define TIMEOUT 5000	//milliseconds

/*
I wrote these two wrapper functions so that you don't have to
mess around with send and return count every time you read or write
*/
int inst_write(ViSession target_instr, char* arg)
{
	ViStatus visa_status;
	ViUInt32 commandbytes = strlen(arg);
	ViUInt32 returnbytes;
	visa_status = viWrite(target_instr, (ViBuf) arg, commandbytes, &returnbytes);
	return 0;
}

unsigned char* inst_read(ViSession target_instr, unsigned char* read_buffer)
{
	ViStatus visa_status;
	ViUInt32 readbytes = BUFFER;
	ViUInt32 actualreadbytes;
	visa_status = viRead(target_instr, (ViPBuf) read_buffer, readbytes, &actualreadbytes);
	return read_buffer;
}

int number_size(int number)
{
	//This function determines how many digits are in a given number
	int numdigits = 0;
	if (number < 10)
	{
		numdigits = 1;
	}
	else if (number < 100)
	{
		numdigits = 2;
	}
	else if (number < 1000)
	{
		numdigits = 3;
	}
	else if (number < 10000)
	{
		numdigits = 4;
	}
	else if (number < 100000)
	{
		numdigits = 5;
	}
	else if (number < 1000000)
	{
		numdigits = 6;
	}
	else
	{
		printf("Your number is longer than I was prepared to handle, and I went up to a million so I think that's good enough.\n");
	}
	return numdigits;
}

char* get_binblock_header(int binblocksize)
{
	//This function creates the IEE 488 binblock header based on 
	//the size (in bytes) of the binary data to be sent to the RSA
	static char header[HEADERLENGTH];
	int numdigits, numnumdigits, stringsize;
	numdigits = number_size(binblocksize);
	numnumdigits = number_size(numdigits);
	//Allocate string size, the + 2 is for the # character and NULL string terminator
	stringsize = numnumdigits + numdigits + 2;
	//create the number portion of the header using number theory
	int header_number = numdigits * pow(10,numdigits) + binblocksize;
	sprintf_s(header, stringsize, "#%d", header_number);
	//optional sanity checks
	/*
	printf("Digits: %d\nNumdigits: %d\n", binblocksize, numdigits);
	printf("%s\n", header);
	*/
	return header;
}

int main()
{
	//Initialize required communication variables
	ViStatus visa_status;
	ViSession resource_mgr = VI_NULL;
	ViSession target_instr = VI_NULL;
	ViUInt32 actual_bytes;
	char* write_buffer = NULL;
	unsigned char read_buffer[BUFFER];
	char* arg_address = "GPIB8::1::INSTR";
	visa_status = viOpenDefaultRM(&resource_mgr);
	printf("Opened resource_mgr.\n");
	visa_status = viOpen(resource_mgr, arg_address, VI_NULL, TIMEOUT, &target_instr);
	printf("Opened RSA.\n");

	//VISA Status experimentation
	/*
	viStatusDesc(target_instr, visa_status, write_buffer);
	printf("%d, %s\n", visa_status, write_buffer);
	*/

	//This is how you would read/write without the wrapper functions I wrote
	/*
	write_buffer = "*RST\n";
	ViUInt32 commandbytes = strlen(write_buffer);
	visa_status = viWrite(target_instr, (ViBuf)write_buffer, commandbytes, &actual_bytes);

	write_buffer = "*IDN?\n";
	commandbytes = strlen(write_buffer);
	visa_status = viWrite(target_instr, (ViBuf)write_buffer, commandbytes, &actual_bytes);

	commandbytes = BUFFER;
	visa_status = viRead(target_instr, (ViPBuf) read_buffer, commandbytes, &actual_bytes);
	*/

	//This is how you read/write with the wrapper functions
	inst_write(target_instr, "*RST\n");
	inst_write(target_instr, "*IDN?\n");
	inst_read(target_instr, read_buffer);
	printf("Connected to %s\n", read_buffer);

	//Configure cf/span, open displays, set up mod type, and turn on synch word
	inst_write(target_instr, "spectrum:frequency:center 1.5e9\n");
	inst_write(target_instr, "spectrum:frequency:span 40e6\n");
	inst_write(target_instr, "display:ddemod:measview:new stable\n");
	inst_write(target_instr, "display:ddemod:measview:new conste\n");
	inst_write(target_instr, "sense:ddemod:modulation:type qpsk\n");
	inst_write(target_instr, "sense:ddemod:synch:word on\n");

	//turn off automatic VISA termination character so we can send a single message in multiple writes
	visa_status = viSetAttribute(target_instr, VI_ATTR_SEND_END_EN, VI_FALSE);
	
	//build synch_word array manually (0x16 = 22) 00 01 01 10
	ViUInt32 synch_word[16] = { 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2 };
/*	ViUInt32 synch_word[SWLENGTH];
	for (int i = 0; i < SWLENGTH; i++)
	{
		synch_word[i] = i;
	}*/
	//Find size of data to be sent and determine the header from that value
	int synch_word_size = sizeof(synch_word);
	char* header = get_binblock_header(synch_word_size);

	//Send the synch word using 3 writes, 1 for the command, 1 for the header, and 1 for the data
	inst_write(target_instr, "sense:ddemod:synch:word:symbol ");
	inst_write(target_instr, header);
	//Turn automatic termination character back on and send synch word
	visa_status = viSetAttribute(target_instr, VI_ATTR_SEND_END_EN, VI_TRUE);
	viWrite(target_instr, (ViBuf) synch_word, (ViUInt32) synch_word_size, &actual_bytes);

	//Gracefully disconnect
	viClose(target_instr);
	viClose(resource_mgr);
	
	printf("Done.\n");

	//this just stops the program from exiting before we have the chance to see the readout
	string throwaway;
	getline(cin, throwaway);

	return 0;
}