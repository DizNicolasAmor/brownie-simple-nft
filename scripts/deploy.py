from brownie import config, network, SimpleNFT
from scripts.helpers import get_account


def deploy():
    account = get_account()
    must_publish = config["networks"][network.show_active()].get("verify")
    print('Deploying...\n')

    simple_nft = SimpleNFT.deploy(
        { "from": account },
        publish_source=must_publish
    )

    print('Deployed!\n')
    print('Token name: "%s"'  % simple_nft.name())
    print('Token symbol: "%s"'  % simple_nft.symbol())
    print('Total supply: "%s"\n'  % simple_nft.totalSupply())

    return simple_nft


def create_collectible(contract_instance):
    contract_instance.createCollectible()


def main():
    instance = deploy()
    create_collectible(instance)
