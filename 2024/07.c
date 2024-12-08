#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    long val, nn, *num;
} Equation;

typedef long Operation(long, long);

char *read_file(const char *fname);
long strcnt(const char *s, int c);
Equation *create_equations(long ne, char *input);
void free_equations(long ne, Equation eqs[ne]);
long compute(long no, long ne, Operation *op[no], Equation eqs[ne]);
long lpow(long a, long b);
Operation add, mul, cat;

int main(void)
{
    // read equations
    char *input = read_file("input/07.txt");
    const long ne = strcnt(input, '\n');
    Equation *eqs = create_equations(ne, input);

    // part one
    printf("%ld\n", compute(2, ne, (Operation *[]){add, mul}, eqs));

    // part two
    printf("%ld\n", compute(3, ne, (Operation *[]){add, mul, cat}, eqs));

    // cleanup
    free_equations(ne, eqs);
    free(input);
}

char *read_file(const char *fname)
{
    FILE *file = fopen(fname, "r");
    char *buffer = 0;
    long n = 0;
    int c;
    while ((c = fgetc(file)) != EOF) {
        buffer = realloc(buffer, ++n * sizeof(*buffer));
        buffer[n - 1] = c;
    }
    buffer = realloc(buffer, ++n * sizeof(*buffer));
    buffer[n - 1] = 0;
    fclose(file);
    return buffer;
}

long strcnt(const char *s, int c)
{
    long count = 0;
    while (*s) count += (*s++ == c);
    return count;
}

Equation *create_equations(long ne, char *input)
{
    Equation *eqs = calloc(ne, sizeof(*eqs));
    char *token = strtok(input, " \n");
    Equation *eq = eqs - 1;
    while (token) {
        if (token[strlen(token) - 1] == ':') {
            (++eq)->val = strtol(token, 0, 10);
        }
        else {
            eq->num = realloc(eq->num, ++eq->nn * sizeof(*eq->num));
            eq->num[eq->nn - 1] = strtol(token, 0, 10);
        }
        token = strtok(0, " \n");
    }
    return eqs;
}

void free_equations(long ne, Equation eqs[ne])
{
    for (Equation *eq = eqs; eq < eqs + ne; ++eq) free(eq->num);
    free(eqs);
}

long compute(long no, long ne, Operation *op[no], Equation eqs[ne])
{
    long tot = 0;
    for (Equation *eq = eqs; eq < eqs + ne; ++eq) {
        const long repeat = eq->nn - 1;
        const long nc = lpow(no, repeat);
        for (long c = 0; c < nc; ++c) {
            long res = eq->num[0];
            for (long i = 0, tc = c; i < repeat; ++i, tc /= no)
                res = op[tc % no](res, eq->num[i + 1]);
            if (res == eq->val) {
                tot += res;
                break;
            }
        }
    }
    return tot;
}

long lpow(long a, long b)
{
    long res = 1;
    for (long i = 0; i < b; ++i) res *= a;
    return res;
}

long add(long a, long b)
{
    return a + b;
}

long mul(long a, long b)
{
    return a * b;
}

long cat(long a, long b)
{
    char tmp[128];
    sprintf(tmp, "%ld%ld", a, b);
    return strtol(tmp, 0, 10);
}
