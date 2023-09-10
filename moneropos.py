from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet
from threading import Thread
from time import sleep

class MoneroPoS:
    def __init__(self, host='127.0.0.1', port=28088, foundIncomingTransactionFunction=None, findConfirmedTransactionAutomatically=False):
        self.host = host
        self.port = port
        self.foundIncomingTransactionFunction = foundIncomingTransactionFunction
        self.findConfirmedIncomingTransactionsAutomatically = findConfirmedTransactionAutomatically
        
        self.wallet = Wallet(JSONRPCWallet(host=self.host, port=self.port))
        
        if findConfirmedTransactionAutomatically:
            Thread(
                target=self._loopForConfirmedIncomingTransactions,
            )
            
    def _loopForConfirmedIncomingTransactions(self):
        while True:
            txHistory = self.wallet.incoming()
            
            for tx in txHistory:
                print(tx)
                
            sleep(5)
            continue
            
    def mainWalletAddress(self):
        return {'success': True, 'address': self.wallet.address()}
    
    def generateNewPayment(self, paymentId, usdAmount=None, xmrAmount=None, processingFunction=None, **kwargs):
        self.newAddress = self.wallet.address().with_payment_id(paymentId)
        
        if processingFunction:
            processingFunction(
                newAddress=self.newAddress, 
                usdAmount=usdAmount, 
                xmrAmount=xmrAmount,
                **kwargs,
            )
        
        return {'success': True, 'address': self.newAddress}
    
    def findConfirmedIncomingTransactions(self, paymentId, xmrAmount, integratedAddress=None):
        txHistory = self.wallet.incoming(payment_id=paymentId)

        txList = list(txHistory)

        foundAConfirmedTransaction = bool(txList)
        
        sumAmount = sum(transaction.amount for transaction in txList)
        transactionSumAmountIsCorrect = float(sumAmount) >= float(xmrAmount)
        
        print(sumAmount)
        print(transactionSumAmountIsCorrect)
        
        return {
                'success': True, 
                'txList': txList, 
                'paymentId': paymentId, 
                'integratedAddress': integratedAddress,
                'foundAConfirmedTransaction': foundAConfirmedTransaction,
                'transactionSumAmountIsCorrect': transactionSumAmountIsCorrect,
                }