# brownie-simple-nft

This is a NFT dApp built with brownie.

## Requirements:

- brownie: https://github.com/eth-brownie/brownie
- yarn: https://classic.yarnpkg.com/en/
- ganache-cli: https://www.npmjs.com/package/ganache-cli

## Setup

```
   # Install OpenZeppelin v4
   $ brownie pm install OpenZeppelin/openzeppelin-contracts@4.0.0

   # compile the app
   $ brownie compile

   #run the deploy.py script
   $ brownie run scripts/deploy.py
```

## Tests

### How to test locally

```
# run all tests:
$ brownie test

# run only one test, for example test_updating_message:
$ brownie test -k test_updating_message

# run post mortem tests to debug error:
$ brownie test -pdb

# run all tests and show more detailed info:
$ brownie test -s
```

### How to deploy to a testnet

#### Kovan (Ethereum testnet)

1. Create an account. For example using MetaMask.
1. Switch into a testnet. For example, kovan.
1. Fund your account. For example using a Faucet.
1. Signup in Infura (https://infura.io/) and create a project. Call it "brownie-simple-message".
1. Inside that project, select the testnet.
1. Save the `WEB3_INFURA_PROJECT_ID` value in the `.env` file
1. With verification (optional, but recommended): in this option you can publish the source code in etherscan and a checkmark will appear in etherscan as a sign of verification.
   1. Signup in Etherscan (https://etherscan.io/), login and go to API-KEYs section. Then create an API-KEY. You have to set a name, for example "verify_brownie".
   1. Once you have the API-KEY, copy and paste it in the `.env` file as the `ETHERSCAN_TOKEN` value.
   1. In `deploy.py` file, inside the `deploy` method, pass `publish_source=True` as the last parameter.
1. In the console, run: `brownie run scripts/deploy.py --network kovan`
1. Note: with the contract address you can add the token in Metamask to see it in the UI.

#### Mumbai (Polygon testnet)

Similar considerations than **kovan** (previous section). The differences are that: use `moralis` instead of `infura` (or continue with infura) and add `mumbai` network in your Metamask.

- Guide to set mumbai network in Metamask and other stuff: https://docs.unbound.finance/guides/guide-to-accessing-polygon-testnet-and-how-to-use-unbound-faucet-tokens
- Polygon faucet: https://faucet.polygon.technology/

If you use infura, run: `brownie run scripts/deploy.py --network polygon-test`

Instead, if you use Moralis:

- Create an account in https://moralis.io/
- Create a server in Polygon network (and other networks if you will use them).
- Then, go to "Speedy nodes" and copy your mumbai endpoint. Replace the host value in `add_mumbai_moralis.bash` file with the value you just copied.
- In the terminal, run `bash ./scripts/add_mumbai_moralis.bash`: this scripts adds a network to brownie.
- You can confirm the network was added by running: `brownie networks list` and check that `mumbai_moralis` is on that list.
- Deploy command: `brownie run scripts/deploy.py --network mumbai_moralis`
- Useful link: https://moralis.io/how-to-create-your-own-erc-20-token-in-10-minutes/

#### BSC Testnet (Moralis)

Same considerations than Mumbai (previous section)

- Faucet: https://testnet.binance.org/faucet-smart
- Bash script: `bash ./scripts/add_bsc_testnet_moralis.bash`
- Explorer: https://testnet.bscscan.com/
- Add blockchain config to Metamask: search for the Metamask button in explorer page.
- Deploy command: `brownie run scripts/deploy.py --network bsc_testnet_moralis`
