# Introduction {#introduction .unnumbered}

- This guide covers the core concepts, formulas, and other important
  information for each topic on the AP Physics C: Mechanics exam.

## Before You Begin {#before-you-begin .unnumbered}

- A decent grasp of basic calculus is required for the Physics C exams
  as they are calculus-based. You will need to know basic integration
  and differentiation, and how to solve separable differential
  equations. The calculus is not at the level of Calculus BC; for
  example, there is no integration by parts.

- A good understanding of high school level physics concepts is also
  recommended. If you have taken Physics 1 or 2, that will be beneficial
  as this course expands on classical mechanics concepts in greater
  detail.

- Variables in formulas that are vector quantities will be in **BOLD**.

- For the acceleration of gravity near Earth's surface, this guide will
  use $10 \, \text{m/s}^2$, as this is permitted on the AP Physics C:
  Mechanics exam and simplifies calculations.

# Unit 1: Kinematics

This unit focuses on motion in one dimension, examining three key
quantities: position, velocity, and acceleration.

## The Kinematic Equations

These three main kinematic equations are applicable when acceleration is
constant. $$x = x_{0} + v_{x_{0}}t + \frac{1}{2}a_{x}t^{2}$$
$$v_{x} = v_{x_{0}} + a_{x}t$$
$$v_{x}^{2} = v_{x_{0}}^{2} + 2a_{x}(x - x_{0})$$

## Constant/Average Velocity and Acceleration Models

- For constant velocity: $$v_{x} = \frac{\Delta x}{\Delta t}$$

- For average velocity and acceleration:
  $$v_{x(\text{avg})} = \frac{\Delta x}{\Delta t}$$
  $$a_{x(\text{avg})} = \frac{\Delta v_{x}}{\Delta t}$$

## Calculus-Based Relationships and Models

When acceleration is not constant, calculus-based relationships are
necessary.

- **Derivatives**: The instantaneous velocity is the derivative of
  position with respect to time, and acceleration is the derivative of
  velocity with respect to time. $$v_{x} = \frac{dx}{dt}$$
  $$a_{x} = \frac{dv_{x}}{dt}$$

- **Integrals**: By the fundamental theorem of calculus, displacement is
  the integral of velocity, and the change in velocity is the integral
  of acceleration. These integrals represent the \"area under the
  curve\" on velocity-time or acceleration-time graphs.
  $$\Delta x = \int v_{x}dt$$ $$\Delta v = \int a_{x}dt$$

# Unit 2: Newton's Laws of Motion

## Newton's First Law

An object at rest or in uniform motion will stay that way unless acted
upon by a net external force. This implies that an object with constant
velocity has a net force of zero acting on it ($F_{net}=0$).

## The Second Law of Motion

The sum of forces on an object is proportional to its mass and
acceleration.

- For a constant mass: $$\sum F = ma$$

- If mass is not constant, a more general form is needed (covered in
  Unit 4).

## The Third Law of Motion

For every action, there is an equal and opposite reaction. If object A
exerts a force on object B, object B exerts an equal and opposite force
on object A. These forces act on different objects.

## Forces

Forces are pushes or pulls between two objects and are categorized as
contact or non-contact forces.

## Equilibrium

An object is in equilibrium if the net force on it is zero.

- **Dynamic equilibrium**: The object is moving at a constant velocity.

- **Static equilibrium**: The object is not moving.

## Normal Force

The normal force is a contact force that prevents objects from passing
through each other.

## Friction Force

Friction opposes the sliding motion or attempted motion between
surfaces. It depends on the normal force ($N$) and the coefficient of
friction ($\mu$).

- **Static Friction**: Occurs when there is no relative motion. It
  increases to match an applied force up to a maximum value.
  $$f_{s} \le \mu_{s}N$$

- **Kinetic Friction**: Occurs during relative motion and is constant if
  the normal force is constant. $$f_{k} = \mu_{k}N$$

## Applying the Laws: Pulleys

For a system with two blocks, one on a frictionless table (mass $m$) and
one hanging (mass $M$), connected by a pulley, we can find the
acceleration by analyzing the forces on each block.

- **Block on table (m)**: The net force is the tension ($F_T$).
  $$F_{T} = ma$$

- **Hanging block (M)**: The net force is the difference between its
  weight and the tension. $$Mg - F_{T} = Ma$$

Adding the two equations yields the acceleration of the system:
$$Mg = (M+m)a$$ $$a = \frac{Mg}{M+m}$$

## Uniform Circular Motion

An object moving in a circle at a constant speed has a centripetal
acceleration directed towards the center of the circle.
$$a_{c} = \frac{v^{2}}{r}$$ Centripetal force is not a new force but is
the net force provided by other forces like tension or gravity.

# Unit 3: Work, Energy, and Power

## Work

