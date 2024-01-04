# Configuring environment

I'll document my progrees in ros in this file

## Setup

Every time i start i new cmd tab I have to write this 

command

```console
source /opt/ros/humble/setup.zsh && export ROS_DOMAIN_ID=0 && printenv | grep -i ROS && export ROS_LOCALHOST_ONLY=1
```


Output:
```console
PATH=/opt/ros/humble/bin:/home/arthur/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/arthur/.fzf/bin
PWD=/home/arthur/Documents/Github/trainee-edrom/ros
AMENT_PREFIX_PATH=/opt/ros/humble
PYTHONPATH=/opt/ros/humble/lib/python3.10/site-packages:/opt/ros/humble/local/lib/python3.10/dist-packages
LD_LIBRARY_PATH=/opt/ros/humble/opt/rviz_ogre_vendor/lib:/opt/ros/humble/lib/x86_64-linux-gnu:/opt/ros/humble/lib
ROS_DISTRO=humble
ROS_LOCALHOST_ONLY=0
ROS_PYTHON_VERSION=3
ROS_VERSION=2
```

### Ros domain

```console
export ROS_DOMAIN_ID=0
```







