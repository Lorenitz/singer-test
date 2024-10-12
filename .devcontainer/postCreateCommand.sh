#!/bin/bash

# install pyenv
curl https://pyenv.run | bash
printf '\nexport PYENV_ROOT="$HOME/.pyenv"\n[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"\neval "$(pyenv init -)"\n' >> ~/.bashrc
. /home/vscode/.bashrc # reload .bashrc to make pyenv available
alias pyenv=/home/vscode/.pyenv/bin/pyenv

# switch to python v 3.9.1
/home/vscode/.pyenv/bin/pyenv install 3.9.1
/home/vscode/.pyenv/bin/pyenv global  3.9.1
