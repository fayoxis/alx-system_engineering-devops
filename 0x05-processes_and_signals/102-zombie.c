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
int i;
pid_t zombie;

for (i = 0; i < 5; i++)
{
zombie = fork();
while (!zombie)
return (0);
printf("Zombie process created, PID: %d\n", zombie);
}
infinite_while();
return (0);
}
