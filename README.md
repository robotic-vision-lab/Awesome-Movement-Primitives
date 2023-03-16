<!-- omit in toc -->
# Awesome Movement Primitives  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Links to software implementations of movement primitive (MP) frameworks and core papers, including:
dynamic MPs,
probabilistic MPs,
kernelized MPs,
conditional neural MPs,
fourier MPs,
and other methods.

<!-- omit in toc -->
## Table of Contents
- [Dynamic Movement Primitives](#dynamic-movement-primitives)
  - [Papers](#papers)
  - [Software](#software)
- [Probabilistic Movement Primitives](#probabilistic-movement-primitives)
  - [Papers](#papers-1)
  - [Software](#software-1)
- [Kernelized Movement Primitives](#kernelized-movement-primitives)
  - [Papers](#papers-2)
  - [Software](#software-2)
- [Conditional Neural Movement Primitives](#conditional-neural-movement-primitives)
  - [Papers](#papers-3)
  - [Software](#software-3)
- [Fourier Movement Primitives](#fourier-movement-primitives)
  - [Papers](#papers-4)
  - [Software](#software-4)
- [Other Approaches](#other-approaches)
- [Citing This Work](#citing-this-work)


## Dynamic Movement Primitives

### Papers
 - [Schaal, S. (2006). Dynamic movement primitives-a framework for motor control in humans and humanoid robotics. *Adaptive motion of animals and machines*, 261-280.](https://link.springer.com/chapter/10.1007/4-431-31381-8_23)
 - [Ijspeert, A. J., Nakanishi, J., Hoffmann, H., Pastor, P., & Schaal, S. (2013). Dynamical movement primitives: learning attractor models for motor behaviors. *Neural computation*, 25(2), 328-373.](https://direct.mit.edu/neco/article-abstract/25/2/328/7850/Dynamical-Movement-Primitives-Learning-Attractor)
 - [Saveriano, M., Abu-Dakka, F. J., Kramberger, A., & Peternel, L. (2021). Dynamic movement primitives in robotics: A tutorial survey. *arXiv preprint arXiv:2102.03861.*](https://arxiv.org/abs/2102.03861)

### Software
[studywolf/pydmps](https://github.com/studywolf/pydmps): DMP tutorial and applications with minimal library dependencies. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/stulp/dmpbbo/stargazers/"><img src="https://img.shields.io/github/stars/studywolf/pydmps?style=social" height="20" /></a> 

[stulp/dmpbbo](https://github.com/stulp/dmpbbo): Combines Black-box optimization (BBO) with DMPs. 

<img src="./ico/python.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/stulp/dmpbbo/stargazers/"><img src="https://img.shields.io/github/stars/stulp/dmpbbo?style=social" height="20" /></a> 

[sniekum/dmp](https://github.com/sniekum/dmp): Robot-agnostic implementation for ROS. 

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/sniekum/dmp/stargazers/"><img src="https://img.shields.io/github/stars/sniekum/dmp?style=social" height="20" /></a> 

[dfki-ric/movement_primitives](https://github.com/dfki-ric/movement_primitives): Various MP frameworks including DMPs (with spatially coupled support) and ProMPs. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/dfki-ric/movement_primitives/stargazers/"><img src="https://img.shields.io/github/stars/dfki-ric/movement_primitives?style=social" height="20" /></a> 

[chauby/PyDMPs_Chauby](https://github.com/chauby/PyDMPs_Chauby): DMPs for simulated UR5 robot in CoppeliaSim (V-REP).

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/chauby/PyDMPs_Chauby/stargazers/"><img src="https://img.shields.io/github/stars/chauby/PyDMPs_Chauby?style=social" height="20" /></a> 

[AlexanderFabisch/PyDMP](https://github.com/AlexanderFabisch/PyDMP): Illustrative notebooks for understanding concepts.

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/AlexanderFabisch/PyDMP/stargazers/"><img src="https://img.shields.io/github/stars/AlexanderFabisch/PyDMP?style=social" height="20" /></a> 

[mginesi/dmp_pp](https://github.com/mginesi/dmp_pp):  Library based on "Overcoming some drawbacks of DMPs" paper.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/mginesi/dmp_pp/stargazers/"><img src="https://img.shields.io/github/stars/mginesi/dmp_pp?style=social" height="20" /></a> 

[suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics](https://github.com/suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics):  Short implementation in matlab.

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics/stargazers/"><img src="https://img.shields.io/github/stars/suryakiranmg/Dynamic-Movement-Primitives-and-Imitation-Learning-Robotics?style=social" height="20" /></a> 

[abakisita/ros_dmp](https://github.com/abakisita/ros_dmp): Package with services for learning motion and generating from leart DMP. 

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/abakisita/ros_dmp/stargazers/"><img src="https://img.shields.io/github/stars/abakisita/ros_dmp?style=social" height="20" /></a> 

[mginesi/dmp_vol_obst](https://github.com/mginesi/dmp_vol_obst): Appended secondary forcing term for obstacle avoidance. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/mginesi/dmp_vol_obst/stargazers/"><img src="https://img.shields.io/github/stars/mginesi/dmp_vol_obst?style=social" height="20" /></a> 

[ferreirafabio/movement_primitives_via_optimization](https://github.com/ferreirafabio/movement_primitives_via_optimization): Incorporates Lagrangian optimization for adapting to demonstrations. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/ferreirafabio/movement_primitives_via_optimization/stargazers/"><img src="https://img.shields.io/github/stars/ferreirafabio/movement_primitives_via_optimization?style=social" height="20" /></a> 

[varadVaidya/dmp](https://github.com/varadVaidya/dmp): Secondary forcing term for single and multi-point obstacle avoidance. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/varadVaidya/dmp/stargazers/"><img src="https://img.shields.io/github/stars/varadVaidya/dmp?style=social" height="20" /></a> 

[liangyuwei/dual_ur5_arm](https://github.com/liangyuwei/dual_ur5_arm): Dual-arm peg-in-hole task with UR5 robots. 

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/liangyuwei/dual_ur5_arm/stargazers/"><img src="https://img.shields.io/github/stars/liangyuwei/dual_ur5_arm?style=social" height="20" /></a> 

[baggepinnen/DynamicMovementPrimitives.jl](https://github.com/baggepinnen/DynamicMovementPrimitives.jl): Standard formulation and implementation of 2DoF control for trajectory tracking and perturbation recovery.  

<img src="./ico/julia.png" height="20" /> 
<a href="https://github.com/baggepinnen/DynamicMovementPrimitives.jl/stargazers/"><img src="https://img.shields.io/github/stars/baggepinnen/DynamicMovementPrimitives.jl?style=social" height="20" /></a> 

[awesomebytes/dmp_gestures](https://github.com/awesomebytes/dmp_gestures): Use cameras to capture gestures to learn and generate DMPs executed through MoveIt!. 

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/awesomebytes/dmp_gestures/stargazers/"><img src="https://img.shields.io/github/stars/awesomebytes/dmp_gestures?style=social" height="20" /></a> 

[CarlDegio/PI2-DMPs](https://github.com/CarlDegio/PI2-DMPs): Reinforcement learning via Policy Improvement with Path Integrals (PI2) 

<img src="./ico/matlab.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/CarlDegio/PI2-DMPs/stargazers/"><img src="https://img.shields.io/github/stars/CarlDegio/PI2-DMPs?style=social" height="20" /></a> 

[tsitsimis/dmpling](https://github.com/tsitsimis/dmpling): Trajectories learned from human gestures (3D marker poses) with notebook visualizations.

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/tsitsimis/dmpling/stargazers/"><img src="https://img.shields.io/github/stars/tsitsimis/dmpling?style=social" height="20" /></a> 

[heracleia/pyrdmp](https://github.com/heracleia/pyrdmp): Reinforcement learning library based on the PoWER algorithm.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/heracleia/pyrdmp/stargazers/"><img src="https://img.shields.io/github/stars/heracleia/pyrdmp?style=social" height="20" /></a> 

[Dennis-BIRL-GDUT/baxter_dmp_rl](https://github.com/Dennis-BIRL-GDUT/baxter_dmp_rl):  Workspace for ROS implementation of Baxter pick-and-place.

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/Dennis-BIRL-GDUT/baxter_dmp_rl/stargazers/"><img src="https://img.shields.io/github/stars/Dennis-BIRL-GDUT/baxter_dmp_rl?style=social" height="20" /></a> 

[chauby/DMP_chebotar](https://github.com/chauby/DMP_chebotar): Implementation supports goal location updates.

<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/chauby/DMP_chebotar/stargazers/"><img src="https://img.shields.io/github/stars/chauby/DMP_chebotar?style=social" height="20" /></a> 

[carlos22/pydmp](https://github.com/carlos22/pydmp): Educational implementation of 1D discrete DMP. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/carlos22/pydmp/stargazers/"><img src="https://img.shields.io/github/stars/carlos22/pydmp?style=social" height="20" /></a> 

[dgerod/more-dmps](https://github.com/dgerod/more-dmps): Implementation on three other python DMP libraries. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/dgerod/more-dmps/stargazers/"><img src="https://img.shields.io/github/stars/dgerod/more-dmps?style=social" height="20" /></a> 

[mathiasesn/obstacle_avoidance_with_dmps](https://github.com/mathiasesn/obstacle_avoidance_with_dmps): Incorporates obstacle avoidance and link-collision avoidance.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/mathiasesn/obstacle_avoidance_with_dmps/stargazers/"><img src="https://img.shields.io/github/stars/mathiasesn/obstacle_avoidance_with_dmps?style=social" height="20" /></a> 

[dkebude/DMP-gen](https://github.com/dkebude/DMP-gen): DMP generator for reinforcement learning applications.

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/dkebude/DMP-gen/stargazers/"><img src="https://img.shields.io/github/stars/dkebude/DMP-gen?style=social" height="20" /></a> 

[stulp/dmp_bbo_matlab_deprecated](https://github.com/stulp/dmp_bbo_matlab_deprecated): Black-box optimization with DMPs. 

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/stulp/dmp_bbo_matlab_deprecated/stargazers/"><img src="https://img.shields.io/github/stars/stulp/dmp_bbo_matlab_deprecated?style=social" height="20" /></a> 

[Slifer64/GMP](https://github.com/Slifer64/GMP): Generalized MPs based on DMPs. Supports online adaptation to via-points and off-line/on-line optimization under kinematic constraints.

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/Slifer64/GMP/stargazers/"><img src="https://img.shields.io/github/stars/Slifer64/GMP?style=social" height="20" /></a> 

[cloudy/dmp-obstacle-avoidance](https://github.com/cloudy/dmp-obstacle-avoidance):  Human obstacle avoidance demonstrated on Rethink Robotics Sawyer manipulator.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/cloudy/dmp-obstacle-avoidance/stargazers/"><img src="https://img.shields.io/github/stars/cloudy/dmp-obstacle-avoidance?style=social" height="20" /></a> 

[abakisita/dmp_motion](https://github.com/abakisita/dmp_motion): Pre-cursor implementation to author's ROS package.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/abakisita/dmp_motion/stargazers/"><img src="https://img.shields.io/github/stars/abakisita/dmp_motion?style=social" height="20" /></a> 

[shobhit6993/egraphs-with-dmp](https://github.com/shobhit6993/egraphs-with-dmp): DMPs are integrated into experience-graph framework to support adaptation to unseen obstacles.

<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/shobhit6993/egraphs-with-dmp/stargazers/"><img src="https://img.shields.io/github/stars/shobhit6993/egraphs-with-dmp?style=social" height="20" /></a> 

[xukechun/DMPs-learning](https://github.com/xukechun/DMPs-learning): Visualizer for DMPs with RViz. 

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/xukechun/DMPs-learning/stargazers/"><img src="https://img.shields.io/github/stars/xukechun/DMPs-learning?style=social" height="20" /></a> 

[baxter-flowers/dmp_lib](https://github.com/baxter-flowers/dmp_lib): Wraps @studywolf implementation in ROS package.

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/baxter-flowers/dmp_lib/stargazers/"><img src="https://img.shields.io/github/stars/baxter-flowers/dmp_lib?style=social" height="20" /></a> 

[yuehuang315/LIL-DMP](https://github.com/yuehuang315/LIL-DMP): Lifelong imitation learning with DMPs.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/yuehuang315/LIL-DMP/stargazers/"><img src="https://img.shields.io/github/stars/yuehuang315/LIL-DMP?style=social" height="20" /></a> 

[gsutanto/dmp](https://github.com/gsutanto/dmp): Reference implementation in three languages with hard real-time support for robot control (C++).

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/gsutanto/dmp/stargazers/"><img src="https://img.shields.io/github/stars/gsutanto/dmp?style=social" height="20" /></a> 

[Shaluols/ur5e_dmp](https://github.com/Shaluols/ur5e_dmp): Leverages UR5e Gazebo simulation to learn DMPs based on @studywolf's library.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/Shaluols/ur5e_dmp/stargazers/"><img src="https://img.shields.io/github/stars/Shaluols/ur5e_dmp?style=social" height="20" /></a> 

[Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree](https://github.com/Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree): Use behavior trees and DMPs for upper-level task planning.

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree/stargazers/"><img src="https://img.shields.io/github/stars/Lygggggg/Upper-level-task-planning-of-Jaco-based-on-behavior-tree?style=social" height="20" /></a> 

[Slifer64/DMP_KF](https://github.com/Slifer64/DMP_KF): DMPs implemented with kalman filtering and support for Kuka/UR robots.

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/Slifer64/DMP_KF/stargazers/"><img src="https://img.shields.io/github/stars/Slifer64/DMP_KF?style=social" height="20" /></a> 

[herambnemlekar/dmp-handovers](https://github.com/herambnemlekar/dmp-handovers): Preditive human-robot handovers using DMPs on the Baxter robot.

<img src="./ico/ros.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/herambnemlekar/dmp-handovers/stargazers/"><img src="https://img.shields.io/github/stars/herambnemlekar/dmp-handovers?style=social" height="20" /></a> 

[AlpX/DMP-LWR](https://github.com/AlpX/DMP-LWR): Reference implementation in matlab using locally weighted regression. 

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/AlpX/DMP-LWR/stargazers/"><img src="https://img.shields.io/github/stars/AlpX/DMP-LWR?style=social" height="20" /></a> 

[kostasVlachos/dmp_control](https://github.com/kostasVlachos/dmp_control): DMP control for Kuka robot.

<img src="./ico/cpp.png" height="20" /> 
<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/kostasVlachos/dmp_control/stargazers/"><img src="https://img.shields.io/github/stars/kostasVlachos/dmp_control?style=social" height="20" /></a> 

[alaradirik/robot-learning](https://github.com/alaradirik/robot-learning): Algorithms from university course implemented in numpy.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/alaradirik/robot-learning/stargazers/"><img src="https://img.shields.io/github/stars/alaradirik/robot-learning?style=social" height="20" /></a> 

[zhouyou-kit/dmp_exercise](https://github.com/zhouyou-kit/dmp_exercise): Educational visualization based on Peter Corke's matlab robotics toolbox.

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/zhouyou-kit/dmp_exercise/stargazers/"><img src="https://img.shields.io/github/stars/zhouyou-kit/dmp_exercise?style=social" height="20" /></a> 

[ZhengYi0310/dmp-ros-pkg](https://github.com/ZhengYi0310/dmp-ros-pkg): DMP implementation for PR2 and WAM robots.

<img src="./ico/cpp.png" height="20" /> 
<img src="./ico/ros.png" height="20" /> 
<a href="https://github.com/ZhengYi0310/dmp-ros-pkg/stargazers/"><img src="https://img.shields.io/github/stars/ZhengYi0310/dmp-ros-pkg?style=social" height="20" /></a> 

[justagist/reversible_dmp](https://github.com/justagist/reversible_dmp):  Implements reversible discrete DMP.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/justagist/reversible_dmp/stargazers/"><img src="https://img.shields.io/github/stars/justagist/reversible_dmp?style=social" height="20" /></a> 

[emarescotti/VelocityPlanning_DMP_FL](https://github.com/emarescotti/VelocityPlanning_DMP_FL): Velocity planning of robotic sealing tasks using DMPs.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/emarescotti/VelocityPlanning_DMP_FL/stargazers/"><img src="https://img.shields.io/github/stars/emarescotti/VelocityPlanning_DMP_FL?style=social" height="20" /></a> 

[ZhengYi0310/DMP](https://github.com/ZhengYi0310/DMP): Implementation in two languages.

<img src="./ico/python.png" height="20" /> 
<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/ZhengYi0310/DMP/stargazers/"><img src="https://img.shields.io/github/stars/ZhengYi0310/DMP?style=social" height="20" /></a> 

[MichailTheofanidis/dmp-protoype](https://github.com/MichailTheofanidis/dmp-protoype): Experimental implementation of reinforcement-learning based adaptation and robot inverse kinematics.

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/MichailTheofanidis/dmp-protoype/stargazers/"><img src="https://img.shields.io/github/stars/MichailTheofanidis/dmp-protoype?style=social" height="20" /></a> 

[cunnia3/Dynamic-Motion-Primitives](https://github.com/cunnia3/Dynamic-Motion-Primitives): Implementation based on @studywolf DMP.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/cunnia3/Dynamic-Motion-Primitives/stargazers/"><img src="https://img.shields.io/github/stars/cunnia3/Dynamic-Motion-Primitives?style=social" height="20" /></a> 

[nag92/dmp_experiments](https://github.com/nag92/dmp_experiments):  Experimental implementation in two languages.

<img src="./ico/python.png" height="20" /> 
<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/nag92/dmp_experiments/stargazers/"><img src="https://img.shields.io/github/stars/nag92/dmp_experiments?style=social" height="20" /></a> 

[Slifer64/resnet_dmp](https://github.com/Slifer64/resnet_dmp): Uses RGB images with resnet network architecture to learn DMPs for planar tasks.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/Slifer64/resnet_dmp/stargazers/"><img src="https://img.shields.io/github/stars/Slifer64/resnet_dmp?style=social" height="20" /></a> 


## Probabilistic Movement Primitives

### Papers
 - [Paraschos, A., Daniel, C., Peters, J. R., & Neumann, G. (2013). Probabilistic movement primitives. *Advances in neural information processing systems*, 26.](https://proceedings.neurips.cc/paper/2013/hash/e53a0a2978c28872a4505bdb51db06dc-Abstract.html)
 - [Gomez-Gonzalez, S., Neumann, G., Schölkopf, B., & Peters, J. (2020). Adaptation and robust learning of probabilistic movement primitives. *IEEE Transactions on Robotics*, 36(2), 366-379.](https://ieeexplore.ieee.org/abstract/document/9020014)

### Software
[dfki-ric/movement_primitives](https://github.com/dfki-ric/movement_primitives): Various MP frameworks including DMPs (with spatially coupled support) and ProMPs. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/dfki-ric/movement_primitives/stargazers/"><img src="https://img.shields.io/github/stars/dfki-ric/movement_primitives?style=social" height="20" /></a> 

[sebasutp/promp](https://github.com/sebasutp/promp):  Library that computes trajectory likelihood of ProMP, trajectory sampling, and save/load.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/sebasutp/promp/stargazers/"><img src="https://img.shields.io/github/stars/sebasutp/promp?style=social" height="20" /></a> 

[baxter-flowers/promplib](https://github.com/baxter-flowers/promplib): Features interactive learning componenet to automatically cluster primitives based on standard deviation.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/baxter-flowers/promplib/stargazers/"><img src="https://img.shields.io/github/stars/baxter-flowers/promplib?style=social" height="20" /></a> 

[mjm522/promps_python](https://github.com/mjm522/promps_python): 1D ProMP model with closed-form trajectory controller.

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/mjm522/promps_python/stargazers/"><img src="https://img.shields.io/github/stars/mjm522/promps_python?style=social" height="20" /></a> 

[sebasutp/promp-cpp](https://github.com/sebasutp/promp-cpp): C++ version of @sebasutp python library.

<img src="./ico/cpp.png" height="20" /> 
<a href="https://github.com/sebasutp/promp-cpp/stargazers/"><img src="https://img.shields.io/github/stars/sebasutp/promp-cpp?style=social" height="20" /></a> 

[herambnemlekar/probabilistic-movement-primitives](https://github.com/herambnemlekar/probabilistic-movement-primitives): Experimental implementation for training ProMPs with the Baxter robot. 

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/herambnemlekar/probabilistic-movement-primitives/stargazers/"><img src="https://img.shields.io/github/stars/herambnemlekar/probabilistic-movement-primitives?style=social" height="20" /></a> 

## Kernelized Movement Primitives

### Papers
 - [Huang, Y., Rozo, L., Silvério, J., & Caldwell, D. G. (2019). Kernelized movement primitives. *The International Journal of Robotics Research*, 38(7), 833-852.](https://journals.sagepub.com/doi/pdf/10.1177/0278364919846363)
 - [Silvério, J., Huang, Y., Abu-Dakka, F. J., Rozo, L., & Caldwell, D. G. (2019, November). Uncertainty-aware imitation learning using kernelized movement primitives. *In 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)* (pp. 90-97). IEEE.](https://ieeexplore.ieee.org/abstract/document/8967996)

### Software
[yanlongtu/robInfLib-matlab](https://github.com/yanlongtu/robInfLib-matlab): Demonstrates various functionalities of KMPs. 

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/yanlongtu/robInfLib-matlab/stargazers/"><img src="https://img.shields.io/github/stars/yanlongtu/robInfLib-matlab?style=social" height="20" /></a> 


## Conditional Neural Movement Primitives

### Papers
 - [Seker, M. Y., Imre, M., Piater, J. H., & Ugur, E. (2019, June). Conditional Neural Movement Primitives. *In Robotics: Science and Systems* (Vol. 10).](https://roboticsproceedings.org/rss15/p71.pdf)
 - [Akbulut, M., Oztop, E., Seker, M. Y., Hh, X., Tekden, A., & Ugur, E. (2021, October). ACMP: Skill transfer and task extrapolation through learning from demonstration and reinforcement learning via representation sharing. *In Conference on Robot Learning* (pp. 1896-1907). PMLR.](https://proceedings.mlr.press/v155/akbulut21a.html)

### Software
[myunusseker/CNMP](https://github.com/myunusseker/CNMP): Full implementation of CNMPs with experiments from the original publication.

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<img src="./ico/pytorch.png" height="20" /> 
<a href="https://github.com/myunusseker/CNMP/stargazers/"><img src="https://img.shields.io/github/stars/myunusseker/CNMP?style=social" height="20" /></a> 

[mtuluhanakbulut/ACNMP](https://github.com/mtuluhanakbulut/ACNMP): Experimental implementation and simulation for adaptive CNMP.

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<img src="./ico/keras.png" height="20" /> 
<a href="https://github.com/mtuluhanakbulut/ACNMP/stargazers/"><img src="https://img.shields.io/github/stars/mtuluhanakbulut/ACNMP?style=social" height="20" /></a> 

[mtuluhanakbulut/RC-NMP](https://github.com/mtuluhanakbulut/RC-NMP): reward CNMP for population-based variational policy optimization. 

<img src="./ico/jupyter.png" height="20" /> 
<img src="./ico/python.png" height="20" /> 
<img src="./ico/keras.png" height="20" /> 
<a href="https://github.com/mtuluhanakbulut/RC-NMP/stargazers/"><img src="https://img.shields.io/github/stars/mtuluhanakbulut/RC-NMP?style=social" height="20" /></a> 


## Fourier Movement Primitives

### Papers
 - [Kulak, T., Silvério, J., & Calinon, S. (2020, June). Fourier movement primitives: an approach for learning rhythmic robot skills from demonstrations. *In Robotics: Science and Systems*. (Vol. 11).](https://roboticsconference.org/2020/program/papers/56.html)


### Software
[nag92/pdblib-matlab](https://github.com/nag92/pdblib-matlab): Demos for a wide variety of programming by demonstration frameworks including FMPs.

<img src="./ico/matlab.png" height="20" /> 
<a href="https://github.com/nag92/pdblib-matlab/stargazers/"><img src="https://img.shields.io/github/stars/nag92/pdblib-matlab?style=social" height="20" /></a> 


## Other Approaches
[ir-lab/intprim](https://github.com/ir-lab/intprim): Complete framework for learning controllers for human-robot interaction applications using Bayesian Interaction Primitives

<img src="./ico/python.png" height="20" /> 
<a href="https://github.com/ir-lab/intprim/stargazers/"><img src="https://img.shields.io/github/stars/ir-lab/intprim?style=social" height="20" /></a> 



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
