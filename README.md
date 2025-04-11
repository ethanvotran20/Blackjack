# 🃏 evt-blackjack

🍎 MacBook Installation Guide (via pipx)
We recommend using pipx to install evt-blackjack — it keeps everything clean, isolated, and system-safe.
✅ Step 1: Install pipx (if not already installed)
First, make sure Homebrew is installed:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Then install pipx and Python (if needed):

    brew install pipx
    brew install python  # if you don't already have Python 3 installed
    pipx ensurepath

✅ Step 2: Install evt-blackjack with pipx
    
    pipx install evt-blackjack

⚠️ Step 3: Add pipx’s binary path to your shell (if needed)
If typing bj doesn’t work after installing, you likely need to add pipx’s bin path to your PATH.

🐚 For zsh users (default on macOS):

    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc

🐚 For bash users:

    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
    source ~/.bash_profile

🃏 Step 4: Run the game!
Now you can simply run:

    bj

...from any terminal window and start playing 🃏♠️

### 🪟 Windows Users
After installing, you might see this warning:

    WARNING: The script bj.exe is installed in '...Scripts', which is not on PATH.

That just means Windows doesn't know where to find the bj command yet.
You have 2 easy options:

✅ Option 1: Use the fallback command

    python -m bj

🛠 Option 2: Add Scripts to your PATH manually

    C:\Users\your-name\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_xxx\LocalCache\local-                        packages\Python311\Scripts

Add it to your system PATH:

Open Start → “Environment Variables”

Edit the Path variable

Add a new entry for the folder path

Click OK and restart your terminal

Then you can run:
                bj
## 💡 Features

Terminal-based Blackjack with suit visuals (♥♠♦♣)

Full support for:

Hitting / Standing / Doubling Down

Blackjack detection

Betting & balance tracking

Reshuffling decks

Great for practice or just passing time in the terminal
