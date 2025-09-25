# flet_easy_manage_digital_ingest
A Flet-Easy Python app to manage Grinnell College ingest of digital objects to Alma or CollectionBuilder.

## Setup Command Sequence

The command sequence used to produce this repo is documented below.  Because `flet-easy` still has references to `colors`, not `Colors`, I had to fork that repo, fix it, and then install it in a new VENV in this repo's parent directory using that corrected version.  

Also, note that `flet` and `flet-easy` are both installed in a VENV within the parent director, not in the repo itself.  This seems to be a necessary so that `fs init` and other `fs` commands work properly.  

Like so...  

```zsh
cd GitHub
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip3 install git+https://github.com/SummittDweller/flet-easy.git
pip3 install 'flet[all]'
pip3 install 'flet-easy[all]' --upgrade <--no longer necessary
fs init
cd flet_easy_manage_digital_ingest
code .
flet run
```

It works!  

## Creation in GitHub

After a successful test, the following steps were taken to capture this work in a new GitHub repo.  

The process started at https://github.com/Digital-Grinnell where a new empty repository was created, namely `flet_easy_manage_digital_ingest`.  After that the terminal/command line process was:  

```zsh
cd ~/GitHub/flet_easy_manage_digital_ingest
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Digital-Grinnell/flet_easy_manage_digital_ingest.git
git push -u origin main
```


> ## ⚠️ **NOTICE** ⚠️
>
> **Important:** The content below this notice is from the original repository's README.md file and may no longer be current or accurate.

# 🔥A Flet application with the [`Flet-Easy`](https://github.com/Daxexs/flet-easy) plugin.
An example of a minimal Flet application.

🗂️ Folder = flet_easy_manage_digital_ingest

To run the application:
```bash
flet run flet_easy_manage_digital_ingest/main.py.
```