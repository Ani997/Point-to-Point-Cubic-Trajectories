# Point-to-Point-Cubic-Trajectories
Implements a ROS package which automatically generates point to point cubic trajectories connecting pairs of randomly generated points

To run the package, please follow the following given steps:
1) Download the package into the catkin workspace by unzipping the file.

2) Next, we will issue the "catkin_make" command in the terminal.

3) Once we are done creating the catkin workspace, we will have to make the Python scripts executable. This can be done by navigating to the     folder(catkin_ws/src/AR_week4_test/scripts) using the "cd" function in the terminal and then issuing the command "chmod +x program.py". We will do this process for all the 4 scripts that have been written. Close the terminal.

4) Now open a new terminal, issue the following commands: "cd catkin_ws", "source ./devel/setup.bash", "roslaunch AR_week4_test cubic_traj_gen.launch" one after the other. The "cubic_traj_gen.launch" file will enable us to run the 4 python scripts sequentially.

5) Now opening a new terminal, and issuing the command "rosrun rqt_graph rqt_graph", we will be able to see a visual representation of how the package works.
