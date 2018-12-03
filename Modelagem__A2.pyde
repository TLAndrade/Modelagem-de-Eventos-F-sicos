x1 = -450
y1 = -300
h = -300
x2 = -92
y2 = -75
#x3 =
#y3 = 
#v1 = 0 
#v2 = 
m1 = 1  
#m2 = 
g = 98
teta = -PI/2
teta2 = 0
t0 = millis()/1000.0
R = 225
R2 = 100
#aux = -1
x = 0
y =0 

def setup():
    size(900, 600)

def draw():
    global x1, x2, y1, y2, t0, m1, m2, h, teta, R, v1, teta2, aux, y, x, v2, y3, y4
    translate(width/2, height/2)

    #variação do tempo 
    t2 =  millis()/1000.0
    dt = t2 - t0
    t0 = t2
    
    noStroke()
    fill(191, 255, 0)
    ellipse(x1, y1, 20, 20)
    line(-255,0,0,0)
    
    if x1 < -225:
        #atualização da posição e velocidade
        x1 = R*sin(teta) - 225
        y1 = R*cos(teta) - 300
        v1 = sqrt(abs(2*g*(h-y1)))
        teta = teta + v1*dt/R

    elif x1 < -112:
        x1 = x1 + v1*dt
        y1 = -75
        
    elif x1 >= -112 and x2 < 0 and y2 == -75 and x < 1:
        x1 = -112
        y1 = -75
        x2 = x2 + v1*dt
        y2 = -75
        v2 = v1
     
    #elif x2 == x2_origem and y2 == y2_origem and x >= 1:
        #x2 = x2 + v2*dt
        #y2 = -75

    elif x2 >= 0 and y2 <= 0 and y <= 0:
        #posicao.append(x2)
        #posicao.append(y2)
        x = x + 1
        y3 = y2
        x2 = R2*sin(teta2) 
        y2 = R2*cos(teta2) - 175
        v2 = sqrt(abs(2*((v2**2)/2 + g*y3 - g*y2)))
        teta2 = teta2 + v2*dt/R2

    elif x2 <= 0 and y2 <= 0:
        x = x + 1
        y = y + 1
        y3 = y2
        x2 = R2*sin(teta2) 
        y2 = R2*cos(teta2) - 175
        v2 = sqrt(abs(2*((v2**2)/2 + g*y3 - g*y2)))
        teta2 = teta2 + v2*dt/R2
        
    elif x2 >= 0 and y2 <= 0 and y > 0:
        x2 = x2 + v2*dt
        y2 = -75
        
    #Imagem de fundo
    background(225)
    
    ellipse(x1, y1, 20, 20)
    fill(191, 0, 255)
    ellipse(x2, y2, 20, 20)
    
    #Trajetória
    noFill()
    stroke(160,82,45)
    strokeWeight(4)
    arc(-230, -290, 450, 450, radians(90), radians(180))
    line(-230, -65, 5 , - 65)
    ellipse(0, -174, 216, 216)
    line(5, -65, 450 , - 65)
    
    #Pêndulo de Newton
    
