import platform

print("*"*50)
info_completa = platform.platform()
print("INFO SISTEMA: ", info_completa)
print("*"*50)

print("*"*50)
ver_os = platform.system()
print("INFO SISTEMA OPERATIVO: ", ver_os)
print("*"*50)

print("*"*50)
release = platform.release()
print("INFO SISTEMA RELEASE: ", release)
print("*"*50)

print("*"*50)
procesador = platform.processor()
print("INFO PROCESADOR: ", procesador)
print("*"*50)

print("*"*50)
arquitectura = platform.machine()
print("INFO ARQUITECTURA: ", arquitectura)
print("*"*50)

print("*"*50)
ver_python = platform.python_version()
print("Ver Python: ", ver_python)
print("*"*50)