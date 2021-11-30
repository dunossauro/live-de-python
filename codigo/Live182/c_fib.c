#include "c_fib.h"

unsigned long long c_fib(int n) {
    int i;
    unsigned long long a=0.0, b=1.0, tmp;
    for (i=0; i<n; ++i) {
        tmp = a; a = a + b; b = tmp;
    }
    return a;
}
