"""
    Another Brick in the Wall :)

    john: 1 2 3...
    jack: 2 4 6...

    total: 12 + 1 -> 13
           jack: 1

    total bricks: 13

"""

# total_bricks = int(input("Enter the total number of bricks :"))
# bricks_in_wall=0
#
# for idx in range(1 , total_bricks):
#     john_bricks = idx
#     bricks_in_wall = bricks_in_wall + john_bricks
#
#     if bricks_in_wall >= total_bricks:
#         difference = bricks_in_wall - total_bricks
#         print("John placed the last bricks: " , john_bricks - difference)
#         break
#
#     jack_bricks = idx *2
#     bricks_in_wall= bricks_in_wall+ jack_bricks
#     if bricks_in_wall >= total_bricks:
#         difference = bricks_in_wall - total_bricks
#         print("Jack placed the last bricks: ", jack_bricks - difference)
#         break
# print("bricks in wall is : " , bricks_in_wall - difference)
#
#


total_bricks= int(input("Enter the number of total bricks :"))
bricks_in_wall=0
idx=0
while (idx<total_bricks):
    jack_bricks=idx
    bricks_in_wall=bricks_in_wall+jack_bricks
    if bricks_in_wall>=total_bricks:
        difference=bricks_in_wall-total_bricks
        print("jack placed the last bricks :",jack_bricks-difference)
        break
    john_bricks=idx*2
    bricks_in_wall=bricks_in_wall+john_bricks
    if bricks_in_wall>=total_bricks:
        difference=bricks_in_wall-total_bricks
        print("john place the last bricks :", john_bricks-difference)
        break

    idx=idx+1
print("total bricks in wall is : " ,bricks_in_wall-difference)
