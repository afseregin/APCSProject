import pygame
import os
import random
pygame.init()
############################################################################################
word = random.choice(open("words.txt").read().split())
width,height = 900,500
window = pygame.display.set_mode((width,height))
line_image = pygame.image.load(os.path.join('assets','line.png'))
line = pygame.transform.scale(line_image,(400,600))
gallow_image = pygame.image.load(os.path.join('assets', 'hangman_gallow.png'))
gallow = pygame.transform.scale(gallow_image, (550,400))
a_image = pygame.image.load(os.path.join('assets','a.png'))
a = pygame.transform.scale(a_image,(40,40))
#
b_image = pygame.image.load(os.path.join('assets','b.png'))
b = pygame.transform.scale(b_image,(40,40))
#
c_image = pygame.image.load(os.path.join('assets','c.png'))
c = pygame.transform.scale(c_image,(40,40))
#
d_image = pygame.image.load(os.path.join('assets','d.png'))
d = pygame.transform.scale(d_image,(40,40))
#
e_image = pygame.image.load(os.path.join('assets','e.png'))
e = pygame.transform.scale(e_image,(40,40))
#
f_image = pygame.image.load(os.path.join('assets','f.png'))
f = pygame.transform.scale(f_image,(40,40))
#
g_image = pygame.image.load(os.path.join('assets','g.png'))
g = pygame.transform.scale(g_image,(40,40))
#
h_image = pygame.image.load(os.path.join('assets','h.png'))
h = pygame.transform.scale(h_image,(40,40))
#
i_image = pygame.image.load(os.path.join('assets','i.png'))
i = pygame.transform.scale(i_image,(40,40))
#
j_image = pygame.image.load(os.path.join('assets','j.png'))
j = pygame.transform.scale(j_image,(40,40))
#
k_image = pygame.image.load(os.path.join('assets','k.png'))
k = pygame.transform.scale(k_image,(40,40))
#
l_image = pygame.image.load(os.path.join('assets','l.png'))
l = pygame.transform.scale(l_image,(40,40))
#
m_image = pygame.image.load(os.path.join('assets','m.png'))
m = pygame.transform.scale(m_image,(40,40))
#
n_image = pygame.image.load(os.path.join('assets','n.png'))
n = pygame.transform.scale(n_image,(40,40))
#
o_image = pygame.image.load(os.path.join('assets','o.png'))
o = pygame.transform.scale(o_image,(40,40))
#
p_image = pygame.image.load(os.path.join('assets','p.png'))
p = pygame.transform.scale(p_image,(40,40))
#
q_image = pygame.image.load(os.path.join('assets','q.png'))
q = pygame.transform.scale(q_image,(40,40))
#
r_image = pygame.image.load(os.path.join('assets','r.png'))
r = pygame.transform.scale(r_image,(40,40))
#
s_image = pygame.image.load(os.path.join('assets','s.png'))
s = pygame.transform.scale(s_image,(40,40))
#
t_image = pygame.image.load(os.path.join('assets','t.png'))
t = pygame.transform.scale(t_image,(40,40))
#
u_image = pygame.image.load(os.path.join('assets','u.png'))
u = pygame.transform.scale(u_image,(40,40))
#
v_image = pygame.image.load(os.path.join('assets','v.png'))
v = pygame.transform.scale(v_image,(40,40))
#
w_image = pygame.image.load(os.path.join('assets','w.png'))
w = pygame.transform.scale(w_image,(40,40))
#
x_image = pygame.image.load(os.path.join('assets','x.png'))
x = pygame.transform.scale(x_image,(40,40))
#
y_image = pygame.image.load(os.path.join('assets','y.png'))
y = pygame.transform.scale(y_image,(40,40))
#
z_image = pygame.image.load(os.path.join('assets','z.png'))
z = pygame.transform.scale(z_image,(40,40))
############################################################################################
def draw():
    window.fill((255,255,255))
    window.blit(gallow, (200,150))
    for x in range(len(word)):
        window.blit(line,(200+(x*50),10))

    counter = 0
    #for letter in word:
    #    for event in pygame.event.get():
    #        if event.type==pygame.KEYDOWN:
    #            if event.key==pygame.K_a:
    #                window.blit(a,(200+(counter*50),15))

    
    pygame.display.update()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        draw()    

    

if __name__ == "__main__":
     main()