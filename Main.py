from Utils import init_data
from RandomAllocation import random_allocation
from GreedAllocation import greed_allocation
from GAAllocation import GA_Allocation
import random

if __name__ == '__main__':

    user_list, server_list = init_data()

    random_allocation(user_list, server_list)

    greed_allocation(user_list, server_list)

    GA_Allocation(user_list,server_list)


# print(unable_allocated_users)
# print(random.randint(0, 1))

#
# for user in user_list:
#     print(user.info())
#
# for server in server_list:
#     print(server.info())
# for i in range(4):
