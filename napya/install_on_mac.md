# Installing Ansible on a MacOS

For anyone running an Apple Mac that wants to upgrade or install Ansible on Python 3.x, use the following steps:

1. Remove the old or current version of Ansible using the inverse way you installed it (example: python -m pip uninstall ansible)

0. Check if homebrew is installed with `brew doctor`. You should get a clever response that it is time to brew the strongest potions or some such silliness.

0. If you got a message indicating brew was not recognized, you need to install it. First install xcode: `xcode-select --install`

0. Great. Now install homebrew: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

0. Cool. You now should be a potions master. Confirm this with `brew doctor`

0. Now install python3. `brew install python3`

0. Install Ansible to the local user: `python3 -m pip install --user ansible`

0. Fix your path! Without this step, you won't be able to use the command ansible. NOTE: Change RZfeeser to your local user:
    `export PATH="/Users/rzfeeser/Library/Python/3.9/bin:$PATH"`

0. You should now be able to run `ansible --version` and see the latest version of ansible supported by Python 3.x
