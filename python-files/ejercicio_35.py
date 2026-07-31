# -------------------------------------------------------------------------------------------
# KATA 35
#
# Crea la clase UsuarioBanco
# - Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#   corriente.
# - Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# - Código a seguir:
#     a. Inicializar un usuario con nombre, saldo y un indicador (True o False) de
#        cuenta corriente.
#     b. Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error
#        si no es posible.
#     c. Implementar transferir_dinero para transferir dinero desde otro usuario,
#        lanzando un error en caso de fallo.
#     d. Implementar agregar_dinero para aumentar el saldo del usuario.
# - Caso de uso:
#     1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo
#        inicial de 50, ambos con cuenta corriente.
#     2. Agregar 20 unidades al saldo de Bob.
#     3. Transferir 80 unidades de Bob a Alicia.
#     4. Retirar 50 unidades del saldo de Alicia.
# -------------------------------------------------------------------------------------------


class SaldoInsuficienteError(Exception):
    """
    Excepción personalizada: se lanza cuando se intenta retirar o
    transferir dinero sin que el usuario tenga saldo disponible.
    """

    pass


class UsuarioBanco:
    """
    Representa a un usuario de banco. Cada objeto UsuarioBanco tiene su
    propio nombre, saldo y un indicador de si tiene cuenta corriente.
    """

    def __init__(self, nombre, saldo, cuenta_corriente):
        # Estos tres valores se guardan como atributos DE ESTE usuario,
        # es decir, con (self), al crear el objeto.
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Resta "cantidad" del saldo de este usuario.
        Lanzará SaldoInsuficienteError si no hay saldo suficiente.
        """
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(
                f"{self.nombre} no tiene saldo suficiente para retirar {cantidad} "
                f"(saldo actual: {self.saldo})."
            )
        self.saldo -= cantidad  # equivalente a: self.saldo = self.saldo - cantidad

    def agregar_dinero(self, cantidad):
        """Suma "cantidad" al saldo de este usuario."""
        self.saldo += cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere "cantidad" desde ESTE usuario (self) hacia
        "otro_usuario".
        """
        # Esta función reutiliza retirar_dinero(), que ya se encarga de
        # comprobar y lanzar el error si no hay saldo suficiente: si
        # retirar_dinero() lanza la excepción, entonces la línea de agregar_dinero()
        # de abajo nunca llega a ejecutarse (la transferencia se cancela
        # por completo, sin dejar el saldo a medias).

        self.retirar_dinero(cantidad)  # quita el dinero de este usuario
        otro_usuario.agregar_dinero(cantidad)  # se lo añade al otro usuario


if __name__ == "__main__":
    # 1. Crear dos usuarios
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    print(f"Alicia: saldo={alicia.saldo}, cuenta_corriente={alicia.cuenta_corriente}")
    print(f"Bob: saldo={bob.saldo}, cuenta_corriente={bob.cuenta_corriente}")

    # 2. Agregar 20 unidades al saldo de Bob (50 -> 70)
    bob.agregar_dinero(20)
    print(f"\nTras agregar_dinero(20) a Bob: saldo={bob.saldo}")

    # 3. Transferir 80 unidades de Bob a Alicia
    #    Bob solo tiene 70, así que esto DEBE fallar con SaldoInsuficienteError
    print("\nIntentando transferir 80 de Bob a Alicia...")
    try:
        bob.transferir_dinero(alicia, 80)
    except SaldoInsuficienteError as error:
        print("Error:", error)

    print(f"\nSaldo de Bob tras el intento: {bob.saldo}")
    print(f"Saldo de Alicia tras el intento: {alicia.saldo}")

    # 4. Retirar 50 unidades del saldo de Alicia (100 -> 50, ya que la
    #    transferencia anterior no llegó a afectar su saldo)
    alicia.retirar_dinero(50)
    print(f"\nTras retirar_dinero(50) de Alicia: saldo={alicia.saldo}")
