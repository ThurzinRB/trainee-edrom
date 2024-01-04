# Understanding topics

command:
```console
rqt_graph
```
output

![Alt text](./img/Screenshot%20from%202024-01-03%2023-56-43.png)

```console
➜  trainee-edrom git:(main) ✗ ros2 topic list                     
/parameter_events
/rosout
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```

```console
➜  trainee-edrom git:(main) ✗ ros2 topic list -t
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
/turtle1/cmd_vel [geometry_msgs/msg/Twist]
/turtle1/color_sensor [turtlesim/msg/Color]
/turtle1/pose [turtlesim/msg/Pose]
```