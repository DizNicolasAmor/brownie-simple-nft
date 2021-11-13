#!/bin/bash
brownie networks add Ethereum ganache_local             \
    chainid=1337                                        \
    name="Ganache (Local)"                              \
    host='http://0.0.0:8545'
