#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>


#define FIFO_NAME "/tmp/fifo"

int main(int argc, char* argv[])
{
	pid_t pid;
	ssize_t bytes;
	char buffer[20], *message;
	int fd;

	if(argc != 2)
	{
		perror("ERROR: Expected 1 argument <message>");
		return -1;
	}

	message = argv[1];

	if(mkfifo(FIFO_NAME, 0666) == -1 && errno != EEXIST)
	{
		perror("ERROR: mkfifo() operation failed.");
		return -1;
	}

	pid = fork();

	if(pid < 0) 
	{
		perror("ERROR: fork() operation failed.");
		return -1;
	}

	if(pid == 0)
	{
		fd = open(FIFO_NAME, O_WRONLY);
		if(fd == -1)
		{
			perror("ERROR: open() operation failed.");
			return -1;
		}

		write(fd, message, strlen(message));
		close(fd);
	}
	else
	{
		fd = open(FIFO_NAME, O_RDONLY);
		if(fd == -1)
		{
			perror("ERROR: open() operation failed.");
			return -1;
		}

		printf("Message received: ");

		while((bytes = read(fd, buffer, sizeof(buffer) -1)) > 0)
		{
			buffer[bytes] = '\0';
			printf("%s", buffer);
		}

		printf("\nEOF\n");

		close(fd);
		unlink(FIFO_NAME);
	}

	return 0;
}
