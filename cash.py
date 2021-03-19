import sys

class CashCase():

    def get_change(self, change_to_return, coins):
        '''
        :param change_to_return: the desired change
        :param coins: (pennies, nickels, dimes, quarters), ej. [0.01, 0.05, 0.10, 0.25]
        :return: Returns a nested list with the currency exchange
        '''
        flag = None
        for c in coins:
            if c == change_to_return:
                return c
            if c < change_to_return:
                flag = c
        temp_balance = round(change_to_return - flag, 2)
        return [flag] + [self.get_change(temp_balance,coins)]

    def get_coins(self, list_coins):
        """
        :param list_coins: Nested list of coins, ej. [0.25, [0.1, [0.05, 0.01]]]
        :return: Returns the minimum number of coins possible , ej. 4.
        """
        count = 0
        if isinstance(list_coins, list):
            for l in list_coins:
                count += self.get_coins(l)
        else:
            count += 1
        return count

    def get_user_output(self):
        '''
        :return: Returns the user input, ej. 0.41
        '''
        boolean = True
        while (boolean):
            try:
                x = float(input("Change owed: "))
                if x > 0:
                    boolean = False
            except ValueError:
                pass
        return x


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    cc= CashCase()
    x = cc.get_user_output()
    result = cc.get_change(x, [0.01, 0.05, 0.10, 0.25])
    print(cc.get_coins(result))