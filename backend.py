import sqlite3 as sql

class IMC:
    def __init__(self,END, peso:float=None, altura:float = None , Imc=None) -> None:
        self.p = peso
        self.a = altura
        self.Imc = Imc
        self.END = END
     
        
    def Calcular(self): 
        #se str no vazia
        if self.p.get() != self.a.get() != '':
           #imc peso / altura * altura 
           peso = self.p.get().replace(',','.')
           altura = self.a.get().replace(',','.')
           try:
                imc = round((float(peso) / (float(altura) ** 2)), 2)
                
                
                if imc < 18.5:
                    self.Imc['text'] = f"IMC: {imc} Abaixo do peso"
                elif imc >= 18.5 and imc < 25:
                    self.Imc['text'] = f"IMC: {imc} Peso normal"
                elif imc >= 25 and imc < 30:
                    self.Imc['text'] = f"IMC: {imc} Sobrepeso"
                elif imc >= 30:
                    self.Imc['text'] = f"IMC: {imc} Obesidade"
           except:
                self.Imc['text'] = "Erro: Insira valores válidos para peso e altura."
                self.a.delete(0, self.END)
                self.p.delete(0, self.END)


class Salva(IMC): 
    def __init__(self, peso:float=None, altura:float = None, imc:list =None) -> None:
        self.altura = altura
        self.peso = peso
        self.imc = imc
        self.criar_db()
        print(self.altura, self.peso, self.imc)
        

    def criar_db(self):
        try:
            conn = sql.connect("imc.db")
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Imc (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        peso REAL,
                        altura REAL,
                        imc REAL
                            )""")
            conn.commit()
        except sql.Error as e:
            print(f'ERROR database:{e}')
        finally:
            if conn:
               conn.close()
    
    def salva_imc(self):
        try:
            conn = sql.connect('imc.db')
            cursor = conn.cursor()
            cursor.execute(" INSERT INTO Imc (peso, altura, imc) VALUES (?, ?, ?)",
                       (float(self.peso), float(self.altura), float(self.imc)))
            conn.commit()
        except sql.Error as e:
            print(f'Error datebase: {e}')
        finally:
            if conn:
                conn.close()
    