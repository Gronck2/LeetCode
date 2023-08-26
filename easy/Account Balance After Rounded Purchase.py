class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        main_part = purchaseAmount // 10 + (1 if purchaseAmount % 10 >= 5 else 0)
        return 100 - main_part * 10
