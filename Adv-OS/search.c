#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <linux/limits.h>
#include <string.h>

#define MAX_LINES 100

int main(int argc, char *argv[]) 
{
	if(argc != 3)
	{
		perror("ERROR: Expected 2 arguments <dir_path> <file_name>");
		return 1;
	}
	
	char *dir_path = argv[1], *file_name = argv[2];

    	int pipe_fd[2];  
	pid_t pid;
    	char buffer[NAME_MAX];
    	char *output[MAX_LINES];
    	int line_count = 0;

    	if (pipe(pipe_fd) == -1) 
    	{
        	perror("ERROR: Pipe operation pipe() failed.");
        	return 1;
    	}

    	pid = fork();

   	if (pid < 0) 
    	{	
        	perror("ERROR: Process operation fork() failed.");
        	return 1;
    	}

    	if (pid == 0) 
    	{  
        	close(pipe_fd[0]);
        	dup2(pipe_fd[1], STDOUT_FILENO);
        	dup2(pipe_fd[1], STDERR_FILENO);
        	close(pipe_fd[1]);

        	execl("./dir_contents.out", "./dir_contents.out", dir_path, NULL);

        	perror("ERROR: Process operation exec() failed.");
        	return 1;
    	} 
    
    	close(pipe_fd[1]);

    	FILE *fp = fdopen(pipe_fd[0], "r");

    	while (fgets(buffer, sizeof(buffer), fp) != NULL && line_count < MAX_LINES) 
	{
		buffer[strlen(buffer) - 1] = '\0'; 
    		output[line_count] = strdup(buffer);
        	line_count++;
    	}

    	fclose(fp);
    	wait(NULL);
	close(pipe_fd[0]);
			
    	int flag = 0;
   
  	for (int i = 0; i < line_count; i++)
       	{
    		if(strcmp(file_name, output[i]) == 0)
    		{
			flag = 1;
			free(output[i]);
			break;
		}
	
        	free(output[i]);
    	}

    	if(flag == 1)
		printf("File '%s' found in directory '%s'.\n", file_name, dir_path);
    	else
	    	printf("File '%s' not found in directory '%s'.\n", file_name, dir_path);

    	return 0;
}
