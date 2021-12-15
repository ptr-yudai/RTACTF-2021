/* gcc main.c -o chall -no-pie -fno-stack-protector */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
  /* Call me :pleading_face: */
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

void readn(char *ptr, int size) {
  /* Read data up to `size` bytes into `ptr` */
  for (int i = 0; i != size; i++, ptr++) {
    read(0, ptr, 1);
    if (*ptr == '\n') break;
  }
  *ptr = '\0'; // terminate by null
}

int main() {
  char title[0x18];
  char *content = alloca(0x80);

  /* Input title */
  printf("title: ");
  readn(title, 0x18);

  /* Input content */
  printf("data: ");
  readn(content, 0x80);

  return 0;
}

__attribute__((constructor))
void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
}
