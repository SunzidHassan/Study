## Setting up Robot Operating System in your 

Robot Operating System (ROS) requires specific versions of Ubuntu. For example, ROS 2 Humble require Ubuntu 22.04. We will be using VS Code dev container to setup ROS environment.

### Install VS Code
#### Windows


#### Ubuntu


### Install docker engine
#### Windows


#### Ubuntu
Find Install using the convenience script from [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/). In your terminal, execute
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
```

[Post installation steps](https://docs.docker.com/engine/install/linux-postinstall/)

```
sudo groupadd docker
sudo usermod -aG docker $USER
```
Then reboot your pc.

### Install vscode extensions
You need to install VSCode's **Remote Development** extension. Click on the Extension tab, search for Remote Development, install.


### Create a new directory


### Open the folder in vscode


### Reopen in container


### Edit container image


### 