#!/bin/bash

# update system
sudo apt update

# install pipx
sudo apt install pipx -y
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument

# install ansible
pipx install --include-deps ansible 

