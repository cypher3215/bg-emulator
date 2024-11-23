class CPU:
    def __init__(self):
        # Inicializamos los registros principales de la CPU
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        # La memoria tiene 65536 bytes (2^16), como en un sistema típico de 8 bits
        self.memory = [0] * 65536

    # Instrucciones RES
    def RES_0B0(self):
        """RES 0, B - Resetea el bit 0 del registro B"""
        self.B &= ~(1 << 0)  # Resetea el bit 0 de B
        return 8

    def RES_0B1(self):
        """RES 0, C - Resetea el bit 0 del registro C"""
        self.C &= ~(1 << 0)  # Resetea el bit 0 de C
        return 8

    def RES_0B2(self):
        """RES 0, D - Resetea el bit 0 del registro D"""
        self.D &= ~(1 << 0)  # Resetea el bit 0 de D
        return 8

    def RES_0B3(self):
        """RES 0, E - Resetea el bit 0 del registro E"""
        self.E &= ~(1 << 0)  # Resetea el bit 0 de E
        return 8

    def RES_0B4(self):
        """RES 0, H - Resetea el bit 0 del registro H"""
        self.H &= ~(1 << 0)  # Resetea el bit 0 de H
        return 8

    def RES_0B5(self):
        """RES 0, L - Resetea el bit 0 del registro L"""
        self.L &= ~(1 << 0)  # Resetea el bit 0 de L
        return 8

    def RES_0B6(self):
        """RES 0, (HL) - Resetea el bit 0 del valor en la memoria apuntada por HL"""
        hl = (self.H << 8) | self.L
        self.memory[hl] &= ~(1 << 0)  # Resetea el bit 0 de la memoria
        return 8

    def RES_0B7(self):
        """RES 0, A - Resetea el bit 0 del registro A"""
        self.A &= ~(1 << 0)  # Resetea el bit 0 de A
        return 8

    def RES_1B0(self):
        """RES 1, B - Resetea el bit 1 del registro B"""
        self.B &= ~(1 << 1)
        return 8

    def RES_1B1(self):
        """RES 1, C - Resetea el bit 1 del registro C"""
        self.C &= ~(1 << 1)
        return 8

    def RES_1B2(self):
        """RES 1, D - Resetea el bit 1 del registro D"""
        self.D &= ~(1 << 1)
        return 8

    def RES_1B3(self):
        """RES 1, E - Resetea el bit 1 del registro E"""
        self.E &= ~(1 << 1)
        return 8

    def RES_1B4(self):
        """RES 1, H - Resetea el bit 1 del registro H"""
        self.H &= ~(1 << 1)
        return 8

    def RES_1B5(self):
        """RES 1, L - Resetea el bit 1 del registro L"""
        self.L &= ~(1 << 1)
        return 8

    def RES_1B6(self):
        """RES 1, (HL) - Resetea el bit 1 del valor en la memoria apuntada por HL"""
        hl = (self.H << 8) | self.L
        self.memory[hl] &= ~(1 << 1)  # Resetea el bit 1 de la memoria
        return 8

    def RES_1B7(self):
        """RES 1, A - Resetea el bit 1 del registro A"""
        self.A &= ~(1 << 1)
        return 8

    def RES_2B0(self):
        """RES 2, B - Resetea el bit 2 del registro B"""
        self.B &= ~(1 << 2)
        return 8

    def RES_2B1(self):
        """RES 2, C - Resetea el bit 2 del registro C"""
        self.C &= ~(1 << 2)
        return 8

    def RES_2B2(self):
        """RES 2, D - Resetea el bit 2 del registro D"""
        self.D &= ~(1 << 2)
        return 8

    def RES_2B3(self):
        """RES 2, E - Resetea el bit 2 del registro E"""
        self.E &= ~(1 << 2)
        return 8

    def RES_2B4(self):
        """RES 2, H - Resetea el bit 2 del registro H"""
        self.H &= ~(1 << 2)
        return 8

    def RES_2B5(self):
        """RES 2, L - Resetea el bit 2 del registro L"""
        self.L &= ~(1 << 2)
        return 8

    def RES_2B6(self):
        """RES 2, (HL) - Resetea el bit 2 del valor en la memoria apuntada por HL"""
        hl = (self.H << 8) | self.L
        self.memory[hl] &= ~(1 << 2)  # Resetea el bit 2 de la memoria
        return 8

    def RES_2B7(self):
        """RES 2, A - Resetea el bit 2 del registro A"""
        self.A &= ~(1 << 2)
        return 8

    # Instrucciones SET
    def SET_0B0(self):
        """SET 0, B - Seta el bit 0 del registro B"""
        self.B |= (1 << 0)
        return 8

    def SET_0B1(self):
        """SET 0, C - Seta el bit 0 del registro C"""
        self.C |= (1 << 0)
        return 8

    def SET_0B2(self):
        """SET 0, D - Seta el bit 0 del registro D"""
        self.D |= (1 << 0)
        return 8

    def SET_0B3(self):
        """SET 0, E - Seta el bit 0 del registro E"""
        self.E |= (1 << 0)
        return 8

    def SET_0B4(self):
        """SET 0, H - Seta el bit 0 del registro H"""
        self.H |= (1 << 0)
        return 8

    def SET_0B5(self):
        """SET 0, L - Seta el bit 0 del registro L"""
        self.L |= (1 << 0)
        return 8

    def SET_0B6(self):
        """SET 0, (HL) - Seta el bit 0 de la memoria apuntada por HL"""
        hl = (self.H << 8) | self.L
        self.memory[hl] |= (1 << 0)
        return 8

    def SET_0B7(self):
        """SET 0, A - Seta el bit 0 del registro A"""
        self.A |= (1 << 0)
        return 8

    def SET_1B0(self):
        """SET 1, B - Seta el bit 1 del registro B"""
        self.B |= (1 << 1)
        return 8

    def SET_1B1(self):
        """SET 1, C - Seta el bit 1 del registro C"""
        self.C |= (1 << 1)
        return 8

    def SET_1B2(self):
        """SET 1, D - Seta el bit 1 del registro D"""
        self.D |= (1 << 1)
        return 8

    def SET_1B3(self):
        """SET 1, E - Seta el bit 1 del registro E"""
        self.E |= (1 << 1)
        return 8

    def SET_1B4(self):
        """SET 1, H - Seta el bit 1 del registro H"""
        self.H |= (1 << 1)
        return 8

    def SET_1B5(self):
        """SET 1, L - Seta el bit 1 del registro L"""
        self.L |= (1 << 1)
        return 8

    def SET_1B6(self):
        """SET 1, (HL) - Seta el bit 1 de la memoria apuntada por HL"""
        hl = (self.H << 8) | self.L
        self.memory[hl] |= (1 << 1)
        return 8

    def SET_1B7(self):
        """SET 1, A - Seta el bit 1 del registro A"""
        self.A |= (1 << 1)
        return 8

    def execute_instruction(self, opcode):
        """Ejecuta la instrucción correspondiente al opcode"""
        if opcode == 0x1B0:
            return self.RES_0B0()
        elif opcode == 0x1B1:
            return self.RES_0B1()
        elif opcode == 0x1B2:
            return self.RES_0B2()
        elif opcode == 0x1B3:
            return self.RES_0B3()
        elif opcode == 0x1B4:
            return self.RES_0B4()
        elif opcode == 0x1B5:
            return self.RES_0B5()
        elif opcode == 0x1B6:
            return self.RES_0B6()
        elif opcode == 0x1B7:
            return self.RES_0B7()
        # Continuar con las demás instrucciones
        else:
            print(f"Opcode {opcode} no soportado.")
            return 0

# Ejemplo de uso
cpu = CPU()

# Ejecutar algunas instrucciones
cpu.execute_instruction(0x1B0)  # RES 0, B
cpu.execute_instruction(0x1B7)  # SET 0, A

# Ver los resultados
print(f"Registro B: {bin(cpu.B)}")  # Ver el registro B en formato binario
print(f"Registro A: {bin(cpu.A)}")  # Ver el registro A en formato binario

#Cuando quieras que la CPU ejecute una instrucción, simplemente llamas al método execute_instruction pasando el opcode de la instrucción que deseas ejecutar, como por ejemplo:

#cpu = CPU()
#cpu.execute_instruction(0x1C0)  # Ejecutar SET 0, B