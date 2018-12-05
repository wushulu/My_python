#include<iostream>
#include<stdio.h>
/**
 * Static table used for the table_driven implementation.
 *****************************************************************************/
static const unsigned short crc_table[16] = 
{
    0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7,
    0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef
};

/****************************************************************************
 * Update the crc value with new data.
 *
 * \param crc      The current crc value.
 * \param data     Pointer to a buffer of \a data_len bytes.
 * \param len		Number of bytes in the \a data buffer.
 * \return         The updated crc value.
 *****************************************************************************/
unsigned short CalculateCrc(char *data, unsigned int len)
{
    unsigned int i;
    unsigned short crc = 0;
    
    while(len--)
    {
        i = (crc >> 12) ^ (*data >> 4);
	    crc = crc_table[i & 0x0F] ^ (crc << 4);
	    i = (crc >> 12) ^ (*data >> 0);
	    crc = crc_table[i & 0x0F] ^ (crc << 4);
	    data++;
	} 

    return (crc & 0xFFFF);
}

void dsply_data(uint8_t* buff_data)
{
  int f,s,t,fu;
  buff_data = &buff_data[0];
  f=buff_data[0];
  s=buff_data[1];
  printf("%d,  %d",f,s);


}

int main()
{
   uint8_t data[] ={0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08};
   dsply_data(&data[1]);
   /*
   uint16_t result;
   result=CalculateCrc(data,1);
   printf("%d",result);
   */

}

