#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int main() 
{
   	sigset_t set;

	sigemptyset(&set);
    	sigaddset(&set, SIGINT);

    	if(sigprocmask(SIG_BLOCK, &set, NULL) < 0)
    	{
        	perror("ERROR: sigprocmask operation failed\n");
        	return 1;
    	}

    	printf("SIGINT is masked.\n");
    
    	printf("Process sleep for 5 seconds.\n");
    	sleep(5);

    	printf("Process wake up.\n");

    	if(sigprocmask(SIG_UNBLOCK, &set, NULL) < 0) 
    	{
        	perror("ERROR: sigprocmask operation failed\n");
        	return 1;
    	}

    	printf("SIGINT is unmasked.\n");    
    	printf("Process pausing.\n'Ctrl+C' to terminate.\n");

	while(1)
		pause();

    	return 0;
}
