#include <stdio.h>
#include <string.h>

void safeCopy(char *src) {
    char buffer[10];
    // Эта строка безопасна, так как используется ограниченное копирование
    strncpy(buffer, src, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';
    printf("Buffer: %s\n", buffer);
}

int main() {
    char *input = "safe";
    safeCopy(input);
    return 0;
}
