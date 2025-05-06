#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>


void handle_sigchld(int sig) 
{
    pid_t pid = wait(NULL);
    printf("Child process %d terminated.\n", pid);
    exit(0);
}


void handle_sigalrm(int sig) 
{
	printf("Child: Exiting.\n");
    	exit(0);
}

int main() 
{
    	pid_t pid = fork();

    	if(pid < 0) 
    	{
        	perror("ERROR: fork operation failed.\n");
        	exit(EXIT_FAILURE);
    	}

    	if(pid == 0) 
    	{
        	signal(SIGALRM, handle_sigalrm);

        	printf("Child: Sleeping for 5 seconds.\n");
        	alarm(5);  

        	while(1) 
            		pause(); 
        
    	} 
	else 
	{
        	signal(SIGCHLD, handle_sigchld);
		printf("Parent: Waiting for child to terminate...\n");
        	
		while(1)
            		pause();
		
    	}

    	return 0;
}
