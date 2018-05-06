import pokerGUI



def numero(carta):
    n= carta % 13 +1
    return n

def pinta(carta):
    p = carta//13
    if p == 0:
        p = "c"
    elif p == 1:
        p = "d"
    elif p == 2:
        p = "p"
    elif p == 3:
        p = "t"
    return p

def total(carta):
    carta = str(numero(carta)) + str(pinta(carta))
    return carta


def tarea(poker):
    

    apuesta = 1
    creditocompleto = 1000
    d = True

    def aumentarapuesta(apuesta):
        while poker.preguntar("¿Desea aumentar al doble la apuesta?"):
            apuesta = 2*apuesta
            poker.cambiarApuesta(apuesta)
            poker.cambiarCredito(creditocompleto - apuesta)
            poker.llenarMazo()
            for i in range(1,5):
                poker.cambiarCarta(i,"base")
            carta = poker.sacarCarta()
            numeroapelea = numero(carta)
            poker.cambiarCarta(0,total(carta))
            click = 8
            while click > 4:
                click = poker.esperarClick()
                if click == 1:
                    cartanueva = poker.sacarCarta()
                    cartapropia = numero(cartanueva)
                    poker.cambiarCarta(1,total(cartanueva))
                    
                elif click == 2:
                    cartanueva = poker.sacarCarta()
                    cartapropia = numero(cartanueva)
                    poker.cambiarCarta(2,total(cartanueva))

                elif click == 3:
                    cartanueva = poker.sacarCarta()
                    cartapropia = numero(cartanueva)
                    poker.cambiarCarta(3,total(cartanueva))

                elif click == 4:
                    cartanueva = poker.sacarCarta()
                    cartapropia = numero(cartanueva)
                    poker.cambiarCarta(4,total(cartanueva))

                else:
                    poker.alerta("elija una carta")

            if cartapropia == 1 and numeroapelea != 1:
                poker.alerta("Haz ganado")
            elif cartapropia > numeroapelea:
                poker.alerta("Haz ganado")
            elif cartapropia == numeroapelea:
                poker.alerta("Haz empatado")

            elif (numeroapelea == 1 and cartapropia != 1) or numeroapelea > cartapropia:
                poker.alerta("Perdiste")
                apuesta = -apuesta
                break
            poker.cambiarCredito(creditocompleto + apuesta)
            poker.cambiarApuesta(1)

      
                                
            
        

    while creditocompleto and d > 0:
        click = poker.esperarClick()
        while click != 7:
            if click == 6:
                apuesta = 5
                poker.cambiarApuesta(apuesta)
                poker.cambiarCredito(creditocompleto - apuesta)

            elif click == 5:
                apuesta += 1
                if apuesta <= 5:
                    poker.cambiarApuesta(apuesta)
                    poker.cambiarCredito(creditocompleto - apuesta)
                else:
                    apuesta = 0

            click = poker.esperarClick()
        creditocompleto = creditocompleto - apuesta

        #empezamos a poner las cartas al azar

        carta0 = poker.sacarCarta()
        poker.cambiarCarta(0,total(carta0))

        
        carta1 = poker.sacarCarta()
        poker.cambiarCarta(1,total(carta1))

        carta2 = poker.sacarCarta()
        poker.cambiarCarta(2,total(carta2))

        carta3 = poker.sacarCarta()
        poker.cambiarCarta(3,total(carta3))

        carta4 = poker.sacarCarta()
        poker.cambiarCarta(4,total(carta4))

        #que cartas cambiar

        poker.mensaje("Seleccione cartas que desea cambiar")
        c0 = c1 = c2 = c3 = c4 = 0
        while True:
            h = poker.esperarClick()
            if h == 0:
                c0 += 1
                if c0 % 2 == 1:
                    poker.cambiarTextoEnCarta(0,"cambiar")
                else:
                    poker.cambiarTextoEnCarta(0,"")

            elif h == 1:
                c1 += 1
                if c1 % 2 == 1:
                    poker.cambiarTextoEnCarta(1,"cambiar")
                else:
                    poker.cambiarTextoEnCarta(1,"")

            elif h == 2:
                c2 += 1
                if c2 % 2 == 1:
                    poker.cambiarTextoEnCarta(2,"cambiar")
                else:
                    poker.cambiarTextoEnCarta(2,"")

            elif h == 3:
                c3 += 1
                if c3 % 2 == 1:
                    poker.cambiarTextoEnCarta(3,"cambiar")
                else:
                    poker.cambiarTextoEnCarta(3,"")

            elif h == 4:
                c4 += 1
                if c4 % 2 == 1:
                    poker.cambiarTextoEnCarta(4,"cambiar")
                else:
                    poker.cambiarTextoEnCarta(4,"")

            else:
                break



        if c0 % 2 == 1:
            carta0 = poker.sacarCarta()
            poker.cambiarCarta(0,total(carta0))
            poker.cambiarTextoEnCarta(0,"")
        
        if c1 % 2 == 1:
            carta1 = poker.sacarCarta()
            poker.cambiarCarta(1,total(carta1))
            poker.cambiarTextoEnCarta(1,"")

        if c2 % 2 == 1:
            carta2 = poker.sacarCarta()
            poker.cambiarCarta(2,total(carta2))
            poker.cambiarTextoEnCarta(2,"")

        if c3 % 2 == 1:
            carta3 = poker.sacarCarta()
            poker.cambiarCarta(3,total(carta3))
            poker.cambiarTextoEnCarta(3,"")
        
        if c4 % 2 == 1:
            carta4 = poker.sacarCarta()
            poker.cambiarCarta(4,total(carta4))
            poker.cambiarTextoEnCarta(4,"")


        #para determinar los premios identificamos las cartas con variables


        n0 = numero(carta0)
        n1 = numero(carta1)
        n2 = numero(carta2)
        n3 = numero(carta3)
        n4 = numero(carta4)

        p0 = pinta(carta0)
        p1 = pinta(carta1)
        p2 = pinta(carta2)
        p3 = pinta(carta3)
        p4 = pinta(carta4)


        if (p0 == p1 == p2 == p3 == p4) and (max(n4,n3,n2,n1,n0) == 4 + min(n4,n3,n2,n1,n0)) and (n0 != n1 and n0 != n2 and n0 != n3 and n0 != n4 and n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4):
            poker.mensaje("Escala color")
            creditocompleto = creditocompleto + 50*apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(50*apuesta)

        elif (n3 == n2 == n1 == n0) or (n4 == n2 == n1 == n0) or (n4 == n3 == n1 == n0) or (n4 == n3 == n2 == n0) or (n4 == n3 == n2 == n1):
            poker.mensaje("poker")
            creditocompleto = creditocompleto + 25*apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(25*apuesta)

        elif (n0 == n1 == n2 and n3 == n4) or (n0 == n2 == n3 and n1 == n4) or (n0 == n2 == n4 and n1 == n3) or (n0 ==n1 == n3 and n2 == n4) or (n0 == n1 == n4 and n2 == n3) or (n1 == n3 == n4 and n0 == n2) or (n1 == n2 == n3 and n0 == 4) or (n1 == n2 == n4 and n0 == n3):
            poker.mensaje("Full House")
            creditocompleto = creditocompleto + 9*apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(9*apuesta)
            
        elif (p4 == p3 == p2 == p1 == p0):
            poker.mensaje("Color")
            creditocompleto = creditocompleto + 6*apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(6*apuesta)

        elif (max(n4,n3,n2,n1,n0) == 4 + min(n4,n3,n2,n1,n0)) and (n0 != n1 and n0 != n2 and n0 != n3 and n0 != n4 and n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4):
            poker.mensaje("Escala")
            creditocompleto = creditocompleto + 4*apuesta
            poker.cambiaCredito(creditocompleto)
            aumentarapuesta(4*apuesta)

        elif (n2 == n1 == n0) or (n3 == n2 == n0) or (n4 == n2 == n0) or (n3 == n1 == n0)  or (n4 == n1 ==n0) or (n4 == n3 == n1) or (n3 == n2 ==n1)or (n4 == n2 == n1):
            poker.mensaje("Trio")
            creditocompleto = creditocompleto + 3*apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(3*apuesta)

        elif ((n3 == n2 or n2 == n4 or n3 == n4) and n1 == n0) or ((n3 == n1 or n4 == n1 or n4 == n3) and n2 == n0) or ((n2 == n1 or n4 == n1 or n4 == n2)and n3 == n0) or ((n2 == n1 or n3 == n1 or n3 == n2) and n4 == n0) or ((n3 == n0 or n4 == n0 or n4 == n3) and n2 == n1) or ((n2 == n0 or n4 == n0 or n4 == n2)and n3 == n1) or ((n2 == n0 or n3 == n0 or n3 ==n2) and n4 == n1) or ((n1 == n0 or n4 == n0 or n4 == n1) and n3 == n2) or ((n1 == n0 or n3 == n0 or n3 == n1) and n4 == n2) or ((n1 == n0 or n2 == n0 or n2 == n1) and n4 == n3):
            poker.mensaje("Dos pares")
            creditocompleto = creditocompleto + 2*apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(2*apuesta)

        elif n4 == n3 or n4 == n2 or n3 == n2 or n4 == n1 or n3 == n1 or n2 == n1 or n4 == n0 or n3 == n0 or n2 == n0 or n1 == n0:
            poker.mensaje("Par")
            creditocompleto = creditocompleto + apuesta
            poker.cambiarCredito(creditocompleto)
            aumentarapuesta(apuesta)

        d = poker.preguntar("¿Seguir jugando?")
        if d == False or creditocompleto < 0:
            poker.terminar()


app = pokerGUI.Application(None)
app.title('Video Poker')
app.loadProgram(tarea)
app.start()
