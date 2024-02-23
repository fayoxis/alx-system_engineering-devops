#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - used when done creating the parent process and the,
 * zombies.
 *
 * Return: always 0
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - this is main entry point for program
 * Description - definitely creates five zombie processes.
 *
 * Return: returns always 0
 */
int main(void)
{
int i, pid;

for (i = 0; i < 5; i++)
{
pid = fork();

if (pid == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
return (0);
}
else if (pid > 0)
{
while (pid != wait(NULL))
;
}
else
{
perror("fork error");
exit(1);
}
}
infinite_while();
return (0);
}
