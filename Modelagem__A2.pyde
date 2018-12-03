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
g = 1000
teta = -PI/2
teta2 = -PI/2
t0 = millis()/1000.0
R = 225
R2 = 100
#aux = -1
x = 0
y =0 

def setup():
    size(900, 600)

def draw():
    global x1, x2, y1, y2, t0, m1, m2, h, teta, R, v1, teta2, aux, y, x, Img
    translate(width/2, height/2)

    #variação do tempo 
    t2 =  millis()/10000.0
    dt = t2 - t0
    t0 = t2
    
    noStroke()
    fill(191, 255, 0)
    ellipse(x1, y1, 20, 20)
    line(-255,0,0,0)
    #aux = aux + 1
    
    #if aux == 0: 
    if x1 < -225:
        #atualização da posição e velocidade
        x1 = R*sin(teta) - 225
        y1 = R*cos(teta) - 300
        v1 = sqrt(abs(2*g*(h-y1)))
        teta = teta + v1*dt/R
        
    #v2 = v1
    #elif aux == 1: 
    elif x1 < -112:
        x1 = x1 + v1*dt
        y1 = -75
        
    #elif aux == 2: 
    elif x1 >= -112 and x2 < 0:
        x1 = -112
        y1 = -75
        x2 = x2 + v1*dt
        y2 = -75 
    
    elif x2 >= 0 and y2 == -75 and y == 0:
        x = x + 1
    
    elif x == 1 and y == 0:
        x2 = R*sin(teta2) + 100
        y2 = R*cos(teta2) -75
        v2 = v1
        teta2 = teta2 + v2*dt/R
        y = y + 1
        v2 = sqrt(abs(2((v2^2)/2-g*y2)))
    
    elif y == 1 and x == 1:
        inic = y2
        inic2 = x2
        x2 = R*sin(teta2) + 100
        y2 = R*cos(teta2) -75
        v2 = sqrt(abs(2*(g*inic+ ((v2)^2)/2 - g*y2)))
        teta2 = teta2 + v2*dt/R
    
    #elif aux == True:
        #v2 = sqrt(abs(2*g*(h-y1)))
        
    #elif aux == 3: #x2 = 0:
        
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
    ellipse(15, -165, 200, 200)
    line(5, -65, 450 , - 65)
    
    #Pêndulo de Newton
    
