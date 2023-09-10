from moneropos import MoneroPoS

if __name__ == "__main__":
    mPoS = MoneroPoS()
    #print(mPoS.mainWalletAddress())
    print(
        mPoS.generateNewPayment(
            paymentId="1234567890123456",
        )
    )
    
    newTxs = mPoS.findConfirmedIncomingTransactions(
                paymentId="1234567890123456",
            )

    for tx in newTxs['txList']:
        print(dir(tx))
        print(tx.amount)
        print(tx.timestamp)
        print(tx.transaction)