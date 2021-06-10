import random


def objective(pos):
    tot = 0
    val = 0
    for i in marks:
        dif = abs(i - pos[0])
        val=pos[0]
        for i2 in pos:
            if abs(i - i2) < dif:
                val = i2
                dif = abs(i - i2)
        tot += (i - val) ** 2
    return tot


class particle():
    def __init__(self, pos, vel, pbest):
        global gbest, gbest_pos
        self.pos = pos.copy()
        self.vel = vel.copy()
        self.pbest = pbest
        self.pbest_pos = pos.copy()
        if self.pbest < gbest or gbest == -1:
            gbest = self.pbest
            gbest_pos = self.pbest_pos.copy()
        print('initialized Particle: ', 'position ', pos, ' velocity ', vel, ' pbest ', pbest)

    def update(self):
        global gbest, gbest_pos, k
        print('updating: ','position',self.pos,'velocity', self.vel, 'pbest_position', self.pbest_pos,'pbest', self.pbest)
        v_new = []
        for i in range(len(self.vel)):
            v_new.append(
                self.vel[i] + c1 * random.randint(0, 1) * (self.pbest_pos[i] - self.pos[i]) + c2 * random.randint(0, 1) * (
                            gbest_pos[i] - self.pos[i]))
            self.pos[i] += v_new[i]
        self.vel = v_new.copy()
        for i in range(0, len(self.pos)):
            if self.pos[i] < marks[0]:
                self.pos[i]=marks[0]
                self.vel[i]=0
            elif self.pos[i]>marks[len(marks)-1]:
                self.pos[i]=marks[len(marks)-1]
                self.vel[i]=0

        for i in range(len(pos)):
            dif = abs(self.pos[i] - marks[0])
            val = marks[0]

            for i2 in marks:
                if abs(self.pos[i] - i2) <dif:
                    val = i2
                    dif = abs(self.pos[i] - i2)
            self.pos[i]=val

        n = objective(self.pos)
        if n < self.pbest:
            self.pbest = n
            self.pbest_pos = self.pos.copy()
        if n < gbest:
            gbest = self.pbest
            gbest_pos = self.pbest_pos.copy()

        print('updated: ','position',self.pos,'velocity', self.vel,'pbest position', self.pbest_pos,'pbest', self.pbest)


num_particles = 3
iterations=50
c1 = 2 #weight of personal influence
c2 = 2 #weight of social influence

print('number particles = ',num_particles,'\n')
N=int(input('Enter N: '))
k=int(input('Enter k: '))
marks=[]
print('Enter the marks')
for i in range(0,N):
    ele=int(input())
    marks.append(ele)

marks.sort()
gbest = -1
gbest_pos = []

particles = []
for i in range(0, num_particles):
    pos = []
    vel = []
    for zx in range(k):
        pos.append(marks[random.randint(0, N - 1)])
        vel.append(0)
    particles.append(particle(pos, vel, objective(pos)))

for i in range(iterations):
    print('Iteration:',i+1)
    for x in range(len(particles)):
        print('\nParticle ',x+1,':')
        particles[x].update()
    print('\ngbest:', gbest, gbest_pos,'\n\n\n')

print('Global best : ', gbest, '\nPosition : ', gbest_pos)
print('Grouping:')
groups=[]
for i in range(k):
    rn=[]
    groups.append(rn.copy())

for i in marks:
    dif = abs(i - gbest_pos[0])
    val=0
    for i2 in range(len(gbest_pos)):
        if abs(i - gbest_pos[i2]) < dif:
            val = i2
            dif = abs(i - gbest_pos[i2])
    groups[val].append(i)
print(groups)
    
    
    





