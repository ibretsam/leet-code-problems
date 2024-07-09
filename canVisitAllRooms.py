def canVisitAllRooms(rooms):
    visited = {}
    def dfs(room):
        if room == []: return
        for key in room:
            if key not in visited:
                visited[key] = True
                dfs(rooms[key])

    visited[0] = True
    dfs(rooms[0])
    return len(visited) == len(rooms)
    
    
    # visited = [False] * len(rooms)

    # def dfs(room):
    #     visited[room] = True
    #     for key in rooms[room]:
    #         if not visited[key]:
    #             dfs(key)

    # dfs(0)
    # return all(visited)


print(canVisitAllRooms([[1], [2], [3], []]))  # Should return True
print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))  # Should return False
print(canVisitAllRooms([[1], [2], [], [3]]))  # Should return False
