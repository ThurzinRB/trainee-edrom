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
