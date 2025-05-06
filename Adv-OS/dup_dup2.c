#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>


int main(int argc, char *argv[]) 
{
    	int file_fd, old_out;

    	file_fd = open("namedtemp.txt", O_WRONLY | O_CREAT | O_APPEND, 0644);
    
	if(file_fd < 0) 
    	{
        	perror("ERROR: open operation failed.");
        	return 1;
    	}

	printf("Redirecting STDOUT.\n");

	old_out = dup(STDOUT_FILENO);
	close(STDOUT_FILENO);
	
    	dup2(file_fd, STDOUT_FILENO);
	close(file_fd);

	printf("M. Sc. Computer Science.\n");
	printf("Semester - II Class.\n");
	printf("Advanced Operating Systems\n");
	printf("Practical Examination\n");
	
	close(STDOUT_FILENO);
	dup2(old_out, STDOUT_FILENO); 
	close(old_out);

	printf("Reset STDOUT.\n");

    	return 0;
}
