#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void sigint_handler(int sig) 
{
	static int count = 0;
    	
	count++; 

    	printf("\nSIGINT signal occurred %d time(s).\n", count);
	
	if (count == 6) 
	{
        	printf("\nExiting after 6 SIGINT occurrences.\n");
        	exit(0);
    	}
}


void sigtstp_handler(int sig) 
{
	printf("\nIgnoring signal SIGTSTP.\n");
	return;
}

int main() 
{
	if(signal(SIGINT, sigint_handler) == SIG_ERR) 
	{
        	perror("ERROR: Failed to set SIGINT handler");
        	exit(1);
	}

  
  	if(signal(SIGTSTP, sigtstp_handler) == SIG_ERR) 
	{
        	perror("ERROR: Failed to set SIGTSTP handler");
        	exit(1);
    	}

    	printf("Program running...\n");

        while(1) 
	        sleep(1);
   
    	return 0;
}
