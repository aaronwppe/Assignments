#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#define MAX_BUF_SIZE 2048

void copy(int source_fd, int dest_fd)
{
	int count;
	char buffer[MAX_BUF_SIZE];

	while((count = read(source_fd, buffer, sizeof(buffer))) > 0)
		write(dest_fd, buffer, count);
}

int main(int argc, char *argv[])
{
	int source_fd, dest_fd;

	if (argc != 3) 
	{
		perror("ERROR: Expected 2 arguments <source_path> <dest_path>");
		return 1;
	}

	source_fd = open(argv[1], O_RDONLY);

	if(source_fd == -1)
	{
			perror("ERROR: File operation open() failed.");
			return 1;
	}

	dest_fd = creat(argv[2], 0666);

	if(dest_fd == -1)
	{
		perror("ERROR: File operation creat() failed.");
		return 1;
	}

	copy(source_fd, dest_fd);

	return 0;
}
