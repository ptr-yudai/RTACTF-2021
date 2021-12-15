/* gcc main.c -o chall -no-pie -fno-stack-protector */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
  /* Call me :pleading_face: */
  char *args[] = {"/bin/sh", NULL};
  execve(args[0], args, NULL);
}

void readn(char *ptr, unsigned size) {
  /* Read data up to `size` bytes into `ptr` */
  for (unsigned i = 0; i != size; i++, ptr++) {
    read(0, ptr, 1);
    if (*ptr == '\n') break;
  }
}

int main() {
  unsigned size;
  char buf[0x80];

  /* Input size */
  printf("size: ");
  scanf("%d%*c", &size);
  if (size > 0x80) {
    puts("*** buffer overflow ***");
    return 1;
  }

  /* Input data */
  printf("data: ");
  readn(buf, size-1);

  return 0;
}

__attribute__((constructor))
void setup() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
}
