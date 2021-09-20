import subprocess

contenido=input()

#bin\dot.exe -Tpng eje.txt -o le.png
f = open ('NomT.txt','w')
                
f.write(contenido)
f.close()
subprocess.run('bin\dot.exe -Tpng NomT.txt -o NomT.png')
print("Imagen generada")
