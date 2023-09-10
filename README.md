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