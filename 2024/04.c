#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define min(a, b) (a < b ? a : b)
#define max(a, b) (a > b ? a : b)

char *read_file(const char *fname);
long strcnt(const char *s, int c);
long horizontal(long ni, long nj, const char grid[ni][nj], const char *s);
long vertical(long ni, long nj, const char grid[ni][nj], const char *s);
long diagonal1(long ni, long nj, const char grid[ni][nj], const char *s);
long diagonal2(long ni, long nj, const char grid[ni][nj], const char *s);
long chunks(long ni, long nj, const char grid[ni][nj], const char *s);

int main(void)
{
    // read input grid
    char *input = read_file("input/04.txt");
    const long ni = strcnt(input, '\n');
    const long nj = strchr(input, '\n') - input + 1;
    const char(*grid)[nj] = (void *)input;

    // part one
    long count1 = horizontal(ni, nj, grid, "XMAS") + vertical(ni, nj, grid, "XMAS") +
                  diagonal1(ni, nj, grid, "XMAS") + diagonal2(ni, nj, grid, "XMAS");
    printf("%ld\n", count1);

    // part two
    printf("%ld\n", chunks(ni, nj, grid, "MAS"));

    // cleanup
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

int strcmpfr(const char *grid, const char *s, long o)
{
    const long l = strlen(s);
    int cmpf = 1, cmpr = 1;
    for (long k = 0; k < l; ++k) cmpf &= grid[o * k] == s[k];
    for (long k = 0; k < l; ++k) cmpr &= grid[o * k] == s[l - k - 1];
    return cmpf | cmpr;
}

long horizontal(long ni, long nj, const char grid[ni][nj], const char *s)
{
    const long l = strlen(s);
    long count = 0;
    for (long i = 0; i < ni; ++i)
        for (long j = 0; j < nj - l; ++j) count += strcmpfr(&grid[i][j], s, 1);
    return count;
}

long vertical(long ni, long nj, const char grid[ni][nj], const char *s)
{
    const long l = strlen(s);
    long count = 0;
    for (long i = 0; i < ni - l + 1; ++i)
        for (long j = 0; j < nj - 1; ++j) count += strcmpfr(&grid[i][j], s, nj);
    return count;
}

long diagonal1(long ni, long nj, const char grid[ni][nj], const char *s)
{
    const long l = strlen(s);
    long count = 0;
    const long nd = min(ni, nj - 1);
    for (long d = l - nd; d < nd - l; ++d)
        for (long r = 0; r < nd - labs(d) - l + 1; ++r)
            count += strcmpfr(&grid[r - min(0, d)][r + max(0, d)], s, nj + 1);
    return count;
}

long diagonal2(long ni, long nj, const char grid[ni][nj], const char *s)
{
    const long l = strlen(s);
    long count = 0;
    const long nd = min(ni, nj - 1);
    for (long d = l - nd; d < nd - l; ++d)
        for (long r = 0; r < nd - labs(d) - l + 1; ++r)
            count += strcmpfr(&grid[ni - (r - min(0, d)) - 1][r + max(0, d)], s, -nj + 1);
    return count;
}

long chunks(long ni, long nj, const char grid[ni][nj], const char *s)
{
    const long l = strlen(s);
    long count = 0;
    for (long i = 0; i < ni - l + 1; ++i)
        for (long j = 0; j < nj - l; ++j)
            count += strcmpfr(&grid[i][j], s, nj + 1) & strcmpfr(&grid[i + l - 1][j], s, -nj + 1);
    return count;
}
