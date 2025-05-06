#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>

#define BUFFER_SIZE 1 


int main(int argc, char *argv[])
{
	int fd, line_count = 0, line_max = 0;
	size_t d_buffer_size = 0;
	char buffer[BUFFER_SIZE], *line, *file_path, *str_ptr, *d_buffer = NULL;
	ssize_t bytes;

	file_path = argv[1];
	line_max = atoi(argv[2]);

	fd = open(file_path, O_RDONLY);
	
	if(fd == -1)
	{
		fprintf(stderr, "ERROR: Failed to open file '%s'\n", file_path);
		exit(EXIT_FAILURE);
	}

	while((bytes = read(fd, buffer, sizeof(buffer))) > 0)
	{	
		d_buffer = realloc(d_buffer, d_buffer_size + sizeof(buffer) + 1);
		if(d_buffer == NULL)
		{
			fprintf(stderr, "ERROR: Failed realloc operation. - 1");
			exit(EXIT_FAILURE);
		}
		
		memcpy(d_buffer + d_buffer_size, buffer, bytes);
		d_buffer_size += bytes;
		d_buffer[d_buffer_size] = '\0';

		str_ptr = d_buffer;

		while((line = strchr(str_ptr, '\n')) != NULL && (line_max == 0 || line_count < line_max))
		{
			*line = '\0';
			printf("%d: %s\n", line_count, str_ptr);
			line_count++;
			str_ptr = line + 1;
		}

		if(line_max != 0 && line_count == line_max)
			break;

		d_buffer_size = strlen(str_ptr);
		memmove(d_buffer, str_ptr, d_buffer_size + 1);
		
		d_buffer = realloc(d_buffer, d_buffer_size + 1);
		if(d_buffer == NULL)
		{
			fprintf(stderr, "ERROR: Failed realloc operation.%d\n", d_buffer_size);
			exit(EXIT_FAILURE);
		}
	}

	if(bytes < 0)
	{
		fprintf(stderr, "ERROR: Failed to read file '%s'\n", file_path);
		exit(EXIT_FAILURE);
	}
	
	if(close(fd) == -1)
	{
		fprintf(stderr, "ERROR: Failed to close file '%s'\n", file_path);		
		exit(EXIT_FAILURE);
	}

	return 0;
}
