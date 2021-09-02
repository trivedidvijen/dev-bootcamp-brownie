from brownie import MyFirstContract, config, accounts


def deployContract():
    """
    docstring
    """
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    MyFirstContract.deploy({"from": account})


def main():
    """
    docstring
    """
    deployContract()
