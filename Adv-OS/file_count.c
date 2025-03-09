#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <errno.h>

mode_t get_file_type(char *path)
{
	struct stat file_status;

	if(stat(path, &file_status) == -1)
		return -1;

	return file_status.st_mode & S_IFMT;
}

int get_file_count(char *dir_path, mode_t file_type)
{
	struct dirent *entry;
    	DIR *dir = opendir(dir_path);

    	if (!dir) 
		return -1;
	
	int file_count = 0;

    	while ((entry = readdir(dir)) != NULL) 
	{
        	if (entry->d_name[0] == '.')  
			continue;

		if(get_file_type(entry->d_name) == file_type)		
			file_count++;
	}

    	closedir(dir);
    	return file_count;
}

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		perror("ERROR: Expected 1 argument <dir_path>");
		return 1;
	}

	char *dir_path = argv[1];
	
	if(get_file_type(dir_path) != S_IFDIR)
	{
		fprintf(stderr, "ERROR: '%s' is not a directory.\n", dir_path);
		return 1;
	}

	int count = get_file_count(dir_path, S_IFREG);

	if(count == -1)
	{
		perror("ERROR: Directory operation get_file_count() failed.");
		return 1;
	}

	printf("Regular File Count: %d\n", count);

	return 0;
}
