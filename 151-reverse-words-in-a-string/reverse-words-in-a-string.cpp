class Solution {
public:
    string reverseWords(string s) {
        int left = 0, right = 0;
        int sz = s.size();

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') continue;

            while (i < sz && s[i] != ' ') {
                s[right++] = s[i++]; 
            }

            reverse(s.begin() + left, s.begin() + right);
            s[right++] = ' ';
            left = right;
        }

        for (int count = 0; count <= sz - right; count++) {
            s.pop_back();
        }

        reverse(s.begin(), s.end());
        return s;
    }
};