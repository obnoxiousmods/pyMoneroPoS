# monero-wallet-rpc --wallet-file jsontesting --password "123123" --rpc-bind-port 28088 --disable-rpc-login --rpc-bind-ip 127.0.0.1

from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet
w = Wallet(JSONRPCWallet(host="127.0.0.1", port=28088))

# If above completes your walletrpc is setup correctly

print(w.height())

mainWalletAddress = w.address()
print(mainWalletAddress)

# Confirm above is different from next address

testingIntegratedAddress = mainWalletAddress.with_payment_id("1234567890123456")
print(testingIntegratedAddress)

# Find tx history for integrated address

txHistory = w.incoming(payment_id="1234567890123456", unconfirmed=True)
print(txHistory[0])
print(dir(txHistory[0]))
print(txHistory[0])