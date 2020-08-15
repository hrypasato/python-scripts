#si tienes python agregado al path
import subprocess
import glob

def py(x): return x.replace(".ui", ".py")
def pyrc(x): return x.replace(".qrc", "_rc.py")

if __name__ == "__main__":
    for ui in glob.glob('*.ui'): #convierte todos los archivos .ui
        subprocess.run("pyuic5 -o "+py(ui)+" "+ui, shell=True)

    for qrc in glob.glob('*.qrc'): #convierte todos los archivos .qrc
        subprocess.run("pyrcc5 -o "+pyrc(qrc)+" "+qrc, shell=True)
