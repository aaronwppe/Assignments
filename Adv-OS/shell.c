#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define BUFFER_SIZE 100

int main()
{
	int i;
	char input[BUFFER_SIZE], *delims=" \n", *args[20];

	while(1)
	{
		printf("shell> ");
		fgets(input, BUFFER_SIZE, stdin);

		i = 0;
		args[i] = strtok(input, delims);

		while(args[i] != NULL && i < 20)
			args[++i] = strtok(NULL, delims);

		args[i] = NULL;

		if(strcmp(args[0], "exit") == 0)
			break;

		if(fork() == 0)
		{
			execvp(args[0], args);
			perror("ERROR: execvp operation failed\n");
			exit(1);
		}
		else
		{
			wait(NULL);
		}
	}
	return 0;
}
