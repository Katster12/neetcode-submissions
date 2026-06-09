class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        '''a dictionary to make sure that we 
        count correctly and if the count is 0 then we well not 
        have any further problems'''
        for s in strs: 
            '''making a loop where we will
        further make an array which will have the count of each
        character and then we will basically see which
        no. have same amt'''
            count =[0]*26 #a...z 26 unique chara
            for c in s:
                count[ord(c)-ord("a")]+=1 #let a=80, then b-a=1 it will get mapped

            res[tuple(count)].append(s)
        return list(res.values())
        

        