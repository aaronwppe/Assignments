#include <stdio.h>
#include <sys/stat.h>

#define PERMISSIONS_SIZE 9

char get_file_type(mode_t mode)
{
	switch(mode & S_IFMT)	// Status Inode File Mode Type
	{
		// Regular
		case S_IFREG:	
			return '-';

		// Directory
		case S_IFDIR:
			return 'd';

		// Symbolic link
		case S_IFLNK:
			return 'l';

		// Character device
		case S_IFCHR:
			return 'c';

		// Block device
		case S_IFBLK:
			return 'b';

		// FIFO named pipe
		case S_IFIFO:
			return 'p';

		// Socket
		case S_IFSOCK:
			return 's';

		default:
			return ' ';
		
	}
}

void get_file_permissions(mode_t mode, char ret[PERMISSIONS_SIZE])
{
	mode_t bit_masks[PERMISSIONS_SIZE] = {
		S_IRUSR, S_IWUSR, S_IXUSR,
		S_IRGRP, S_IWGRP, S_IXGRP,
		S_IROTH, S_IWOTH, S_IXOTH
	};

	char permissions[3] = {'r', 'w', 'x'};

	for (int i = 0; i < PERMISSIONS_SIZE; i++)
	{
		if(mode & bit_masks[i])
			ret[i] = permissions[i % 3];
		else
			ret[i] = '-';
	}
}

int main(int argc, char *argv[])
{
	if(argc != 2)
	{
		perror("ERROR: Expected 1 argument <file_path>");
		return 1;
	}

	char *file_path = argv[1];

	struct stat file_status;

	if(stat(file_path, &file_status) == -1) 
	{
		perror("ERROR: stat() call failed!");
		return 1;
	}

	char permissions[PERMISSIONS_SIZE] = {' '};

	get_file_permissions(file_status.st_mode, permissions);

	printf("%c\t", get_file_type(file_status.st_mode));
	printf("%s\t", permissions);
	printf("%s\n", file_path);

	return 0;
}
