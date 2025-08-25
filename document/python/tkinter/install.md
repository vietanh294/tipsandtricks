brew install python-tk
brew install tcl-tk
brew reinstall python@3.13 --with-tcl-tk

export PATH="/opt/homebrew/opt/tcl-tk/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/tcl-tk/lib/pkgconfig"
source ~/.zshrc
python3 -m tkinter





----
sudo apt update
sudo apt install python3-tk
