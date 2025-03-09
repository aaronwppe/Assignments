#include <stdio.h>
#include <unistd.h>
#include <dirent.h>

int main(int argc, char *argv[])
{
	struct dirent *entry;
	char *path;
	DIR *dir;

	if(argc != 2)
	{
		perror("ERROR: Expected 1 argument <dir_path>");
		return 1;
	}

	path = argv[1];

	dir = opendir(path);

	if(!dir)
	{
		perror("ERROR: Directory operation opendir() failed.");
		return 1;
	}

	while((entry = readdir(dir)) != NULL)
			printf("%s\n", entry->d_name);

	closedir(dir);

	return 0;
}
