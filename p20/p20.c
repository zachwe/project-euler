#include <stdio.h>

void multiply(int ar[], int num, int len) {
    int carry = 0;
    for(int i = 0; i < len; i++) {
        int prod = ar[i] * num + carry;
        int digit = prod % 10;
        carry = prod / 10;
        ar[i] = digit;
    }
}

main() {
    int answer[1000];
    int len = sizeof(answer) / sizeof(answer[0]);
    for(int i = 0; i < len; i++) {
        if(i == 0) {
            answer[i] = 1;
        } else {
            answer[i] = 0;
        }
    }
    for(int i = 1; i <= 100; i++) {
        multiply(answer, i, len);
    }
    for(int i = len - 1; i >= 0; i--) {
        printf("%d", answer[i]);
    }
    printf("\n");
    int sum = 0;
    for(int i = 0; i < len; i++) {
        sum += answer[i];
    }
    printf("%d\n", sum);
}

