class Solution {
public:
    int maximumXorProduct(long long a, long long b, int n) {
        long long MOD = 1e9 + 7;
        long long num1 = a >> n;
        long long num2 = b >> n;

        for (int i = n - 1; i >= 0; i--) {
            long long bitA = a & (1LL << i);
            long long bitB = b & (1LL << i);

            if (bitA == bitB) {
                num1 = (num1 << 1) | 1;
                num2 = (num2 << 1) | 1;
            }
            else {
                if (num1 > num2) {
                    num2 = (num2 << 1) | 1;
                    num1 = (num1 << 1);
                }
                else {
                    num1 = (num1 << 1) | 1;
                    num2 = (num2 << 1);
                }
            }
        }

        return ((__int128)num1 * num2) % MOD;
    }
};