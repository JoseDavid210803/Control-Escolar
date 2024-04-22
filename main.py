# main ejecutable
# los print() son únicamente para visualizar la ejecución del código y localizar errores

# Para iniciar, se necesita tener instalados:
# python -m pip install mysql-connector-python
# python.exe -m pip install --upgrade pip

import time

from app.login_app import AppLogin

if __name__ == "__main__":
    start = time.time()
    print("Executing...\n")

    login = AppLogin()
    login.mainloop()

    print("\nFinishing...")
    end = time.time()
    print(f"\nProgram working during {(end-start):.2f} seconds\n")