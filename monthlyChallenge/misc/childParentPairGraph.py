# based on https://leetcode.com/discuss/interview-question/786821/indeed-oa-2020-parents-and-children-graph?fbclid=IwAR0m27Yy5iW_kbZUbgLLPh5OdSTdFYmAOdMSCi2EdRZMVs_wnAjr8upncJI
# given parent_child pairs, find all child with zero or one parent


parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),(4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

dic = {}
for pair in parent_child_pairs:
    if pair[0] not in dic:
        dic[pair[0]] = []
    
    if pair[1] not in dic:
        dic[pair[1]] = [pair[0]]
    else:
        dic.get(pair[1]).append(pair[0])
        
print(dic)
single_p = []
zero_p = []

for key in dic:
    if len(dic[key]) == 0:
        zero_p.append(key)
    if len(dic[key]) == 1:
        single_p.append(key)

print("zero parent: ", zero_p)
print("single parent: ", single_p)
        
        
