from brownie import config, network, SimpleNFT
from scripts.helpers import get_account


OPENSEA_URL_BASE = "https://testnets.opensea.io/assets/{}/{}"
SAMPLE_TOKEN_URI = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create_collectible():
    account = get_account()
    must_publish = config["networks"][network.show_active()].get("verify")
    print('Deploying...\n')

    contract_instance = SimpleNFT.deploy(
        { "from": account },
        publish_source=must_publish
    )

    print('Deployed!\n')
    print('Token name: "%s"'  % contract_instance.name())
    print('Token symbol: "%s"'  % contract_instance.symbol())

    tx = contract_instance.createNFT(SAMPLE_TOKEN_URI, {"from": account})
    tx.wait(1)

    OPENSEA_URL = OPENSEA_URL_BASE.format(contract_instance.address, contract_instance.tokenCounter() - 1)

    print(f"Awesome, you can view your NFT at {OPENSEA_URL}")
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")

    return contract_instance


def main():
    deploy_and_create_collectible()
