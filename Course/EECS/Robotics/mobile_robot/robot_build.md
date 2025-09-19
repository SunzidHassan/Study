# Table of Contents

- [Table of Contents](#table-of-contents)
- [Log](#log)
  - [2025](#2025)
    - [September](#september)
- [Docker for Robotics](#docker-for-robotics)
  - [ROS2 Dev Container Setup](#ros2-dev-container-setup)
- [Making a Mobile Robot](#making-a-mobile-robot)
  - [Introduction](#introduction)
    - [Adding Files](#adding-files)
  - [Robot Model](#robot-model)
    - [URDF Syntax](#urdf-syntax)
      - [Creating URDF](#creating-urdf)
    - [Links](#links)
    - [Joints](#joints)
    - [xacro](#xacro)
    - [Robot URDF Example](#robot-urdf-example)
  - [Driving the Robot (in old Gazebo)](#driving-the-robot-in-old-gazebo)
  - [Robot Brain: Pi](#robot-brain-pi)
  - [Powering the Robot](#powering-the-robot)
    - [Deciding Battery Voltage](#deciding-battery-voltage)
    - [Current Draw](#current-draw)
    - [Battery](#battery)
  - [Motors](#motors)
    - [L298N Motor Driver](#l298n-motor-driver)
    - [Motor-Driver-Arduino Pairing](#motor-driver-arduino-pairing)
    - [ROS Driver](#ros-driver)
  - [LiDAR](#lidar)
    - [Connecting Physical LiDAR](#connecting-physical-lidar)
  - [Camera](#camera)
    - [Camera and Images Fundamentals](#camera-and-images-fundamentals)
      - [Image Representation](#image-representation)
      - [Image Compression](#image-compression)
      - [Camera Parameter - Focal Length](#camera-parameter---focal-length)
      - [ROS-Camera/Image Integration](#ros-cameraimage-integration)
      - [Coordinate Systems](#coordinate-systems)
      - [Gazebo Camera Simulation](#gazebo-camera-simulation)
        - [Camera Xacro](#camera-xacro)
      - [Connecting a Real Camera and Getting Data](#connecting-a-real-camera-and-getting-data)
    - [Depth Camera](#depth-camera)
      - [Depth Camera Fundamentals](#depth-camera-fundamentals)
      - [ROS-Depth Camera Integration and Simulation](#ros-depth-camera-integration-and-simulation)
        - [Depth Camera Xacro](#depth-camera-xacro)
      - [Connecting a Real Depth Camera and Getting Data](#connecting-a-real-depth-camera-and-getting-data)
  - [Chassis Design](#chassis-design)
    - [Bench test components](#bench-test-components)
  - [Control](#control)
    - [ROS2 Control](#ros2-control)
      - [Setting up ROS2 Control](#setting-up-ros2-control)
        - [ROS2 Control Xacro](#ros2-control-xacro)
      - [Starting controllers](#starting-controllers)
      - [Extra bits](#extra-bits)
        - [Gazebo lag](#gazebo-lag)
        - [Wheel friction and rviz2 lag](#wheel-friction-and-rviz2-lag)
        - [Object scan move around for simulation](#object-scan-move-around-for-simulation)
    - [Driving Actual Robot using ROS2 Control](#driving-actual-robot-using-ros2-control)
      - [Setting up controller manager](#setting-up-controller-manager)
      - [Testing the real robot](#testing-the-real-robot)
      - [Switch real and gazebo controller manager](#switch-real-and-gazebo-controller-manager)
    - [Wireless Control](#wireless-control)
      - [Getting feedback using rviz2](#getting-feedback-using-rviz2)
    - [Phone Control](#phone-control)
  - [SLAM](#slam)
    - [ROS and SLAM](#ros-and-slam)
    - [Running on real robot](#running-on-real-robot)
  - [Nav2](#nav2)
  - [Additional Hardware](#additional-hardware)
  - [Humble](#humble)
  - [New Gazebo](#new-gazebo)

---
# Log
## 2025
### September
- Managed to run LiDAR, but not rplidar.launch.pi
- Managed to run 

# Docker for Robotics

## ROS2 Dev Container Setup

- Install Docker Engine for Ubuntu using the convenience script and post-installation steps.
- Install Remote Development extension in VSCode.
- Install and configure NVIDIA Container Toolkit.
- Disconnect VPN.
- Don't install Python/Anaconda.
- Install correct CUDA for latest PyTorch (default CUDA may be fine), install default PyTorch.

```json
{
  "name": "humble desktop-full",
  "dockerFile": "Dockerfile",
  "runArgs": [
    "--privileged",
    "--network=host",
    "--gpus","all"
  ],
  "workspaceMount": "source=${localWorkspaceFolder},target=/${localWorkspaceFolderBasename},type=bind",
  "workspaceFolder": "/${localWorkspaceFolderBasename}",
  "mounts": [
    "source=${localEnv:HOME}${localEnv:USERPROFILE}/.bash_history,target=/home/vscode/.bash_history,type=bind"
  ],
  "features": {
    "ghcr.io/devcontainers/features/desktop-lite:1": {},
    "ghcr.io/devcontainers/features/nvidia-cuda:1": {},
    "ghcr.io/raucha/devcontainer-features/pytorch:1": {}
  }
}
```

**Running GUI**

```bash
xhost +local:
```
In terminal, and rebuild container.

---

# Making a Mobile Robot

## Introduction

**Differential Drive:** Robot with two wheels driving it.

**Base link:** Main coordinate system: x-pointing forward, y-pointing left, z-pointing up.

![Robot State Publisher](./images/Robot_state_publisher.png)

The main coordinate frame of the robot is called `base_link` with x pointing forward, y pointing left, z pointing up.

We start with config files written in URDF format that altogether describe the structure of the robot. These are combined using xacro into a single processed URDF file.

This URDF robot structure is passed to `robot_state_publisher`. This makes URDF data in `/robot_description` topic, and broadcasts appropriate transforms `/tf`.

If any joint moves, `robot_state_publisher` expects the input to be published on the `/joint_states` topic.

While testing, we can use the `/joint_state_publisher_gui` to fake these values.

We run all of these files using launch files.

Every time we add a URDF file, we need to run:

```bash
colcon build --symlink-install
source install/setup.bash
```

After change, we need to quit and relaunch `/robot_state_publisher`. If Rviz doesn't show updates in URDF visualization, refresh.

### Adding Files

You can copy `blue_bot` and `blue_bot_controller` folders to your `/src` folder and run:

```bash
colcon build --symlink-install
source install/setup.bash
```

Run the `/robot_state_publisher` by running the launch file:

```bash
ros2 launch blue_bot rsp.launch.py
```

---

## Robot Model

### URDF Syntax

URDF is based on XML, where everything is represented as a series of tags nested inside each other.

```xml
<?xml version="1.0"?>
<robot name="my_bot">
  <link name="link_name"></link>
  <joint name="joint_name"></joint>
  <link></link>
  ...
</robot>
```

#### Creating URDF

In `workspace/src/`, we have `blue_bot/description/robot.urdf.xacro`:

```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="robot">
  <!-- we'll add the robot_core.xacro -->
  <xacro:include filename="robot_core.xacro" />
</robot>
```

Now add a new file `robot_core.xacro` in the same directory.

Install joint_state_publisher_gui:

```bash
sudo apt install ros-jazzy-joint-state-publisher-gui
```

---

### Links

Each `<link>` tag represents one link. It must have a name, but can also have 3 additional properties:

- `<visual>`
  - `<geometry>`: defines the overall shape (box, cylinder, sphere, path to a 3d mesh)
  - `<origin>`: offset for the geometry, so that it doesn't have to center around the origin.
  - `<material>`: for color

- `<collision>`: for physics calculations, includes `<geometry>` and `<origin>` that can be copied from `<visual>`. This can be made simple for computational savings.

- `<inertial>`: for physics calculation - how the links react to forces.
  - `<mass>`
  - `<origin>`: the center of gravity, for most cases the same as visual and collision origin.
  - `<inertia>`: rotational inertia matrix.

**Link coordinate system:** If the `link` can rotate, it should have the origin at the pivot point.

**Link joints:** Joints show relation of the origin and coordinate frame of the links, which determines the position and orientation of the links.

**Link motion:**
- *Revolute*: rotational motion about a point, with fixed start and stop angle.
- *Continuous*: rotational motion about a point, without fixed limit - wheel.
- *Prismatic*: linear translational motion.
- *Fixed*: child link doesn't move relative to the parent link.

---

### Joints

Joints specify where the links are in space.

```xml
<joint name="arm_joint" type="revolute">
  <parent link="slider_link"/>
  <child link="arm_link"/>
  <origin xyz="0.25 0 0.15" rpy="0 0 0"/>
  <axis xyz="0 -1 0"/>
  <limit lower="0" upper="${pi/2}" velocity="100" effort="100"/>
</joint>
```

Other tags include `<material>` for colors, `<gazebo>` for simulation, `<transmission>` for actuator connection.

Naming convention: `_link`, `_joint` (e.g., `arm_link` is the child link in `arm_joint`).

---

### xacro

XML macro (xacro) helps with URDF files:
- Splitting URDF into multiple files
- Avoidance of repetition

To add xacro in a URDF file:

```xml
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">
```

xacro compiles split URDF files into one URDF, which is fed to robot_state_publisher, which publishes the complete URDF on `/robot_description` topic.

**Example:**

`my_robot.urdf.xacro`
```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="my_robot">
  <xacro:include filename="my_materials.xacro"/>
  <link>...</link>
  <joint>...</joint>
</robot>
```

`my_materials.xacro`
```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">
  <material name="white">
    <color rgba="1 1 1 1"/>
  </material>
</robot>
```

**Properties:**
```xml
<xacro:property name="arm_radius" value="0.5"/>
<cylinder radius="${arm_radius}" length="7"/>
```

**Math operations:**
```xml
<cylinder length="${4*arm_radius*pi1}"/>
```

**Macros:**
```xml
<xacro:macro name="inertial_box" params="mass x y z *origin">
  <inertial>
    <xacro:insert_block name="origin"/>
    <mass value="${mass}"/>
    <inertia ixx="${(1/12) * mass * (y*y+z*z)}"/>
  </inertial>
</xacro:macro>
```

Usage:
```xml
<xacro:inertial_box mass="12" x="2" y="3" z="4">
  <origin xyz="0 2 4" rpy="0 0 0"/>
</xacro:inertial_box>
```

---

### Robot URDF Example

```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">

  <xacro:include filename="inertial_macros.xacro" />

  <!-- Define colors -->
  <material name="white">
    <color rgba="1 1 1 1"/>
  </material>
  <material name="black">
    <color rgba="0 0 0 1"/>
  </material>
  <material name="orange">
    <color rgba="1 0.3 0.1 1"/>
  </material>
  <material name="blue">
    <color rgba="0.2 0.2 1 1"/>
  </material>

  <!-- BASE_LINK -->
  <link name="base_link"></link>

  <!-- CHASSIS LINK -->
  <joint name="chassis_joint" type="fixed">
    <parent link="base_link"/>
    <child link="chassis"/>
    <origin xyz="0 0 0"/>
  </joint>
  <link name="chassis">
    <visual>
      <origin xyz="0 0 0.0625"/>
      <geometry>
        <cylinder radius="0.08" length="0.125"/>
      </geometry>
      <material name="blue"/>
    </visual>
    <collision>
      <origin xyz="0 0 0.0625"/>
      <geometry>
        <cylinder radius="0.08" length="0.125"/>
      </geometry>
    </collision>
    <xacro:inertial_cylinder mass="2.0" length="0.125" radius="0.08">
      <origin xyz="0 0 0.0625" rpy="0 0 0"/>
    </xacro:inertial_cylinder>
  </link>

  <!-- LEFT WHEEL LINK -->
  <joint name="left_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="left_wheel"/>
    <origin xyz="0 0.08 0" rpy="-${pi/2} 0 0"/>
    <axis xyz="0 0 1"/>
  </joint>
  <link name="left_wheel">
    <visual>
      <geometry>
        <cylinder radius="0.0325" length="0.02"/>
        <material name="black"/>
      </geometry>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.0325" length="0.02"/>
      </geometry>
    </collision>
    <xacro:inertial_cylinder mass="0.5" length="0.02" radius="0.0325">
      <origin xyz="0 0 0" rpy="0 0 0"/>
    </xacro:inertial_cylinder>
  </link>

  <!-- RIGHT WHEEL LINK -->
  <joint name="right_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="right_wheel"/>
    <origin xyz="0 -0.08 0" rpy="${pi/2} 0 0"/>
    <axis xyz="0 0 -1"/>
  </joint>
  <link name="right_wheel">
    <visual>
      <geometry>
        <cylinder radius="0.0325" length="0.02"/>
        <material name="black"/>
      </geometry>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.0325" length="0.02"/>
      </geometry>
    </collision>
    <xacro:inertial_cylinder mass="0.5" length="0.02" radius="0.0325">
      <origin xyz="0 0 0" rpy="0 0 0"/>
    </xacro:inertial_cylinder>
  </link>

  <!-- Front Caster Wheel Link -->
  <joint name="front_caster_wheel_joint" type="fixed">
    <parent link="chassis"/>
    <child link="front_caster_wheel"/>
    <origin xyz="0.07 0 0"/>
  </joint>
  <link name="front_caster_wheel">
    <visual>
      <geometry>
        <sphere radius="0.0325"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.0325"/>
      </geometry>
    </collision>
    <xacro:inertial_sphere mass="0.5" radius="0.0325">
      <origin xyz="0 0 0" rpy="0 0 0"/>
    </xacro:inertial_sphere>
  </link>

  <!-- Back Caster Wheel Link -->
  <joint name="back_caster_wheel_joint" type="fixed">
    <parent link="chassis"/>
    <child link="back_caster_wheel"/>
    <origin xyz="-0.07 0 0"/>
  </joint>
  <link name="back_caster_wheel">
    <visual>
      <geometry>
        <sphere radius="0.0325"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.0325"/>
      </geometry>
    </collision>
    <xacro:inertial_sphere mass="0.5" radius="0.0325">
      <origin xyz="0 0 0" rpy="0 0 0"/>
    </xacro:inertial_sphere>
  </link>

</robot>
```

After adding wheel link, run:

```bash
ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

before opening rviz2.

In rviz, set `Global Options > Fixed Frame` to `base_link`. Add `/tf`, show names. Add robot body and set `Description Topic` to `/robot_description`.

---

## Driving the Robot (in old Gazebo)

Robot launcher:

```bash
ros2 launch blue_bot rsp.launch.py use_sim_time:=true
```

Gazebo launcher:

```bash
ros2 launch gazebo_ros gazebo.launch.py
```

Entity spawner in gazebo:

```bash
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity <NAME>
```

Combining these 3 with a single launcher file:

```python
def generate_launch_description():
    # ...existing code...
    return LaunchDescription([
        rsp,
        joystick,
        twist_mux,
        gazebo,
        spawn_entity,
        diff_drive_spawner,
        joint_broad_spawner
    ])
```

Now launch using the combined launcher:

```bash
ros2 run gazebo_ros launch_sim.launch.py
```

---

## Robot Brain: Pi

- **PC**
  - 64-bit
  - RAM: >= 4GB
  - Storage: >=
  - 5V low current
- **OS**
  - ROS compatible Ubuntu
- **Software**
  - Git
  - Openssh-server
  - Arduino IDE
  - VS Code
- **Networking:** Remote PC and Pi on the same network with internet
- **ROS**
  - Install main packages following official instructions
  - Install colcon
  - Setup environment
- **Setup workspace and packages**

---

## Powering the Robot

| Name    | Other Names        | Units              | Symbol | Water Analogy         |
| ------- | ------------------ | ------------------ | ------ | --------------------- |
| Voltage | Potential Diff.    | Volts (V)          | V      | Water Pressure        |
| Current | Amperage           | Amperes/Amps (A)   | I      | Flow Rate of Water    |
| Power   | Wattage            | Watts (W)          | P      | Power of Flow         |

- $P=VI$. Power in supplier indicates the max power it can provide (5W with 5V-1A) or draw.
- Most electrical components use 5V.
- Motors draw more.
- Use switching regulator/buck converter to convert high voltage into 5V.

### Deciding Battery Voltage

12V for DC motors.

### Current Draw

![Estimated current draw](./images/current_draw.png)

- The demand is about 5A. So the regulator needs to be capable of delivering $5V\times 5A=25W$ of power.
- The supply is $25W/12V\approx 2.1\rightarrow 2.5A$
- Motor demand: highest (stall) current draw * 2 $1.8A\times 2=3.6A$
- Total current $2.5+3.6=6.1A$

### Battery

LiPo

- S number: number of cells
- Cell voltage: nominally 3.7V (11.1 for 3S); safe range 3.2V-4.2V (**3S 9.6V-12.6V**)
- Capacity: how much mA it takes to empty the battery in 1 hour - 3000 mAh battery could run for 30 minutes at 6A. But you'd want to use at most 2/3.
- C number: max discharge current = C number $\times$ capacity. 3000 mAh $\times$ 20C = 60A max current (draining the battery in 3 minutes!).

LiPo needs careful handling.

- Check voltage regularly
- Charge with a good charger at a fireproof setup
- Make sure the wiring (gauge) and connector current carrying capacity. For example, breadboards can only handle milliamps.
- Pi can handle specific current flow, so external devices should be powered separately, with a USB hub for instance.
- We also need switch and fuse for safety.

![Power circuit](./images/power_circuit.png)

---

## Motors

- Robot controller (e.g., Pi calculating required speed)
  - Comms layer: computer to motor controller (e.g., USB serial)
    - closed-loop or feedback control (e.g., PID control takes motor measurement and adjusts target speed)
      - open-loop control (map joystick button to target speed)
        - motor controller (takes target-speed/position, outs low-voltage signal)
          - motor driver (takes low-voltage signal and current, outs amplified high-voltage signal)
            - voltage signal
              - 12V DC motor

![Motor Circuit](./images/motor_loop.png)

### L298N Motor Driver

- It has 12V in for motors, and 5V in for the L298N chip.
- Pair of terminals in each side are for the motors.

### Motor-Driver-Arduino Pairing

- Upload driver code on the Arduino
- Connect Arduino to the motor driver
Arduino		L298N
- D10		L Fwd - IN2
- D6		L Rev - IN1
- D9		R Fwd - IN3
- D5		R Rev - IN4

Arduino		Encoder pin
- Gnd		Black
- 5V		Blue
- D2		Left A (Left Green)
- D3		Left B (Left Yellow)
- A4		Right A (Right Yellow)
- A5		Right B (Right Green)

- Install pyserial
- Check the USB in which the Arduino is connected (e.g., `/dev/ttyUSB0` or `/dev/ttyACM0`)
- Check if the motor control works using pyserial (by sending serial command): `python3 -m serial.tools.miniterm /dev/ttyUSB0 57600 --echo` or `python3 -m serial.tools.miniterm /dev/ttyACM0 57600 --echo`
  - `e` for checking current speed
  - `r` to reset
  - `o (+/-)0-255 (+/-)0-255` for spinning at variable speed with open-loop control
  - `m (+/-)0-255 (+/-)0-255` for spinning at variable speed with closed-loop control

- The motor encoders can have 4 wires - two will go to 5V and Gnd to power the encoder circuit, two will go to Arduino input.
- After connecting the encoder to the Arduino, check if rotating the wheel gives positive return (r in miniterm). Otherwise, swap the motor power wires.
- Rotate the wheel by n times, get encoder reading e (e in miniterm), e/n is rev of encoders per rev of wheel. For my first motor, it's about 1970.
- In the Arduino code, PID loop runs 30 loops/sec, number of encoder counts per PID loop = (e/n)/30=1970/30=66 - is the magnitude (range 0-255) for 1 rev/sec. But after testing closed loop, m 36 gives approx 1 rev, which makes e/n=36*30=1080


### ROS Driver

Demo driver with two nodes, an encoder listener in topic and send them to the controller, another GUI for sending commands.

On the both the dev machine and PI:

- Clone https://github.com/joshnewans/serial_motor_demo in workspace (src) folder, build, source.

```bash
ros2 run serial_motor_demo driver --ros-args -p serial_port:=/dev/ttyUSB0 -p baud_rate:=57600 -p loop_rate:=30 -p encoder_cpr:=1080

#or
ros2 run serial_motor_demo driver --ros-args -p serial_port:=/dev/ttyACM0 -p baud_rate:=57600 -p loop_rate:=30 -p encoder_cpr:=1080

```

`Error: Serial timeout on command: e` is OK.

On the dev machine:

```bash
ros2 run serial_motor_demo gui
```

---

## LiDAR

Can be based on sound or light, 1/2/3D.

In ROS, different LiDAR are subscribed using `/scan`.

In the robot description `robot.urdf.xacro`, add another xacro file for lidar.

**LiDAR xacro:**

```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" >

  <joint name="laser_joint" type="fixed">
    <parent link="chassis"/>
    <child link="laser_frame"/>
    <origin xyz="0.122 0 0.212" rpy="0 0 0"/>
  </joint>

  <link name="laser_frame">
    <visual>
      <geometry>
        <cylinder radius="0.05" length="0.04"/>
      </geometry>
      <material name="black"/>
    </visual>
    <visual>
      <origin xyz="0 0 -0.05"/>
      <geometry>
        <cylinder radius="0.01" length="0.1"/>
      </geometry>
      <material name="black"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.05" length="0.04"/>
      </geometry>
    </collision>
    <xacro:inertial_cylinder mass="0.1" length="0.04" radius="0.05">
      <origin xyz="0 0 0" rpy="0 0 0"/>
    </xacro:inertial_cylinder>
  </link>

  <gazebo reference="laser_frame">
    <material>Gazebo/Black</material>
    <sensor name="laser" type="ray">
      <pose> 0 0 0 0 0 0 </pose>
      <visualize>false</visualize>
      <update_rate>10</update_rate>
      <ray>
        <scan>
          <horizontal>
            <samples>360</samples>
            <min_angle>-3.14</min_angle>
            <max_angle>3.14</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.3</min>
          <max>12</max>
        </range>
      </ray>
      <plugin name="laser_controller" filename="libgazebo_ros_ray_sensor.so">
        <ros>
          <argument>~/out:=scan</argument>
        </ros>
        <output_type>sensor_msgs/LaserScan</output_type>
        <frame_name>laser_frame</frame_name>
      </plugin>
    </sensor>
  </gazebo>

</robot>
```

In Rviz2, add LaserScan topic.

### Connecting Physical LiDAR

On Pi, install rplidar driver with `sudo apt install ros-${ROS_DISTRO}-rplidar-ros`.

To figure out the USB where the LiDAR is connected:

```bash
ls /dev/serial/by-path/
```

Run:

```bash
ros2 run rplidar_ros rplidar_composition --ros-args  -p serial_port:=/dev/ttyUSB0 -p serial_baudrate:=115200 -p frame_id:=laser_frame -p inverted:=false -p angle_compensate:=true -p scan_mode:=Standard
```

On dev machine, launch `rviz2`. If the robot state publisher is not published, select Fixed Frame `laser_frame`.

To start/stop LiDAR motor:

```bash
ros2 service call /stop_motor std_srvs/srv/Empty {}
```

---

## Camera

### Camera and Images Fundamentals

- Types: RGB, infrared, thermal, wide angle, telephoto
- Capture light through a lens, aperture, onto a sensor.

#### Image Representation

Stored in 2D array of pixels. For RGB, 3 color channels per pixel (0-255).

#### Image Compression

PNG is lossless, JPEG is lossy.

#### Camera Parameter - Focal Length

Affects horizontal Field of View (FOV):

$$
\text{h\_fov}=2\tan^{-1}\left(\frac{\text{sensor\_width}}{2\times \text{focal\_length}}\right)
$$

---

#### ROS-Camera/Image Integration

- Driver node communicates with hardware, publishes to `sensor_msgs/Image` and `sensor_msgs/CompressedImage`.
- The published unprocessed image is called `/image_raw` or `/image_raw/compressed`.
- `sensor_msgs/CameraInfo` contains camera related info.

---

#### Coordinate Systems

- **ROS:** Right-hand rule, `camera_link` (x-forward, y-left, z-up)
- **Camera:** Left-hand rule, `camera_link_optical` (x-left to right, y-top to bottom, z-away from camera)

![ROS and camera coordinate system](./images/ros_and_camera_coordinates.png)

---

#### Gazebo Camera Simulation

In the robot description `robot.urdf.xacro`, add another xacro file for camera.

##### Camera Xacro

```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" >

  <joint name="camera_joint" type="fixed">
    <parent link="chassis"/>
    <child link="camera_link"/>
    <origin xyz="0.276 0 0.181" rpy="0 0.18 0"/>
  </joint>

  <link name="camera_link">
    <visual>
      <geometry>
        <box size="0.010 0.03 0.03"/>
      </geometry>
      <material name="black"/>
    </visual>
    <visual>
      <origin xyz="0 0 -0.05"/>
      <geometry>
        <cylinder radius="0.002" length="0.1"/>
      </geometry>
      <material name="black"/>
    </visual>
  </link>

  <!-- Special joint for ros coordinate system to vision coordinate system -->
  <joint name="camera_optical_joint" type="fixed">
    <parent link="camera_link"/>
    <child link="camera_link_optical"/>
    <origin xyz="0 0 0" rpy="${-pi/2} 0 ${-pi/2}"/>
  </joint>
  <link name="camera_link_optical"></link>

  <gazebo reference="camera_link">
    <material>Gazebo/Black</material>
    <sensor name="camera" type="camera">
      <pose> 0 0 0 0 0 0 </pose>
      <visualize>true</visualize>
      <update_rate>10</update_rate>
      <camera>
        <camera_info_topic>camera/camera_info</camera_info_topic>
        <horizontal_fov>1.089</horizontal_fov>
        <image>
          <format>R8G8B8</format>
          <width>640</width>
          <height>480</height>
        </image>
        <clip>
          <near>0.05</near>
          <far>8.0</far>
        </clip>
      </camera>
      <topic>camera/image_raw</topic>
      <gz_frame_id>camera_link_optical</gz_frame_id>
    </sensor>
  </gazebo>

</robot>
```

Install compressed image transport plugins:

```bash
sudo apt install ros-${ROS_DISTRO}-image-transport-plugins
sudo apt install ros-${ROS_DISTRO}-rqt-image-view
```

View compressed image:

```bash
ros2 run rqt_image_view rqt_image_view
ros2 run image_transport list_transports
ros2 run image_transport republish compressed raw --ros-args -r in/compressed:=/camera/image_raw/compressed -r out:=/camera/image_raw/uncompressed
```

---

#### Connecting a Real Camera and Getting Data

Install camera on Pi:

```bash
sudo apt install libraspberrypi-bin v4l-utils ros-${ROS_DISTRO}-v4l2-camera
groups # check if video is in groups, if not:
sudo usermod -aG video robot # add video to group > reboot
vcgencmd get_camera # check if camera is connected to the pi
raspistill -k # shows camera feed. Press x > Enter to close
v4l2-ctl --list-devices # check if video for linux subsystem can see camera
sudo apt install ros-${ROS_DISTRO}-image-transport-plugins ros-${ROS_DISTRO}-rqt-image-view
```


Run the camera:

```bash
ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]" -p camera_frame_id:=camera_link_optical
# or
ros2 launch camera.launch.py
```

On a new terminal:

```bash
ros2 run rqt_image_view rqt_image_view
```

---

### Depth Camera

#### Depth Camera Fundamentals

- Major types:
  - Structured light: emit light (e.g., IR) and record
  - Time-of-Flight: emit light, record time of return.
  - Stereo: record with two cameras.
- Pipeline: raw data > depth processing > depth image > 3D projection > point cloud
- Just like normal image, depth image has topics and transprot.
- **Storage**: depth data is stored as 32-bit Float in meters, or 16-bit Uint in mm.
- The depth image can be viewed. In such case the image is normalized - the furthest thing is white and the closest thing is black.
- ROS `depth_image_proc` package includes depth image related tools. This includes converting 16-bit UInt to 32-bit float, generating point cloud, aligning RGB-D.

#### ROS-Depth Camera Integration and Simulation

In the robot description `robot.urdf.xacro`, add another xacro file for depth camera in place of the Camera Xacro.

##### Depth Camera Xacro

```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" >

    <joint name="camera_joint" type="fixed">
        <parent link="chassis"/>
        <child link="camera_link"/>
        <origin xyz="0.305 0 0.08" rpy="0 0 0"/>
    </joint>

    <link name="camera_link">
        <visual>
            <geometry>
                <box size="0.010 0.03 0.03"/>
            </geometry>
            <material name="red"/>
        </visual>
    </link>


    <joint name="camera_optical_joint" type="fixed">
        <parent link="camera_link"/>
        <child link="camera_link_optical"/>
        <origin xyz="0 0 0" rpy="${-pi/2} 0 ${-pi/2}"/>
    </joint>

    <link name="camera_link_optical"></link>



    <gazebo reference="camera_link">
        <material>Gazebo/Red</material>

        <sensor name="camera" type="depth">
            <pose> 0 0 0 0 0 0 </pose>
            <visualize>true</visualize>
            <update_rate>10</update_rate>
            <camera>
                <horizontal_fov>1.089</horizontal_fov>
                <image>
                    <format>B8G8R8</format>
                    <width>640</width>
                    <height>480</height>
                </image>
                <clip>
                    <near>0.05</near>
                    <far>8.0</far>
                </clip>
            </camera>
            <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
                <frame_name>camera_link_optical</frame_name>
                <min_depth>0.1</min_depth>
                <max_depth>100.0</max_depth>
            </plugin>
        </sensor>
    </gazebo>

</robot>
```

Since we added a new file, build and source the workspace.

```bash
colcon build --symlink-install
source install/setup.bash
```
Run gazebo launcher and `rviz2`, add `point cloud`, select `/camera/points` topic to view.


#### Connecting a Real Depth Camera and Getting Data
`lsusb` to check if depth camera is connected via USB. Install drivers.

---

## Chassis Design
### Bench test components
Check if Pi is undervoltaged:
```bash
vcgencmd get_throttled # 0X0 is not throttled
```
If the Pi is getting low-voltage, probe in key connections (regulator, terminal, Pi pins) to find where the drop is occuring.

Connect all the components (motors, camera, LiDAR) and see if they work.

`journalctl -fe` checks if the Pi is looking for a display continuously. `systemctl get-default` shows the default startup target (e.g., graphical target). `systemctl set-default multi-user.target` to change, and `systemctl set-default graphical.target` to swap back > `reboot`.

Clone and build workspace > Chassis design


---

## Control
### ROS2 Control

Fast common framework between drivers for hardwares and control algorithms.

The center of ros2 control is **Controller manager**, links controllers and drivers. It has **hardware interfaces** or hardware components that speaks to the hardware and exposes them to controller. Hardwares are represented with **command interfaces (read/write)** and **state interfaces (real only)**.  An actuator can have multiple command interfaces, e.g., it can be controlled by either speed or torque.For motors, we can only control it, making it a command interface. But we can monitor the speed, position with encoders, making them state interfaces. For the two motors, we have two command interfaces (one for velocity of each motor), and four state interfaces (position and velocity of each wheel).  

With motors and their hardware interfaces loaded, `ros2 control list_hardware_interfaces` returns command and state interfaces. ROS2 control doesn't know or care which one does what. **Resource Manager** takes all command and state interfaces and publishes as a list, accessible by the controllers. The URDF mentions which interfaces are connected to which part of the hardware.  

**Controllers**: are how we interact with the robot. On one end, they listen to ros_topics for sensed data, do some calculations, and send output to hardware interfaces exposed by the resource manager. While the hardware interfaces is designed for specific hardwares, the controllers are designed for robot applications. ROS2 control packages has built in controllers for common needs, like the `diff_drive_controller` for differential drive robot. Controllers can be input-only, output-only or both. 

**Control Manager and Controllers**: The controller manager matches controllers with the right command and state interfaces the resource manager is exposing. To set up the controller, we write a yaml file with parameters, and pass that to the controller manager. From there we can tell it to start/stop controller as needed. We can have multiple controllers in one robot - as long as they are not trying to control the same command interface (real-only state interfaces can be shared).  

**Setting up Controller Manager**: With hardware and controllers, we can write node and have controller manager running inside it, or more usually, use node provided for us. In either way, we need to provide hardware info, usually with URDF, and controller info, usually with yaml file. 

**Interacting with Controller Manager**:
- The controller manager has *services* to access the functionalities
- ros2control command line tool (CLI): makes these service calls easier. 
- Nodes/scripts: can run key functions.

On the dev machine:
```bash
sudo apt install ros-${ROS_DISTRO}-ros2-control ros-${ROS_DISTRO}-ros2-controllers ros-${ROS_DISTRO}-gz-ros2-control
```

#### Setting up ROS2 Control

In the robot description `robot.urdf.xacro`, add another xacro file for ros2 control and replace `gazebo_control` with it.

##### ROS2 Control Xacro

```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">

    <xacro:unless value="$(arg sim_mode)">
        <ros2_control name="RealRobot" type="system">
        <!-- Other than system, we can use "sensor" and "actuator" for s single  sensor or actuator-->
            <hardware>
            <!-- Plugins are the hardware interfaces -->
                <plugin>diffdrive_arduino/DiffDriveArduinoHardware</plugin>
                <!-- The joint names are from our robot URDF -->
                <param name="left_wheel_name">left_wheel_joint</param>
                <param name="right_wheel_name">right_wheel_joint</param>
                <param name="loop_rate">30</param>
                <param name="device">/dev/ttyUSB0</param>  <!-- The USB device needs to be udpated to differential between the arduino and the LiDAR-->
                <param name="baud_rate">57600</param>
                <param name="timeout_ms">1000</param> <!-- 1 second -->
                <param name="enc_counts_per_rev">3436</param>
            </hardware>
            <joint name="left_wheel_joint">
            <!-- define motor command interface of velocity and state interfaces of position and velocity-->
                <command_interface name="velocity">
                    <param name="min">-10</param>
                    <param name="max">10</param>
                </command_interface>
                <state_interface name="position"/>
                <state_interface name="velocity"/>
            </joint>
            <joint name="right_wheel_joint">
                <command_interface name="velocity">
                    <param name="min">-10</param>
                    <param name="max">10</param>
                </command_interface>
                <state_interface name="position"/>
                <state_interface name="velocity"/>
            </joint>
        </ros2_control>
    </xacro:unless>

    <xacro:if value="$(arg sim_mode)">
        <ros2_control name="GazeboSystem" type="system">
            <hardware>
                <plugin>gz_ros2_control/GazeboSimSystem</plugin>
            </hardware>
            <joint name="left_wheel_joint">
                <command_interface name="velocity">
                    <param name="min">-10</param>
                    <param name="max">10</param>
                </command_interface>
                <state_interface name="velocity"/>
                <state_interface name="position"/>
            </joint>
            <joint name="right_wheel_joint">
                <command_interface name="velocity">
                    <param name="min">-10</param>
                    <param name="max">10</param>
                </command_interface>
                <state_interface name="velocity"/>
                <state_interface name="position"/>
            </joint>
        </ros2_control>
    </xacro:if>

    <gazebo>
    <!-- Has its own controller manager, that takes URDF from state_publisher, but controler yaml needs to be passed -->
        <plugin name="gz_ros2_control::GazeboSimROS2ControlPlugin" filename="libgz_ros2_control-system.so">
            <parameters>$(find articubot_one)/config/my_controllers.yaml</parameters>
            <!-- path to the controller yaml -->
            <parameters>$(find articubot_one)/config/gaz_ros2_ctl_use_sim.yaml</parameters>
        </plugin>
    </gazebo>

</robot>
```
We'll write a controllers yaml file in the config folder.

```yaml
controller_manager:
  ros__parameters:
    update_rate: 30
    # use_sim_time: true

    diff_cont:
      type: diff_drive_controller/DiffDriveController

    joint_broad:
      type: joint_state_broadcaster/JointStateBroadcaster

diff_cont:
  ros__parameters:

    publish_rate: 30.0

    base_frame_id: base_link

    left_wheel_names: ['left_wheel_joint']
    right_wheel_names: ['right_wheel_joint']
    wheel_separation: 0.297
    wheel_radius: 0.033

    # use_stamped_vel: false

    # open_loop: false    

    # wheels_per_side: x
    # wheel_separation_multiplier: x
    # left_wheel_radius_multiplier: x
    # right_wheel_radius_multiplier: x

    # odom_frame_id: x
    # pose_covariance_diagonal: x
    # twist_covariance_diagonal: x
    # open_loop: x
    # enable_odom_tf: x

    # cmd_vel_timeout: x
    # publish_limited_velocity: x
    # velocity_rolling_window_size: x
    

    # linear.x.has_velocity_limits: false
    # linear.x.has_acceleration_limits: false
    # linear.x.has_jerk_limits: false
    # linear.x.max_velocity: NAN
    # linear.x.min_velocity: NAN
    # linear.x.max_acceleration: NAN
    # linear.x.min_acceleration: NAN
    # linear.x.max_jerk: NAN
    # linear.x.min_jerk: NAN

    # angular.z.has_velocity_limits: false
    # angular.z.has_acceleration_limits: false
    # angular.z.has_jerk_limits: false
    # angular.z.max_velocity: NAN
    # angular.z.min_velocity: NAN
    # angular.z.max_acceleration: NAN
    # angular.z.min_acceleration: NAN
    # angular.z.max_jerk: NAN
    # angular.z.min_jerk: NAN




# joint_broad:
#   ros__parameters:
```
Build and source the installation. Now launch Gazebo, and check hardware interfaces with `ros2 control list hardware_interfaces`. 

#### Starting controllers

```bash
ros2 run controller_manager spawner.py diff_cont
ros2 run controller_manager spawner.py joint_broad
```

Now teleop is not going to work, as the controller is expecting command velocity from `/diff_cont/cmd_vel_unstamped`, and not `/cmd_vel`. So we need to map it using

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
```

The diff_drive_spawner can be added in the launcher files.

```python
diff_drive_spawner = Node(
    package="controller_manager",
    executable="spawner",
    arguments=["diff_cont"],
)

joint_broad_spawner = Node(
    package="controller_manager",
    executable="spawner",
    arguments=["joint_broad"],
)
```

#### Extra bits
##### Gazebo lag
Add an extra gazebo parameters file and add it in the launcher.
```python
# Include the Gazebo launch file, provided by the ros_gz_sim package
gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
                launch_arguments={'gz_args': ['-r -v4 ', world], 'on_exit_shutdown': 'true'}.items()
            )
```
##### Wheel friction and rviz2 lag
Make the wheel collision into sphere geometry to reduce friction.

##### Object scan move around for simulation
Use gazebo_control instead of ros2 control. In the `robot.urdf.xacro`, use a conditional:

```xml
<xacro:if value="$(arg use_ros2_control)">
    <xacro:include filename="ros2_control.xacro" />
</xacro:if>
<xacro:unless value="$(arg use_ros2_control)">
    <xacro:include filename="gazebo_control.xacro" />
</xacro:unless>
```

Update `rsp.launch.py`.

### Driving Actual Robot using ROS2 Control

We have our physical robot on one side, and the command velocity to be published by a nav stack on another side. Command velocity is of type `Twist` or `TwistStamped`, a 6-d velocity including `linear.x`, `linear.y`, `linear.z`, `angular.x`, `angular.y`, `angular.z`. But for a differential drive robot, we'll only use `linear.x`, `angular.z`. `ros2_control` will link the `/cmd_vel` to the actual motors.  

`ros2_control` has 3 main parts - a controller manager that links diff drive controller to hardware interface. `ros2_control` provides the controller manager - `ros2_control_node`, the diff drive controller - `diff_drive_controller` (although we could write one), we write the hardware interface plugin - `diffdrive_arduino`. The `diff_drive_controller` converts the `/cmd_vel` into required motor velocity, and the `diffdrive_arduino` converts the abstract motor velocity into hardware commands, the `ros2_control_node` links the `diff_drive_controller` and `diffdrive_arduino`.

We also have a controller manager `joint_state_broadcaster` that reads motor encoder position state provided by the hardware interface, and publishes them in the `/joint_states` topic. For the robot state publisher to generate transforms.

The last section discusses setting up controller manager and hardware interfaces for gazebo. This section deals with setting up controller manager and hardware interfaces for the real robot.

#### Setting up controller manager
If you use the arduino code provided, youcan use the hardware interface `diffdrive_arduino` discussed here. It exposes the two command interfaces (velocities) and four state interfaces (velocities, positions), and uses the same serial commands to drive the motors. Control will use the `diff_drive_controller` used for Gazebo.

Right now, the custom hardware interface can't be installed using apt, we'll have to build from source. 

On the Pi:

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y \
  ros-${ROS_DISTRO}-twist-mux \
  ros-${ROS_DISTRO}-twist-stamper \
  ros-${ROS_DISTRO}-ros2-control \
  ros-${ROS_DISTRO}-ros2-controllers \
  ros-${ROS_DISTRO}-gz-ros2-control \
  ros-${ROS_DISTRO}-ros-gz

# sudo apt install ros-${ROS_DISTRO}-ros2-control ros-${ROS_DISTRO}-ros2-controllers ros-${ROS_DISTRO}-gazebo-ros2-control

sudo apt install libserial-dev
cd <workspace>/src
git clone https://github.com/joshnewans/diffdrive_arduino
git clone https://github.com/joshnewans/serial
cd ../..
colcon build --symlink-install
source install/setup.bash
```
Connect to the Pi using vscode remote host (ssh) to udpate the `ros2_control.xacro` and to create/update `launch_robot.launch.py`.

The controller manager needs two things: the robot URDF that includes information to load the hardware interfaces, and a params file that includes information to load the controllers. For the URDF, we'll edit the `launch_robot.launch.py` launcher. We'll include the library `from launch.substitution import Command`, and add a command substitution `robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])`, that is going to execute a command that asks `robot_state_publisher` node to return its `robot_description` parameters as a string.

We'll add a `controller_manager` node with the same `controller_manager` package, but with the executable `ros2_control_node`, and some parameters.

```python
robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])

controller_params_file = os.path.join(get_package_share_directory(package_name),'config','my_controllers.yaml')

controller_manager = Node(
    package="controller_manager",
    executable="ros2_control_node",
    parameters=[{'robot_description': robot_description}, # for urdf (hardware interface)
                controller_params_file] # for params (controllers)
)
```

Now this will launch `ros2_control` node, it'll set robot description parameter to what `robot_description` returns, and set the controller parameters from the yaml file.

```python
# delays running the controller manager by 3 seconds for the parameters to complete loading.
from launch.actions import TimerAction
delayed_controller_manager = TimerAction(period=3.0, actions=[controller_manager])

# waits for the controller_manager to start, then starts `diff_drive_spawner
from launch.event_handlers import OnProcessStart

diff_drive_spawner = Node(
    package="controller_manager",
    executable="spawner",
    arguments=["diff_cont"],
)

delayed_diff_drive_spawner = RegisterEventHandler(
    event_handler=OnProcessStart(
        target_action=controller_manager,
        on_start=[diff_drive_spawner],
    )
)

joint_broad_spawner = Node(
    package="controller_manager",
    executable="spawner",
    arguments=["joint_broad"],
)

delayed_joint_broad_spawner = RegisterEventHandler(
    event_handler=OnProcessStart(
        target_action=controller_manager,
        on_start=[joint_broad_spawner],
    )
)


# Launch them all!
return LaunchDescription([
    rsp,
    # joystick,
    twist_mux,
    delayed_controller_manager,
    delayed_diff_drive_spawner,
    delayed_joint_broad_spawner
])
```

#### Testing the real robot
- Initial test: Drive it with teleop and compare with rviz.
- Encoder counts per revolution: Rotate the wheels, and check alignment with rviz transforms.
- Wheel radius: Drive the robot 1m, and check if it aligns with rviz. You can update the value in URDF and in `my_controllers.yaml`.
- Wheel seperation: rotate the robot 1 circle, check alignment with rviz. You can update the value in URDF and in `my_controllers.yaml`.

Check the camera by launcing it in the Pi:
```bash
# source workspace
ros2 launch articubot_one camera.launch.py
```

Check the lidar by launcing it in the Pi:
```bash
# source workspace
ros2 launch articubot_one rplidar.launch.py
```

#### Switch real and gazebo controller manager

```xml
<xacro:arg name="sim_mode" default="false"/>
```

On the `ros2_control.xacro` file, put the real robot control tag inside xacro:unless, and gazebo control tag inside if:
```xml
<xacro:unless value="$(arg sim_mode)">
    <ros2_control name="RealRobot" type="system">...</ros2_control>
</xacro:unless>

<xacro:if value="$(arg sim_mode)">
    <ros2_control name="GazeboSystem" type="system">...</ros2_control>
</xacro:if>
```

### Wireless Control

```bash
cd dev_ws/
sudo apt install joystick jstest-gtk evtest
evtest # typing event number will enable testing the gamepad in Linux
```
Linux Joystick Driver > Joy Node (talks to Linux driver) > /joy (topic sensor messages /joy - list of buttons and axis values we're pressing) > teleop_twist_joy (message) > /cmd_vel

```bash
ros2 run joy joy_enumerate_devices # shows plugged in controllers
ros2 run joy joy_node # run joy node
```

On a new terminal
```bash
ros2 topic echo /joy # pressing controller should print topic
```

`joystick.launch.py` launcher runs node `joy_node` of package `joy`, and passes parameters from `joystick.yaml` in `config` directory.

```yaml
joy_node:
  ros_parameters:
    device_id: 0
    deadzone: 0.05
    autorepeat_rate: 20.0
```

colcon build, run launcher, run test.

Now we'll generate twist message from joy input. We'll use `teleop_twist_joy` node to do this. We'll add this to the launch file. The package is `teleop_teist_joy`, the executable is `teleop_node`, and give it a name, pass the same params file, and run it in the launch description.

In joystick.yaml
```yaml
teleop_node:
  ros_parameters:
    axis_linear:
      x: 1 # the axis button ID
    scale_linear: # speed in x direction when we push the button to the limit
      x: 0.5 # m/s
    scale_linear_turbo:
      x: 1.0 # m/s in turbo mode

    axis_angular:
      yaw: 0
    scale_angular: # angular speed
      yaw: 0.5 # rad/s
    scale_angular_turbo:
      yaw: 1.0 # rad/s in turbo mode

    enable_button: 6
    enable_turbo_button: 7

    require_enable_button: true # dead man's switch enable - if you don't press 6/7, it'll send 0 m/s
```

Build and relaunch, run `ros2 topic echo /cmd_vel`, and now joystick input should publish `/cmd_vel`. In the launcher file, we'll add remapping in teleop_node from `/cmd_vel` to `/diff_cont/cmd_vel_unstamped`.

#### Getting feedback using rviz2
Launch rviz2.

ssh into your robot and launch camera launcher to get image feedback in rviz or rqt.

ssh into the robot and launch LiDAR launcher

### Phone Control

---

## SLAM
Simultaneous Localization And Mapping.
GridSLAM using 2D LiDAR.

Localization is placing concepts on map. If we don't have GPS to start with, we can use SLAM to both localize and update our map. Two major approaches are `feature or landmark` slam and `grid slam`. Feature slam detects objects in our map. Grid slam divides the area into grids, and each are occupied or unoccupied.


### ROS and SLAM
We can set our fixed frame in rviz to `odom`, which represents the robot's world origin. And the transform from odom to `base_link` is calculated by the differential drive controller using the wheel odometry. But odometry drifts away from the truth slowly over time, as it integrates velocity to estimate position (dead reckoning), which compunds error.  
GPS/SLAM can correct these errors. But using them to correct odom can result in transporting base_link. Instead we use a `map` link instead of `odom`. And the final output combines two.  
In addition to `odom` and `map` frames, we have `odom` and `map` topics that contain data of odometry (`nav_msgs/msg/Odometry`: contains position info of odom->base_link TF and velocity) and map (`nav_msgs/msg/OccupancyGrid`: contains grid map occupancy data).  

`base_footprint` is a like a 2D shadow of `base_link` stuck on the ground - used for 2D SLAM algorithms. `Pose` means the position and orientation of robot (same as robot's transform frame).  

You can find more info on coordinate frames in **REP 105 - Coordinate Frames for Mobile Platforms** and **REP 120 - Coordinate Frames for Humanoid Robots**.  

Now we'll add `base_footprint` link in our `robot_core.xacro` file under the `base_link`.

We'll also install:
```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y ros-${ROS_DISTRO}-slam-toolbox
```
SLAM toolbox has many modes. We'll use -
- `Online`: working on a live data stream rather than recorded logs.
- `Asynchronous`: always process the latest scan to avoid lagging, even if it skips scans.

SLAM toolbox comes with launcher and param files - we'll copy a params file in our directory.

```bash
cp /opt/ros/${ROS_DISTRO}/share/slam_toolbox/config/mapper_params_online_async.yaml dev_ws/src/bluebot_one/config/
```
Go to workspace > Rebuild with colcon > source workspace > launch simulation launcher and rviz. If you drive your robot and come back to the origin, you'll find it has drifted away in rviz. Restart gazebo and rviz, and in a new terminal:

```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/bluebot_one/config/mapper_params_online_async.yaml use_sim_time:=true 
```

In rviz, add map and set topic to `\map`, and change the Fixed Frame to `map` (this'll make the map steady, while the robot can jump around). Now driving the robot will udpate the map. You can change your view from Orbit (rviz default) to TopDownOrthographic. Now, returning to the map origin will land it very close to origin in Gazebo, while the odom has drifted.

Running `ros2 service list` shows options to save map. But it also has a rviz plugin (Panels Tab > Add new Panel > SlamToolboxPlugin). You can use `Save Map` to save it in old format, and `Serialize Map` to save map that can be used with `slam_toolbox`. Go to the `mapper_params_online_async.yaml` file and change `mode: localization`. For `map_file_name: `, write the path to the saved map (e.g., `/home/dev/dev_ws/my_map_serial`). Set `map_start_at_dock` to `true`. Then rerun the `slam_toolbox`.  

Once we've built our map, we can use it with other systems like the AMCL (Adaptive Monte Carlo Localisation).  

Now install Nav2 from the [Getting Started with Nav2](https://docs.nav2.org/getting_started/index.html).

We'll now start a `map_server` node that take the saved map and makes it avaiable as `/map` topic. We'll run
```bash
ros2 run nav2_map_server map_serve --ros-args -p yaml_file_name:=my_map_save.yaml -p use_sim_time:=true
```
In a new tab
```bash
ros2 run nav2_util lifecycle_bringup map_server
```

After rerunning gazebo, rviz, we can set rviz > map > Topic> Reliability to Reliable and Durability Policy to Transient Local. To localize our robot we'll run amcl in a new tab
```bash
ros2 run nav2_amcl amcl --ros-args -p use_sim_time:=true
```
In a new tab run lifecycle bringup with amcl
```bash
ros2 run nav2_util lifecycle_bringup amcl
```
Now we'll use 2D Pose Estimate on rviz to localize the robot.

### Running on real robot
On the Pi
```bash
ros2 launch bluebot_one launch_robot.launch.py
```

In another tab
```bash
ros2 launch bluebot_one rplidar.launch.py
```

Now we'll run `slam_toolbox` on the dev machine
```bash
ros2 launch slam_toolbox online_async_launch.py params_file:=./src/bluebot_one/config/mapper_params_online_async.yaml use_sim_time:=false 
```

Wait for the map to appear, and change the fixed frame to map. You can also run `slam_toolbox` on the robot to reduce latency.

---

## Nav2

---

## Additional Hardware

---

## Humble

---

## New Gazebo

---