Work is done when a force displaces an object. Only the component of the
force parallel to the displacement does work.

- **Constant force in direction of displacement**: $$W = Fd$$

- **Constant force at an angle $\theta$ to displacement**:
  $$W = \vec{F} \cdot \vec{r} = Fr \cos(\theta)$$

- **Variable force**: Work is the integral of the force over the
  displacement, which is the area under a force-position graph.
  $$W = \int_{x_{1}}^{x_{2}} F(r) \cdot dr$$

## Work-Energy Theorem

The net work done on an object equals the change in its kinetic energy.
$$W_{\text{net}} = \Delta K$$

- **Kinetic Energy**: $$K = \frac{1}{2}mv^{2}$$

## Conservative and Nonconservative Forces

- A force is **conservative** if the work it does depends only on the
  initial and final positions, not the path taken. The net work done by
  a conservative force over a closed path is zero.

- Forces like friction are generally **dissipative** (nonconservative).

## Potential Energy

Potential energy is associated with conservative forces.
$$\Delta U = - \int_{a}^{b} \vec{F}_{\text{cons}} \cdot d\vec{r}$$
$$F_{x} = -\frac{dU(x)}{dx}$$

- **Elastic Potential Energy (Ideal Spring)**: From Hooke's Law
  ($F_s = -kx$). $$U_{s} = \frac{1}{2}k(\Delta x)^{2}$$

- **Gravitational Potential Energy (Near Earth)**:
  $$\Delta U_{g} = mg\Delta h$$

- **Gravitational Potential Energy (General)**: For distances where
  gravity is not constant. $$F_{G} = \frac{Gm_{1}m_{2}}{r^{2}}$$
  $$U_{G} = -\frac{Gm_{1}m_{2}}{r}$$

## The Conservation of Energy

In a conservative system where only internal forces act, the total
mechanical energy ($E = K + U$) is constant.
$$E = U_{g} + U_{s} + K = \text{constant}$$ If nonconservative forces do
work, the change in the system's total energy equals the work done by
these forces. $$W_{\text{noncons}} = \Delta E$$

## Power

Power is the rate at which energy changes or work is done.

- **Instantaneous Power**: $$P = \frac{dE}{dt}$$

- **Power from force and velocity**:
  $$P = \frac{W}{t} = \frac{Fd}{t} = Fv$$ $$P = \vec{F} \cdot \vec{v}$$

# Unit 4: Systems of Particles & Linear Momentum

## Center of Mass

The center of mass is a point that represents the average position of
all parts of the system, weighted by mass.

- **For a collection of point masses**:
  $$x_{\text{cm}} = \frac{\sum m_{i}x_{i}}{\sum m_{i}}$$

- **For a continuous distribution of mass**:
  $$x_{\text{cm}} = \frac{\int x dm}{\int dm}$$

If no net external force acts on a system, its center of mass does not
accelerate.

## Linear Momentum

Momentum ($\vec{p}$) is a vector quantity defined as the product of an
object's mass and velocity. $$\vec{p} = m\vec{v}$$ The rate of change of
a system's momentum is equal to the net external force acting on it.
$$\vec{F} = \frac{d\vec{p}}{dt}$$ For constant mass, this simplifies to
$\vec{F} = m\vec{a}$.

## Impulse

Impulse ($\vec{J}$) is the change in momentum and is calculated as the
integral of force over time.
$$\vec{J} = \int \vec{F} dt = \Delta \vec{p}$$ For an average force over
a time interval $\Delta t$: $$\vec{J} = \vec{F}_{\text{avg}} \Delta t$$

## Collisions

In a system with no external forces, linear momentum is conserved during
collisions.

- **Elastic Collisions**: Both momentum and kinetic energy are
  conserved.

- **Completely Inelastic Collisions**: The objects stick together after
  the collision, resulting in the maximum loss of kinetic energy.

# Unit 5: Rotation

## Rotational Quantities

Rotational motion is described by angular position ($\theta$), angular
velocity ($\omega$), and angular acceleration ($\alpha$).

- **Relationship to linear quantities**: $$v = r\omega$$
  $$a_{\theta} = r\alpha$$ The vector relationships are
  $\vec{v} = \vec{\omega} \times \vec{r}$ and
  $\vec{\tau} = \vec{r} \times \vec{F}$.

## Rotational Kinematics

For constant angular acceleration ($\alpha$):
$$\theta = \theta_{0} + \omega_{0}t + \frac{1}{2}\alpha t^{2}$$
$$\omega = \omega_{0} + \alpha t$$
$$\omega^{2} = \omega_{0}^{2} + 2\alpha(\theta - \theta_{0})$$

## Torque

Torque ($\tau$) is the rotational equivalent of force.
$$\tau = rF \sin(\theta)$$ $$\vec{\tau} = \vec{r} \times \vec{F}$$ The
relationship between torque, rotational inertia ($I$), and angular
acceleration is: $$\tau = I\alpha$$

