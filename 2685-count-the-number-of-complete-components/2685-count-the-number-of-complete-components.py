class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dictionary_list = {}
        count = 0
        for edge in edges:
            if edge[0] in dictionary_list:
                if edge[1] not in dictionary_list[edge[0]]:
                    dictionary_list[edge[0]].append(edge[1])
            else: 
                dictionary_list[edge[0]] = [edge[1]]
            
            if edge[1] in dictionary_list:
                if edge[0] not in dictionary_list[edge[1]]:
                    dictionary_list[edge[1]].append(edge[0])
            else: 
                dictionary_list[edge[1]] = [edge[0]]
        
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            else:
                current_island = [i]
                component = []
                while current_island:
                    val = current_island.pop()
                    if val not in visited:
                        visited.add(val)
                        component.append(val)
                        neighbors = dictionary_list.get(val, [])
                        for neighbor in neighbors:
                            if neighbor not in visited:
                                current_island.append(neighbor)
            # component check
            current_len = len(component)
            flag = 0
            for j in component:
                if len(dictionary_list.get(j, [])) != current_len - 1:
                    flag += 1
            
            if flag == 0:
                count += 1

        return count