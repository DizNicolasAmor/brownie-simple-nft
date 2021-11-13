#!/bin/bash
brownie networks add 'Binance Smart Chain' bsc_testnet_moralis  \
    chainid=80001                                               \
    name="BSC Testnet (Moralis)"                                \
    explorer='https://testnet.bscscan.com/'                     \
    host='https://speedy-nodes-nyc.moralis.io/448b3db1d7566ce7ce7af835/bsc/testnet'
