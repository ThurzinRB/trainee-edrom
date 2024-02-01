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

# Turtle sim

Command:

```console
sudo apt update

sudo apt install ros-humble-turtlesim
```

Output:
```console
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ros-humble-turtlesim is already the newest version (1.4.2-1jammy.20231205.184659).
The following packages were automatically installed and are no longer required:
  gconf-service gconf-service-backend gconf2-common libc++1 libgconf-2-4 linux-headers-5.15.0-73 linux-headers-5.15.0-73-generic linux-headers-5.15.0-75 linux-headers-5.15.0-75-generic
  linux-headers-5.15.0-84 linux-headers-5.15.0-84-generic linux-headers-5.15.0-88 linux-headers-5.15.0-88-generic linux-headers-5.15.0-89 linux-headers-5.15.0-89-generic
  linux-image-5.15.0-73-generic linux-image-5.15.0-75-generic linux-image-5.15.0-84-generic linux-image-5.15.0-88-generic linux-image-5.15.0-89-generic linux-modules-5.15.0-73-generic
  linux-modules-5.15.0-75-generic linux-modules-5.15.0-84-generic linux-modules-5.15.0-88-generic linux-modules-5.15.0-89-generic linux-modules-extra-5.15.0-73-generic
  linux-modules-extra-5.15.0-75-generic linux-modules-extra-5.15.0-84-generic linux-modules-extra-5.15.0-88-generic linux-modules-extra-5.15.0-89-generic
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```
Output:

```console
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```
## Start turtlesim
```console
ros2 run turtlesim turtlesim_node
```
Output:
```console
[INFO] [1704302973.519933290] [turtlesim]: Starting turtlesim with node name /turtlesim
[INFO] [1704302973.535802908] [turtlesim]: Spawning turtle [turtle1] at x=[5,544445], y=[5,544445], theta=[0,000000]
```
![Alt text](./img/Screenshot%20from%202024-01-03%2014-30-33.png "Turtle sim window")

## use turtlesim

Command:
```console
ros2 run turtlesim turtle_teleop_key
```

Output:
```console
Reading from keyboard
---------------------------
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
'Q' to quit.
```

Command:
```console
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
```
Output:
```console
/teleop_turtle
/parameter_events
/rosout
/turtle1/cmd_vel
/teleop_turtle/describe_parameters
/teleop_turtle/get_parameter_types
/teleop_turtle/get_parameters
/teleop_turtle/list_parameters
/teleop_turtle/set_parameters
/teleop_turtle/set_parameters_atomically
/turtle1/rotate_absolute
```

## Install rqt

command:
```console
rqt
```
output:

![Alt text](./img/Screenshot%20from%202024-01-03%2014-45-02.png "rqt start")

## calling services

![Alt text](./img/Screenshot%20from%202024-01-03%2022-53-28.png)

## Remapping

Command:
```console
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel
```

Output

![Alt text](./img/Screenshot%20from%202024-01-03%2022-56-47.png)


# Understanding nodes

## ros2 run

command:
```console
ros2 run turtlesim turtlesim_node
```

output:
```console
[INFO] [1704334405.182405111] [turtlesim]: Starting turtlesim with node name /turtlesim
[INFO] [1704334405.184109202] [turtlesim]: Spawning turtle [turtle1] at x=[5,544445], y=[5,544445], theta=[0,000000]
```

## node list

comand:
```console
ros2 node list
```

output:
```
/turtlesim
```

command:
```console
ros2 run turtlesim turtle_teleop_key
```
output:
```console
Reading from keyboard
---------------------------
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
'Q' to quit.
```

## Remapping

command:
```console
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```
output:
```console
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
[INFO] [1704334778.523262492] [my_turtle]: Starting turtlesim with node name /my_turtle
[INFO] [1704334778.525555991] [my_turtle]: Spawning turtle [turtle1] at x=[5,544445], y=[5,544445], theta=[0,000000]
```

command:
```console
ros2 node list
```
output:
```console
/my_turtle
/teleop_turtle
/turtlesim
```

## Node info

command:
```console
ros2 node info /my_turtle
```
output;
```console
/my_turtle
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /my_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /my_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /my_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /my_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /my_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /my_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```

with telop_turtle:

```console
/teleop_turtle
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Service Servers:
    /teleop_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /teleop_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /teleop_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /teleop_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /teleop_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /teleop_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
```

# Understanding nodes

## ros2 run

command:
```console
ros2 run turtlesim turtlesim_node
```

output:
```console
[INFO] [1704334405.182405111] [turtlesim]: Starting turtlesim with node name /turtlesim
[INFO] [1704334405.184109202] [turtlesim]: Spawning turtle [turtle1] at x=[5,544445], y=[5,544445], theta=[0,000000]
```

## node list

comand:
```console
ros2 node list
```

output:
```
/turtlesim
```

command:
```console
ros2 run turtlesim turtle_teleop_key
```
output:
```console
Reading from keyboard
---------------------------
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
'Q' to quit.
```

## Remapping

command:
```console
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
```
output:
```console
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
[INFO] [1704334778.523262492] [my_turtle]: Starting turtlesim with node name /my_turtle
[INFO] [1704334778.525555991] [my_turtle]: Spawning turtle [turtle1] at x=[5,544445], y=[5,544445], theta=[0,000000]
```

command:
```console
ros2 node list
```
output:
```console
/my_turtle
/teleop_turtle
/turtlesim
```

## Node info

command:
```console
ros2 node info /my_turtle
```
output;
```console
/my_turtle
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /my_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /my_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /my_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /my_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /my_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /my_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```

with telop_turtle:

```console
/teleop_turtle
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Service Servers:
    /teleop_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /teleop_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /teleop_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /teleop_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /teleop_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /teleop_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
```




