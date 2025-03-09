#include <stdio.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>

int main(int argc, char *argv[])
{
	struct dirent *entry;
	char *path, *fname;
	DIR *dir;

	if(argc != 3)
	{
		perror("ERROR: Expected 2 arguments <directory_path> <file_name>.");
		return 1;
	}

	path = argv[1];
	fname = argv[2];

	dir = opendir(path);

	if(!dir)
	{
		perror("ERROR: Directory operation opendir() failed.");
		return 1;
	}
	
	int flag = 0;

	while((entry = readdir(dir)) != NULL)
	{
		if(strcmp(fname, entry->d_name) == 0)
		{
			flag = 1;
			break;
		}
	}

	closedir(dir);

	if(flag == 1)
		printf("File found.\n");
	else
		printf("File not found.\n");

	return 0;
}
