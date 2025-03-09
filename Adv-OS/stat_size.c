#include <stdio.h>
#include <sys/stat.h>

long get_file_size(char *fpath)
{
	struct stat file_status;

	if(stat(fpath, &file_status) < 0)
		return -1;

	return file_status.st_size;
}

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		perror("ERROR: Expected 1 argument <file_path>");
		return 1;
	}

	char *fpath = argv[1];

	long size = get_file_size(fpath);

	if(size == -1)
	{
		perror("ERROR: stat call failed!");
		return 1;
	}

	printf("File Path: %s\t", fpath);
	printf("File Size: %ld\n", size);

	return 0;
}
