class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        keys_list = [0]
        keys_list.extend(rooms[0])
        for key in keys_list:
            for room_key in rooms[key]:
                if room_key not in keys_list:
                    keys_list.append(room_key)
        if len(keys_list) >= len(rooms):
            return True
        return False


sol = Solution()
print(sol.canVisitAllRooms([[1], [2], [3], []]))
