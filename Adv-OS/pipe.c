#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

int main(int argc, char* argv[])
{
	int fd[2];
	char *message, buffer[20];
	pid_t pid;
	ssize_t bytes;

	if(argc != 2)
	{
		perror("ERROR: Expected 1 argument <message>");
		return -1;
	}

	message = argv[1];
	
	if(pipe(fd) == - 1)
	{
		perror("ERROR: pipe() operation failed.");
		return -1;
	}

	pid = fork();

	if(pid == -1)
	{
		perror("ERROR: fork() operation failed.");
		return -1;
	}

	if(pid == 0)
	{
		close(fd[0]);

		write(fd[1], message, strlen(message));
		close(fd[1]);
	}
	else
	{
		close(fd[1]);
		
		printf("Message received: ");

		while((bytes = read(fd[0], buffer, sizeof(buffer) - 1)) > 0)
		{
			buffer[bytes] = '\0';
			printf("%s", buffer);
		}
		
		printf("\nEOF\n");
		close(fd[0]);
	}

	return 0;
}