## Rotational Inertia (Moment of Inertia)

Rotational inertia ($I$) is the rotational equivalent of mass.

- **For a point mass**: $I = mr^2$

- **For a collection of particles**: $I = \sum m_i r_i^2$

- **For a continuous body**: $I = \int r^2 dm$

## Rotational (Angular) Momentum

Angular momentum ($\vec{L}$) is the rotational equivalent of linear
momentum. $$\vec{L} = \vec{r} \times \vec{p}$$ For a rotating rigid
body: $$L = I\omega$$ The rate of change of angular momentum is equal to
the net external torque. $$\vec{\tau} = \frac{d\vec{L}}{dt}$$

## Rotational Kinetic Energy

$$K_{\text{rot}} = \frac{1}{2}I\omega^{2}$$ The total kinetic energy of
a rolling object is the sum of its translational and rotational kinetic
energies.
$$K_{\text{total}} = \frac{1}{2}mv^{2} + \frac{1}{2}I\omega^{2}$$

## Rolling Without Slipping

This is a special case where the point of contact with the ground is
stationary. This implies that $v = r\omega$ and $a = r\alpha$. For an
object rolling down a slope, conservation of energy can be used:
$$mgh = \frac{1}{2}mv^{2} + \frac{1}{2}I\left(\frac{v}{r}\right)^{2}$$

# Unit 6: Oscillation

## Simple Harmonic Motion (SHM)

SHM occurs when a restoring force is proportional to the displacement
from equilibrium (like a mass on a spring).

- **Position**: $$x(t) = A \cos(\omega t + \phi)$$ where $A$ is
  amplitude, $\omega$ is angular frequency, and $\phi$ is phase shift.

- **Velocity**: $$v(t) = -A\omega \sin(\omega t + \phi)$$

- **Acceleration**:
  $$a(t) = -A\omega^{2} \cos(\omega t + \phi) = -\omega^{2}x$$

The motion is described by the differential equation:
$$\frac{d^{2}x}{dt^{2}} + \frac{k}{m}x = 0$$ This gives the angular
frequency for a mass-spring system: $$\omega = \sqrt{\frac{k}{m}}$$

## Types of SHM

- **Simple Pendulum (small angles)**: $$\omega = \sqrt{\frac{g}{L}}$$

- **Physical Pendulum**: $$\omega = \sqrt{\frac{mgL_{\text{cm}}}{I}}$$
  where $L_{cm}$ is the distance from the pivot to the center of mass.

## Period and Frequency

The period ($T$) is the time for one full oscillation.
$$T = \frac{2\pi}{\omega} = \frac{1}{f}$$

- **Mass-Spring**: $T = 2\pi\sqrt{\frac{m}{k}}$

- **Simple Pendulum**: $T = 2\pi\sqrt{\frac{L}{g}}$

- **Physical Pendulum**: $T = 2\pi\sqrt{\frac{I}{mgL_{\text{cm}}}}$

## Energy in SHM

The total energy in a mass-spring system is constant:
$$E_{\text{total}} = K + U_s = \frac{1}{2}kA^{2}$$

# Unit 7: Gravitation

## Newton's Law of Universal Gravitation

The magnitude of the gravitational force between two masses is:
$$F_{G} = G\frac{m_{1}m_{2}}{r^{2}}$$ where
$G \approx 6.674 \times 10^{-11} \, \text{N}\cdot\text{m}^2/\text{kg}^2$
is the gravitational constant. For spatially extended objects, the net
force is the vector sum (or integral) of the forces from all parts of
the object. $$\vec{F} = GM \int \frac{dm}{r^2}\hat{r}$$

## Gravitational Field

The gravitational field, $\vec{g}$, is the gravitational force per unit
mass. $$\vec{F} = m\vec{g}$$ For a point mass $m$:
$$\vec{g}(r) = -G\frac{m}{|r|^{2}}\hat{r}$$

## Gravitational Potential Energy

Gravity is a conservative force, so it has an associated potential
energy. $$U_{g} = -G\frac{m_{1}m_{2}}{r}$$ Potential energy is zero at
an infinite distance.

## Orbits

- **Circular Orbit Velocity**: The gravitational force provides the
  necessary centripetal force.
  $$\frac{GMm}{r^2} = \frac{mv^2}{r} \implies v_{\text{orbit}} = \sqrt{\frac{GM}{r}}$$

- **Orbital Period (Kepler's Third Law)**: For a circular orbit:
  $$T = \frac{2\pi r}{v} \implies T^2 = \frac{4\pi^2}{GM}r^3$$

## Conservation in Orbits

- **Angular Momentum is conserved** because gravity is a central force
  and exerts no torque.

- **Mechanical Energy is conserved** because gravity is a conservative
  force.
