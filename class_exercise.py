#Class Exercise
class Line:
    def __init__(self, point_start:list, point_end:list):
        self.point_start = point_start
        self.point_end = point_end
    def compute_length(self):
        length = (float(self.point_end[0] - self.point_start[0])**2 +
                  float(self.point_end[1] - self.point_start[1])**2)**(1/2)
        return length
    def compute_slope(self):
        if (self.point_end[0] - self.point_start[0]) == 0:
            print("Esta línea es vertical, su pendiente está indefinida")
            return None
        else:
            slope = (float(self.point_end[1] - self.point_start[1])/
                  float(self.point_end[0] - self.point_start[0]))
            return slope
    def compute_horizontal_cross(self): #está complicado de entender
#pero este if verifica que los signos de los Y de los puntos sean contrarios o alguno sea 0
        primer_y = '-' in str(self.point_start[1])
        segundo_y = '-' in str(self.point_end[1])
        alguno = primer_y or segundo_y #(debe retornar True)
        ambos = primer_y and segundo_y #(debe retornar False)
        if ((alguno == True and ambos == False)
            or(self.point_start[1] == 0 or self.point_end[1] == 0)) :
            return True
        else:
            return False
    def compute_vertical_cross(self): #se aplica la misma lógica que el anterior con los X de los puntos
        primer_y = '-' in str(self.point_start[0])
        segundo_y = '-' in str(self.point_end[0])
        alguno = primer_y or segundo_y #(debe retornar True)
        ambos = primer_y and segundo_y #(debe retornar False)
        if ((alguno == True and ambos == False)
            or(self.point_start[0] == 0 or self.point_end[0] == 0)) :
            return True
        else:
            return False
class Rectangle:
    def __init__(self,linea_1: "Line", linea_2: "Line",linea_3: "Line", linea_4: "Line"):
        self.linea_horizontal = linea_1 #inferior
        self.linea_vertical = linea_2 #izquierda
        self.linea_horizontal_2 = linea_3 #superior
        self.linea_vertical_2 = linea_4 #derecha
        #se validan las líneas de entrada
        horizontales = ((self.linea_horizontal != self.linea_horizontal_2) 
            and ( self.linea_horizontal.compute_slope() == 0 and 
                 self.linea_horizontal_2.compute_slope() == 0))
        verticales = ((self.linea_vertical != self.linea_vertical_2) 
            and (self.linea_vertical.compute_slope() == None and 
                 self.linea_vertical_2.compute_slope() == None))
        if not (horizontales and verticales ):
            print("ingrese lineas válidas")
        else: #aquí se verifica que compartan vertices
            #*la solución que está a continuación es muy estricta así que solo sirve para algunos rectángulos
            """
            lado_izquierdo = (self.linea_horizontal.point_start[0] == 
                              self.linea_vertical.point_start[0] == 
                              self.linea_horizontal_2.point_start[0])
            lado_derecho = (self.linea_horizontal.point_end[0] == 
                            self.linea_vertical_2.point_start[0] == 
                            self.linea_horizontal_2.point_end[0])
            lado_superior = (self.linea_horizontal.point_start[1] == 
                             self.linea_vertical_2.point_start[1] == 
                             self.linea_horizontal_2.point_start[1])
            lado_inferior = (self.linea_horizontal.point_end[1] == 
                             self.linea_vertical.point_start[1] == 
                             self.linea_horizontal_2.point_end[1])
            self.validador = (lado_izquierdo and lado_derecho) and (lado_superior and lado_inferior)
            """
            #* la solución a continuación es más universal aunque sinceramente me la dió copilot
            puntos = [
                tuple(self.linea_horizontal.point_start), tuple(self.linea_horizontal.point_end),
                tuple(self.linea_vertical.point_start), tuple(self.linea_vertical.point_end),
                tuple(self.linea_horizontal_2.point_start), tuple(self.linea_horizontal_2.point_end),
                tuple(self.linea_vertical_2.point_start), tuple(self.linea_vertical_2.point_end)
                    ]
            self.validador = len(set(puntos)) == 4 and horizontales and verticales #el set(puntos) quita los duplicados
    def compute_area(self):
        if self.validador == True:
            area = self.linea_horizontal.compute_length()*self.linea_vertical.compute_length()
            return area
        else: return "ingrese líneas válidas"
    def compute_perimeter(self):
        if self.validador == True:
            perimeter = (self.linea_horizontal.compute_length()*2 
                            + self.linea_vertical.compute_length()*2)
            return perimeter
        else: return "ingrese líneas válidas"
point_1 = [-10,10]
point_2 = [-20,0]
linea = Line(point_1,point_2)
linea.compute_length()
linea.compute_slope()
linea.compute_horizontal_cross()
linea.compute_vertical_cross()

p1 = [0, 0]    # esquina inferior izquierda
p2 = [4, 0]    # esquina inferior derecha
p3 = [0, 3]    # esquina superior izquierda
p4 = [4, 3]    # esquina superior derecha

linea_inferior = Line(p1, p2)    
linea_izquierda = Line(p1, p3)   
linea_superior = Line(p3, p4)   
linea_derecha = Line(p2, p4) 

rectangulo = Rectangle(linea_inferior, linea_izquierda, linea_superior, linea_derecha)

rectangulo.compute_area()