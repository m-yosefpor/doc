int main()


// speed up tips
x%2 = x&1 // x%(2^n) = x & 11111..1
x/2 = x<<1 // x/2^n = x<<n
2*x = x>>1 // 2^n * x = x>>n
pow(2,n) = 1<<n
//use #define instead of global const

#define inf 1<<31-1
#define sup 1<<31
bit mask

// tips for ram #but decrease speed
#define swap(a,b) {a^=b;b^=a;a^=b;}


// time a program:

/usr/bin/time ./a.out
