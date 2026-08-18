class Solution {
public:
    int maximumXorProduct(long long a, long long b, int n) {
        long long MOD = 1e9 + 7;

        for (int i = n - 1; i >= 0; i--) {
            long long bit = (1LL << i);

            long long firstNum = a ^ bit;
            long long secondNum = b ^ bit;

            __int128 firstProd = (__int128)firstNum * secondNum;
            __int128 secondProd = (__int128)a * b;

            if (firstProd > secondProd) {
                a ^= bit;
                b ^= bit;
            }
        }

        return ((__int128)a * b) % MOD;
    }
};