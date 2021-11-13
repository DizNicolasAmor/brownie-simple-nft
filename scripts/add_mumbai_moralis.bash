#!/bin/bash
brownie networks add Polygon mumbai_moralis             \
    chainid=80001                                       \
    name="Mumbai (Moralis)"                             \
    explorer='https://explorer-mumbai.maticvigil.com/'  \
    host='https://speedy-nodes-nyc.moralis.io/448b3db1d7566ce7ce7af835/polygon/mumbai'
