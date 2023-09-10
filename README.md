# pyMoneroPoS
A library for python applications to use native monero payment processing, you'll need a monero node synced for this to work properly.

Examples

    starletteExample.py

    is a fully working webapp that uses sessions + mongodb to track and process a payment

Requirements

    monerod synced
    monero-wallet-rpc running 127.0.0.1 28088 and connected to monerod
    if its remote use a ssh tunnel

About

    This is a python library to simplify the process for a developer to accept monero payments programatically


Basic Example

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