class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reserved_counts = 0
        seats = {}

        for seat in reservedSeats:
            if seat[0] in seats:
                seats[seat[0]].append(seat[1])
            else:
                seats[seat[0]] = [seat[1]]
        
        unreserved_counts = 2*(n - len(seats))

        for seat in seats:

            group_a = False
            group_b = False
            group_c = False

            for seat_num in seats[seat]:
                if seat_num-1 >= 1 and seat_num-1 <= 4:
                    group_a = True
                if seat_num-1 >= 3 and seat_num-1 <= 6:
                    group_b = True
                if seat_num-1 >= 5 and seat_num-1 <= 8:
                    group_c = True
            
            if group_a == False and group_b == False and group_c == False:
                reserved_counts += 2
            elif group_a == False and group_b == False:
                reserved_counts += 1
            elif group_b == False and group_c == False:
                reserved_counts += 1
            elif group_a == False and group_c == False:
                reserved_counts += 2
            elif group_a == False or group_b == False or group_c == False:
                reserved_counts += 1
            
        return reserved_counts+unreserved_counts

        # for row in small_grid:
        #     if row[0] == 0 and row[1] == 0 and row[2] == 0:
        #         count += 2
        #     elif row[0] == 0 and row[1] == 0:
        #         count += 1
        #     elif row[1] == 0 and row[2] == 0:
        #         count += 1
        #     elif row[0] == 0 and row[2] == 0:
        #         count += 2
        #     elif row[0] == 0 or row[1] == 0 or row[2] == 0:
        #         count += 1
