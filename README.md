# Awesome Movement Primitives
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Links to software implementations of movement primitive (MP) frameworks and core papers, including:
dynamic MPs,
probabilistic MPs,
kernelized MPs,
contextual neural MPs,
fourier MPs,
and other methods.

## Table of Contents
 - [Dynamic Movement Primitives](#dynamic-movement-primitives)
 - [Probabilistic Movement Primitives](#probabilistic-movement-primitives)
 - [Kernelized Movement Primitives](#kernelized-movement-primitives)
 - [Contextual Neural Movement Primitives](#contextual-neural-movement-primitives)
 - [Fourier Movement Primitives](#fourier-movement-primitives)
 - [Other Approaches](#other-approaches)
 - [Citing This Work](#citing-this-work)


## Dynamic Movement Primitives

### Software
[studywolf/pydmps](https://github.com/studywolf/pydmps): Tutorial and applications with minimal library dependencies. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/studywolf/pydmps?style=social)](https://github.com/studywolf/pydmps/stargazers/)

[stulp/dmpbbo](https://github.com/stulp/dmpbbo): Combines Black-box optimization (BBO) with DMPs. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/stulp/dmpbbo?style=social)](https://github.com/stulp/dmpbbo/stargazers/)

[sniekum/dmp](https://github.com/sniekum/dmp): Robot-agnostic implementation for ROS. 

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/sniekum/dmp?style=social)](https://github.com/sniekum/dmp/stargazers/) 

[dfki-ric/movement_primitives](https://github.com/dfki-ric/movement_primitives): Various MP frameworks including DMPs (with spatially coupled support) and ProMPs. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/dfki-ric/movement_primitives?style=social)](https://github.com/dfki-ric/movement_primitives/stargazers/)

[chauby/PyDMPs_Chauby](https://github.com/chauby/PyDMPs_Chauby): Implementation for simulated UR5 robot in CoppeliaSim (V-REP).

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/chauby/PyDMPs_Chauby?style=social)](https://github.com/chauby/PyDMPs_Chauby/stargazers/)

[AlexanderFabisch/PyDMP](https://github.com/AlexanderFabisch/PyDMP): Illustrative notebooks for understanding concepts.

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/AlexanderFabisch/PyDMP?style=social)](https://github.com/AlexanderFabisch/PyDMP/stargazers/)

[mginesi/dmp_pp](https://github.com/mginesi/dmp_pp):  Library based on "Overcoming some drawbacks of DMPs" paper.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/mginesi/dmp_pp?style=social)](https://github.com/mginesi/dmp_pp/stargazers/)

[suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics](https://github.com/suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics):  Short implementation in matlab.

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics?style=social)](https://github.com/suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics/stargazers/)

[abakisita/ros_dmp](https://github.com/abakisita/ros_dmp): Package with services for learning motion and generating from leart DMP. 

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/abakisita/ros_dmp?style=social)](https://github.com/abakisita/ros_dmp/stargazers/)

[mginesi/dmp_vol_obst](https://github.com/mginesi/dmp_vol_obst): Appended secondary forcing term for obstacle avoidance. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/mginesi/dmp_vol_obst?style=social)](https://github.com/mginesi/dmp_vol_obst/stargazers/)

[ferreirafabio/movement_primitives_via_optimization](https://github.com/ferreirafabio/movement_primitives_via_optimization): Incorporates Lagrangian optimization for adapting to demonstrations. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/ferreirafabio/movement_primitives_via_optimization?style=social)](https://github.com/ferreirafabio/movement_primitives_via_optimization/stargazers/)

[varadVaidya/dmp](https://github.com/varadVaidya/dmp): Secondary forcing term for single and multi-point obstacle avoidance. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/varadVaidya/dmp?style=social)](https://github.com/varadVaidya/dmp/stargazers/)

[liangyuwei/dual_ur5_arm](https://github.com/liangyuwei/dual_ur5_arm): Dual-arm peg-in-hole task with UR5 robots. 

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/liangyuwei/dual_ur5_arm?style=social)](https://github.com/liangyuwei/dual_ur5_arm/stargazers/)

[baggepinnen/DynamicMovementPrimitives.jl](https://github.com/baggepinnen/DynamicMovementPrimitives.jl): Standard formulation and implementation of 2DoF control for trajectory tracking and perturbation recovery.  

![Julia](https://img.shields.io/badge/-Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white)
[![GitHub stars](https://img.shields.io/github/stars/baggepinnen/DynamicMovementPrimitives.jl?style=social)](https://github.com/baggepinnen/DynamicMovementPrimitives.jl/stargazers/)

[awesomebytes/dmp_gestures](https://github.com/awesomebytes/dmp_gestures): Use cameras to capture gestures to learn and generate DMPs executed through MoveIt!. 

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/awesomebytes/dmp_gestures?style=social)](https://github.com/awesomebytes/dmp_gestures/stargazers/)

[CarlDegio/PI2-DMPs](https://github.com/CarlDegio/PI2-DMPs): Reinforcement learning via Policy Improvement with Path Integrals (PI2) 

![matlab](https://img.shields.io/badge/matlab-%20-blue)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/CarlDegio/PI2-DMPs?style=social)](https://github.com/CarlDegio/PI2-DMPs/stargazers/)

[tsitsimis/dmpling](https://github.com/tsitsimis/dmpling): Trajectories learned from human gestures (3D marker poses) with notebook visualizations.

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/tsitsimis/dmpling?style=social)](https://github.com/tsitsimis/dmpling/stargazers/)

[heracleia/pyrdmp](https://github.com/heracleia/pyrdmp): Reinforcement learning library based on the PoWER algorithm.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/heracleia/pyrdmp?style=social)](https://github.com/heracleia/pyrdmp/stargazers/)

[Dennis-BIRL-GDUT/baxter_dmp_rl](https://github.com/Dennis-BIRL-GDUT/baxter_dmp_rl):  Workspace for ROS implementation of Baxter pick-and-place.

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/Dennis-BIRL-GDUT/baxter_dmp_rl?style=social)](https://github.com/Dennis-BIRL-GDUT/baxter_dmp_rl/stargazers/)

[chauby/DMP_chebotar](https://github.com/chauby/DMP_chebotar): Implementation supports goal location updates.

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/chauby/DMP_chebotar?style=social)](https://github.com/chauby/DMP_chebotar/stargazers/)

[carlos22/pydmp](https://github.com/carlos22/pydmp): Educational implementation of 1D discrete DMP. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/carlos22/pydmp?style=social)](https://github.com/carlos22/pydmp/stargazers/)

[dgerod/more-dmps](https://github.com/dgerod/more-dmps): Implementation on three other python DMP libraries. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/dgerod/more-dmps?style=social)](https://github.com/dgerod/more-dmps/stargazers/)

[mathiasesn/obstacle_avoidance_with_dmps](https://github.com/mathiasesn/obstacle_avoidance_with_dmps): Incorporates obstacle avoidance and link-collision avoidance.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/mathiasesn/obstacle_avoidance_with_dmps?style=social)](https://github.com/mathiasesn/obstacle_avoidance_with_dmps/stargazers/)

[dkebude/DMP-gen](https://github.com/dkebude/DMP-gen): DMP generator for reinforcement learning applications.

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/dkebude/DMP-gen?style=social)](https://github.com/dkebude/DMP-gen/stargazers/)

[stulp/dmp_bbo_matlab_deprecated](https://github.com/stulp/dmp_bbo_matlab_deprecated): Black-box optimization with DMPs. 

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/stulp/dmp_bbo_matlab_deprecated?style=social)](https://github.com/stulp/dmp_bbo_matlab_deprecated/stargazers/)

[cloudy/dmp-obstacle-avoidance](https://github.com/cloudy/dmp-obstacle-avoidance):  Human obstacle avoidance demonstrated on Rethink Robotics Sawyer manipulator.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/cloudy/dmp-obstacle-avoidance?style=social)](https://github.com/cloudy/dmp-obstacle-avoidance/stargazers/)

[abakisita/dmp_motion](https://github.com/abakisita/dmp_motion): Pre-cursor implementation to author's ROS package.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/abakisita/dmp_motion?style=social)](https://github.com/abakisita/dmp_motion/stargazers/)

[shobhit6993/egraphs-with-dmp](https://github.com/shobhit6993/egraphs-with-dmp): DMPs are integrated into experience-graph framework to support adaptation to unseen obstacles.

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/shobhit6993/egraphs-with-dmp?style=social)](https://github.com/shobhit6993/egraphs-with-dmp/stargazers/)

[xukechun/DMPs-learning](https://github.com/xukechun/DMPs-learning): Visualizer for DMPs with RViz. 

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/xukechun/DMPs-learning?style=social)](https://github.com/xukechun/DMPs-learning/stargazers/)

[baxter-flowers/dmp_lib](https://github.com/baxter-flowers/dmp_lib): Wraps @studywolf implementation in ROS package.

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/baxter-flowers/dmp_lib?style=social)](https://github.com/baxter-flowers/dmp_lib/stargazers/)

[yuehuang315/LIL-DMP](https://github.com/yuehuang315/LIL-DMP): Lifelong imitation learning with DMPs.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/yuehuang315/LIL-DMP?style=social)](https://github.com/yuehuang315/LIL-DMP/stargazers/)

[gsutanto/dmp](https://github.com/gsutanto/dmp): Reference implementation in three languages with hard real-time support for robot control (C++).

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/gsutanto/dmp?style=social)](https://github.com/gsutanto/dmp/stargazers/)

[Shaluols/ur5e_dmp](https://github.com/Shaluols/ur5e_dmp): Leverages UR5e Gazebo simulation to learn DMPs based on @studywolf's library.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/Shaluols/ur5e_dmp?style=social)](https://github.com/Shaluols/ur5e_dmp/stargazers/)

[Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree](https://github.com/Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree): Use behavior trees and DMPs for upper-level task planning.

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree?style=social)](https://github.com/Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree/stargazers/)

[herambnemlekar/dmp-handovers](https://github.com/herambnemlekar/dmp-handovers): Preditive human-robot handovers using DMPs on the Baxter robot.

![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/herambnemlekar/dmp-handovers?style=social)](https://github.com/herambnemlekar/dmp-handovers/stargazers/)

[AlpX/DMP-LWR](https://github.com/AlpX/DMP-LWR): Reference implementation in matlab using locally weighted regression. 

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/AlpX/DMP-LWR?style=social)](https://github.com/AlpX/DMP-LWR/stargazers/)

[kostasVlachos/dmp_control](https://github.com/kostasVlachos/dmp_control): DMP control for Kuka robot.

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/kostasVlachos/dmp_control?style=social)](https://github.com/kostasVlachos/dmp_control/stargazers/)

[alaradirik/robot-learning](https://github.com/alaradirik/robot-learning): Algorithms from university course implemented in numpy.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/alaradirik/robot-learning?style=social)](https://github.com/alaradirik/robot-learning/stargazers/)

[zhouyou-kit/dmp_exercise](https://github.com/zhouyou-kit/dmp_exercise): Educational visualization based on Peter Corke's matlab robotics toolbox.

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/zhouyou-kit/dmp_exercise?style=social)](https://github.com/zhouyou-kit/dmp_exercise/stargazers/)

[ZhengYi0310/dmp-ros-pkg](https://github.com/ZhengYi0310/dmp-ros-pkg): DMP implementation for PR2 and WAM robots.

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/ZhengYi0310/dmp-ros-pkg?style=social)](https://github.com/ZhengYi0310/dmp-ros-pkg/stargazers/)

[justagist/reversible_dmp](https://github.com/justagist/reversible_dmp):  Implements reversible discrete DMP.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/justagist/reversible_dmp?style=social)](https://github.com/justagist/reversible_dmp/stargazers/)

[emarescotti/VelocityPlanning_DMP_FL](https://github.com/emarescotti/VelocityPlanning_DMP_FL): Velocity planning of robotic sealing tasks using DMPs.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/emarescotti/VelocityPlanning_DMP_FL?style=social)](https://github.com/emarescotti/VelocityPlanning_DMP_FL/stargazers/)

[ZhengYi0310/DMP](https://github.com/ZhengYi0310/DMP): Implementation in two languages.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/ZhengYi0310/DMP?style=social)](https://github.com/ZhengYi0310/DMP/stargazers/)

[MichailTheofanidis/dmp-protoype](https://github.com/MichailTheofanidis/dmp-protoype): Experimental implementation of reinforcement-learning based adaptation and robot inverse kinematics.

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/MichailTheofanidis/dmp-protoype?style=social)](https://github.com/MichailTheofanidis/dmp-protoype/stargazers/)

[cunnia3/Dynamic-Motion-Primitives](https://github.com/cunnia3/Dynamic-Motion-Primitives): Implementation based on @studywolf DMP.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/cunnia3/Dynamic-Motion-Primitives?style=social)](https://github.com/cunnia3/Dynamic-Motion-Primitives/stargazers/)

[nag92/dmp_experiments](https://github.com/nag92/dmp_experiments):  Experimental implementation in two languages.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/nag92/dmp_experiments?style=social)](https://github.com/nag92/dmp_experiments/stargazers/)

[Slifer64/resnet_dmp](https://github.com/Slifer64/resnet_dmp): Uses RGB images with resnet network architecture to learn DMPs for planar tasks.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/Slifer64/resnet_dmp?style=social)](https://github.com/Slifer64/resnet_dmp/stargazers/)


## Probabilistic Movement Primitives
[dfki-ric/movement_primitives](https://github.com/dfki-ric/movement_primitives): Various MP frameworks including DMPs (with spatially coupled support) and ProMPs. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/dfki-ric/movement_primitives?style=social)](https://github.com/dfki-ric/movement_primitives/stargazers/)

[sebasutp/promp](https://github.com/sebasutp/promp):  Library that computes trajectory likelihood of ProMP, trajectory sampling, and save/load.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/sebasutp/promp?style=social)](https://github.com/sebasutp/promp/stargazers/)

[baxter-flowers/promplib](https://github.com/baxter-flowers/promplib): Features interactive learning componenet to automatically cluster primitives based on standard deviation.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/baxter-flowers/promplib?style=social)](https://github.com/baxter-flowers/promplib/stargazers/)

[mjm522/promps_python](https://github.com/mjm522/promps_python): 1D ProMP model with closed-form trajectory controller.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/mjm522/promps_python?style=social)](https://github.com/mjm522/promps_python/stargazers/)

[sebasutp/promp-cpp](https://github.com/sebasutp/promp-cpp): C++ version of @sebasutp python library.

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) 
[![GitHub stars](https://img.shields.io/github/stars/sebasutp/promp-cpp?style=social)](https://github.com/sebasutp/promp-cpp/stargazers/)

[herambnemlekar/probabilistic-movement-primitives](https://github.com/herambnemlekar/probabilistic-movement-primitives): Experimental implementation for training ProMPs with the Baxter robot. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/herambnemlekar/probabilistic-movement-primitives?style=social)](https://github.com/herambnemlekar/probabilistic-movement-primitives/stargazers/)

## Kernelized Movement Primitives
[yanlongtu/robInfLib-matlab](https://github.com/yanlongtu/robInfLib-matlab): Demonstrates various functionalities of KMPs. 

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/yanlongtu/robInfLib-matlab?style=social)](https://github.com/yanlongtu/robInfLib-matlab/stargazers/)


## Contextual Neural Movement Primitives
[myunusseker/CNMP](https://github.com/myunusseker/CNMP): Full implementation of CNMPs with experiments from the original publication.

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
[![GitHub stars](https://img.shields.io/github/stars/myunusseker/CNMP?style=social)](https://github.com/myunusseker/CNMP/stargazers/)

[mtuluhanakbulut/ACNMP](https://github.com/mtuluhanakbulut/ACNMP): Experimental implementation and simulation for adaptive CNMP.

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
[![GitHub stars](https://img.shields.io/github/stars/mtuluhanakbulut/ACNMP?style=social)](https://github.com/mtuluhanakbulut/ACNMP/stargazers/)

[mtuluhanakbulut/RC-NMP](https://github.com/mtuluhanakbulut/RC-NMP): reward CNMP for population-based variational policy optimization. 

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
[![GitHub stars](https://img.shields.io/github/stars/mtuluhanakbulut/RC-NMP?style=social)](https://github.com/mtuluhanakbulut/RC-NMP/stargazers/)


## Fourier Movement Primitives

[nag92/pdblib-matlab](https://github.com/nag92/pdblib-matlab): Demos for a wide variety of programming by demonstration frameworks including FMPs.

![matlab](https://img.shields.io/badge/matlab-%20-blue)
[![GitHub stars](https://img.shields.io/github/stars/nag92/pdblib-matlab?style=social)](https://github.com/nag92/pdblib-matlab/stargazers/)


## Other Approaches
[ir-lab/intprim](https://github.com/ir-lab/intprim): Complete framework for learning controllers for human-robot interaction applications using Bayesian Interaction Primitives

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
[![GitHub stars](https://img.shields.io/github/stars/ir-lab/intprim?style=social)](https://github.com/ir-lab/intprim/stargazers/)



## Citing This Work

This repository was made in support of the following survey paper:


```
@article{cloud2023movement,
  title={Movement Primitives in Robotics: A Survey},
  author={Cloud, Joseph M and Beksi, William J},
  journal={arXiv preprint arXiv:TBD.TBD},
  year={2023}
}
```
