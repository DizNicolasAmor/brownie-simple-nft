from scripts.helpers import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network
import pytest
from scripts.deploy import deploy_and_create_collectible


def test_can_create_simple_nft():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_nft = deploy_and_create_collectible()
    assert simple_nft.ownerOf(0) == get_account()
