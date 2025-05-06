#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>


int main(int argc, char *argv[]) 
{
    	int file_fd, i, out_fd;

    	file_fd = open("output.txt", O_WRONLY | O_CREAT | O_APPEND, 0644);
    
	if(file_fd < 0) 
    	{
        	perror("ERROR: open operation failed.");
        	return 1;
    	}
	
	close(STDOUT_FILENO);
	
    	if((out_fd = dup(file_fd)) != STDOUT_FILENO) 
    	{
        	perror("ERROR: dup operation failed.");
        	return 1;
    	}

	close(file_fd);

	for(i = 1; i < argc; i++)
		printf("%s ", argv[i]);
	

	printf("\n");

    	return 0;
}
