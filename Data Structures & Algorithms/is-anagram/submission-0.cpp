class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
        {
            return false;
        }
        unordered_map<char,int>s2;
        unordered_map<char,int>t2;

        for(int i=0;i<s.length();++i)
        {
            s2[s[i]]++;
            t2[t[i]]++;
        }
        return s2==t2;
    }
};
