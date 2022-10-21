
<img src="https://www.dataquest.io/wp-content/uploads/2022/01/python-virtual-envs1.webp" width="800"/>

- Using virtual environments is a way that you can separate different Python environments for different projects.

- So why would you want to do something like this?

- For example say that you have multiple projects and they all rely on Flask.

- And these may have been projects you inherited and didn't write. So some projects may be using a different version of Flask.

- Now if you went and upgraded Flask to the latest version, you may find that WHAM- that Flask script doesn't work anymore and now you've got a bunch of broken websites and angry clients.

- So it would be better if each project had an isolated environment where each project has their own special little dependency packages and whatever adorable specific version they require. And that's what virtual env allows us to do.

```
python3 -m pip install virtualenv
python3 -m pip list
mkdir environments
cd environments/
ls
virtualenv demo1_env
source demo1_env/bin/activate
which python3
which pip
python3 -m pip list
python3 -m pip install --upgrade pip
python3 -m pip install flask
python3 -m pip list
python3 -m pip freeze
python3 -m pip freeze --local
python3 -m pip freeze > requirements.txt
cat requirements.txt 
deactivate
which python3
python3 -m pip list
ls
rm -rf demo1_env/
sudo apt update
sudo apt install python3
sudo apt install python2
python2 --version
which python2
virtualenv -p /usr/bin/python2 demo2_py2
source demo2_py2/bin/activate
which python
python --version
python3 --version
python2 --version
python --version
pip list
pip3 list
pip install -r requirements.txt 
deactivate
```
