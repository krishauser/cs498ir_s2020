import math

class DifferentialDrive:
    def __init__(self,wheelbase,wheelradius,vmin=-1,vmax=1):
        self.wheelbase = wheelbase
        self.wheelradius = wheelradius
        self.vmin=vmin
        self.vmax=vmax

    def derivative(self,q,u):
        """Given:

        - configuration q=(x,y,theta)
        - controls u=(vl,vr) giving left and right wheel velocities
        
        returns the time derivative dq/dt of the configuration.
        """
        x,y,theta = q
        vl,vr = u
        c,s = math.cos(theta),math.sin(theta)
        Vfwd = self.wheelradius*(vl+vr)*0.5
        dx = c*Vfwd
        dy = s*Vfwd
        dtheta = self.wheelradius/self.wheelbase*(vr-vl)
        return (dx,dy,dtheta)

    def nextState(self,q,u,dt):
        """Given:

        - configuration q=(x,y,theta)
        - controls u=(vl,vr) giving left and right wheel velocities
        - time step dt
        
        returns the next state q' after executing controls u for
        time dt.
        """
        x,y,theta = q
        vl,vr = u
        dtheta = self.wheelradius/self.wheelbase*(vr-vl)
        c,s = math.cos(theta),math.sin(theta)
        Vfwd = self.wheelradius*(vl+vr)*0.5
        if abs(vl-vr) < 1e-3:
            #straight movement, no center of rotation defined
            dx = c*Vfwd*dt
            dy = s*Vfwd*dt
        else:
            #find center of rotation
            cry = Vfwd/dtheta
            #rotate dtheta*dt rads around point (0,cry)
            dx_local = cry*math.sin(dtheta*dt)
            dy_local = cry*(1-math.cos(dtheta*dt))
            #rotate back to original coordinate system
            dx = c*dx_local - s*dy_local
            dy = s*dx_local + c*dy_local
        return (x+dx,y+dy,theta+dtheta*dt)

    def trajectory(self,q,u,dt,inner_dt=1e-2):
        """Similar to nextState, but returns a trajectory of states
        discretized at resolution inner_dt."""
        traj = [q]
        t=0
        while t < dt:
            q = self.nextState(q,u,min(inner_dt,dt-t))
            traj.append(q)
            t += inner_dt
        return traj



def selfTest():
    robot = dd.DifferentialDrive(0.7,0.1)
    print("@ x=y=theta=0")
    print("dq/dt, u=(1,1):",robot.derivative((0,0,0),(1,1)))
    print("dq/dt, u=(-1,1):",robot.derivative((0,0,0),(-1,1)))
    print("dq/dt, u=(1,0):",robot.derivative((0,0,0),(1,0)))
    print("@ theta=pi/2")
    print("dq/dt, u=(1,1):",robot.derivative((0,0,math.pi/2),(1,1)))
    print("dq/dt, u=(-1,1):",robot.derivative((0,0,math.pi/2),(-1,1)))
    print("dq/dt, u=(1,0):",robot.derivative((0,0,math.pi/2),(1,0)))
    
    print("@ x=y=theta=0")
    print("next q, u=(0,0), dt=1.0:",robot.nextState((0,0,0),(0,0),1.0))
    print("next q, u=(1,1), dt=1.0:",robot.nextState((0,0,0),(1,1),1.0))
    print("next q, u=(1,-1), dt=1.0:",robot.nextState((0,0,0),(1,-1),1.0))
    print("next q, u=(1,0), dt=1.0:",robot.nextState((0,0,0),(1,0),1.0))