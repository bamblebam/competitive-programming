class Bank:

    def __init__(self, balance: List[int]):
        self.balance=balance
        self.accounts=len(balance)
        
    def account_exists(self,account):
        if 1<=account<=self.accounts:
            return True
        return False
    
    def balance_exists(self,account,balance):
        if self.balance[account-1]>=balance:
            return True
        return False
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.account_exists(account1) and self.account_exists(account2) and self.balance_exists(account1,money):
            self.balance[account1-1]-=money
            self.balance[account2-1]+=money
            return True
        return False
        
    def deposit(self, account: int, money: int) -> bool:
        if self.account_exists(account):
            self.balance[account-1]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.account_exists(account) and self.balance_exists(account,money):
            self.balance[account-1]-=money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)