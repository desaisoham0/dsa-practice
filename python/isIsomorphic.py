class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Isomorphism is impossible if lengths differ.
        if len(s) != len(t):
            return False
        
        # map_s_t checks: Have we mapped this character from 's' before?
        # map_t_s checks: Has this character from 't' already been used?
        map_s_t = {}
        map_t_s = {}

        # zip() for parallel iteration
        for char_s, char_t in zip(s, t):
            # Case A: We have seen 'char_s' before.
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            
            # Case B: We have not seen 'char_s' but 'char_t' is already taken.
            elif char_t in map_t_s:
                return False
            
            # Case c: Completely new pair.
            else:
                map_s_t[char_s] = char_t
                map_t_s[char_t] = char_s
        
        return True