#include <stdio.h>
// 2^1000 < (2^3)^334 < 10^334
#define MAXLEN 334
#define POW 1000

void printar(int len, int digits[]) {
    for(int i = 0; i < len; i++) {
        printf("%d ", digits[i]);
    }
    printf("\n");
}

int main() {
    int carry, newval, len;
    int digits[MAXLEN];
    
    digits[0] = 1;
    len = 1;
    printf("hi\n");
    for(int i = 0; i < POW; i++) {
        carry = 0;
        int tmplen = len;
        for(int j = 0; j < tmplen; j++) {
            int tmp = digits[j] * 2;
            newval = tmp % 10 + carry;
            carry = tmp / 10;
            digits[j] = newval;
            if(carry == 1 && j  == tmplen - 1) {
                // new place
                len++;
                digits[j + 1] = carry;

            }
        }
        printar(len, digits);
    }
    printf("hi\n");
    
    int sum = 0;
    for(int i = 0; i < len; i++) {
        sum += digits[i];
    }
    printf("sum: %d\n", sum);
}
