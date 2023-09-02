import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk
from tkinter import ttk
from tkinter import font

# Variables globales para almacenar los valores
usuario = None
password = None
diai = None
mesi = None
anoi = None
diaf = None
mesf = None
anof = None
horai = None
minutosi = None
horaf = None
minutosf = None
TiempoMin = None
zonas = None
usar_vpn = 1

zonas_por_region = {
    "Santa Cruz": {
        "El Bajío": "sp_47",
        "Pirai": "sp_48",
        "Grigota": "sp_11",
        "Guapay": "sp_14",
        "Hipermaxi Pampa": "sp_18",
        "La Alemana": "sp_3",
        "Norte": "sp_9",
        "Santos Dumont": "sp_13",
        "Sevilla": "sp_15",
        "Villa 1ro de Mayo": "sp_17",
        "Zona Sur": "sp_1",
        "Equipetrol": "sp_2",
        "Fidalga Pampa": "sp_19"
    },
    "La Paz": {
        "Achumani": "sp_36",
        "Av. Bolivia": "sp_44",
        "Calacoto": "sp_6",
        "El Alto": "sp_12",
        "Irpavi": "sp_35",
        "Miraflores": "sp_10",
        "Multicine Alto": "sp_26",
        "Obrajes": "sp_5",
        "San Pedro": "sp_29",
        "Satélite": "sp_16",
        "Sopocachi": "sp_4",
        "Villa Victoria": "sp_33"
    },
    "Cochabamba": {
        "Colquiri": "sp_41",
        "Plaza Colon": "sp_42",
        "Queru": "sp_8"
    }
}


def enviar_formulario():
    global usuario, password
    global diaf, mesf, anof, diai, mesi, anoi
    global TiempoMin
    global horai, horaf, minutosi, minutosf

    # Asignar los valores a las variables globales
    usuario = str(usuario_entry.get())
    password = str(contraseña_entry.get())
    diai = str(dia_inicial_menu.get())
    mesi = str(mes_inicial_menu.get())
    anoi = str(año_inicial_menu.get())
    diaf = str(dia_final_menu.get())
    mesf = str(mes_final_menu.get())
    anof = str(año_final_menu.get())
    horai = str(hora_inicial_menu.get())
    horaf = str(hora_final_menu.get())
    minutosi = str(minuto_inicial_menu.get())
    minutosf = str(minuto_final_menu.get())
    TiempoMin = str(horas_menu.get())

    # Cerrar la ventana
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingrese sus datos")
ventana.geometry("400x500")

switch_var = tk.IntVar()
switch_var.set(0)  # Inicialmente apagado

# Usuario contraseña
usuario = ttk.Frame(ventana)
usuario.pack(pady=10)

usuario_label = ttk.Label(usuario, text="Usuario:")
usuario_label.pack(side="left")
usuario_entry = ttk.Entry(usuario)
usuario_entry.pack(side="left", padx=5)

contraseña_label = ttk.Label(usuario, text="Contraseña:")
contraseña_label.pack(side="left")
contraseña_entry = ttk.Entry(usuario)
contraseña_entry.pack(side="left", padx=5)

# fechas
dias = [str(i).zfill(2) for i in range(1, 32)]
meses = [str(i).zfill(2) for i in range(1, 13)]
años = [str(i) for i in range(2023, 2051)]

diai = tk.StringVar(value=dias[0])
mesi = tk.StringVar(value=meses[0])
anoi = tk.StringVar(value=años[0])

diaf = tk.StringVar(value=dias[0])
mesf = tk.StringVar(value=meses[0])
anof = tk.StringVar(value=años[0])

#fecha inicial
fechainicial = ttk.Frame(ventana)
fechainicial.pack(pady=5)

fecha_final_label = ttk.Label(fechainicial, text="Fecha Inicial:")
fecha_final_label.pack(side="left")
dia_inicial_menu = ttk.Combobox(fechainicial, values=dias, textvariable=diai, width=3, state="readonly")
dia_inicial_menu.pack(side="left", padx=5)
mes_inicial_menu = ttk.Combobox(fechainicial, values=meses, textvariable=mesi, width=3, state="readonly")
mes_inicial_menu.pack(side="left")
año_inicial_menu = ttk.Combobox(fechainicial, values=años, textvariable=anoi, width=5, state="readonly")
año_inicial_menu.pack(side="left", padx=5)

#fecha final
fechafinal = ttk.Frame(ventana)
fechafinal.pack(pady=5)

fecha_final_label = ttk.Label(fechafinal, text="Fecha Final:")
fecha_final_label.pack(side="left")
dia_final_menu = ttk.Combobox(fechafinal, values=dias, textvariable=diaf, width=3, state="readonly")
dia_final_menu.pack(side="left", padx=5)
mes_final_menu = ttk.Combobox(fechafinal, values=meses, textvariable=mesf, width=3, state="readonly")
mes_final_menu.pack(side="left")
año_final_menu = ttk.Combobox(fechafinal, values=años, textvariable=anof, width=5, state="readonly")
año_final_menu.pack(side="left", padx=5)

#Horas
horas = [str(i).zfill(2) for i in range(24)]
minutos = [str(i).zfill(2) for i in range(60)]

horai = tk.StringVar(value=horas[0])
minutosi = tk.StringVar(value=minutos[0])

horaf = tk.StringVar(value=horas[0])
minutosf = tk.StringVar(value=minutos[0])

#Hora inicial
horainicial = ttk.Frame(ventana)
horainicial.pack(pady=5)

hora_inicial_label = ttk.Label(horainicial, text="Hora Inicial:")
hora_inicial_label.pack(side="left")
hora_inicial_menu = ttk.Combobox(horainicial, values=horas, textvariable=horai, width=5, state="readonly")
hora_inicial_menu.pack(side="left")
puntoshi = ttk.Label(horainicial, text=":")
puntoshi.pack(side="left", padx=5)
minuto_inicial_menu = ttk.Combobox(horainicial, values=minutos, textvariable=minutosi, width=5, state="readonly")
minuto_inicial_menu.pack(side="left")

#Hora final
horafinal = ttk.Frame(ventana)
horafinal.pack(pady=5)

hora_final_label = ttk.Label(horafinal, text="Hora Final:")
hora_final_label.pack(side="left")
hora_final_menu = ttk.Combobox(horafinal, values=horas, textvariable=horaf, width=5, state="readonly")
hora_final_menu.pack(side="left")
puntoshf = ttk.Label(horafinal, text=":")
puntoshf.pack(side="left", padx=5)
minuto_final_menu = ttk.Combobox(horafinal, values=minutos, textvariable=minutosf, width=5, state="readonly")
minuto_final_menu.pack(side="left")

horasch = [str(i) for i in range(1, 9)]
TiempoMin = tk.StringVar(value=horasch[0])
horas = ttk.Frame(ventana)
horas.pack(pady=5)

cantidad_horas_minima_label = ttk.Label(horas, text="Cantidad de Horas Mínima:")
cantidad_horas_minima_label.pack(side="left")
horas_menu = ttk.Combobox(horas, values=horasch, textvariable=TiempoMin, width=5, state="readonly")
horas_menu.pack(side="left", padx=5)

#Frame zonas
def mostrar_zonas(region_seleccionada):
    for widget in frame_zonas.winfo_children():
        widget.pack_forget()

    zonas = zonas_por_region.get(region_seleccionada, {})
    zonas_items = list(zonas.items())

    # Dividir las zonas en grupos de 3
    grupos_de_zonas = [zonas_items[i:i+3] for i in range(0, len(zonas_items), 3)]

    fuente = font.Font(size=12)

    for grupo in grupos_de_zonas:
        fila = tk.Frame(frame_zonas)
        fila.pack(anchor='w')
        
        for zona, codigo in grupo:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(fila, text=zona, variable=var, font=fuente)
            checkbox.pack(side='left', padx=10)  # Ajustar el valor de padx según sea necesario
            zona_checkboxes[codigo] = var

def guardar_zonas():
    global zonas
    zonas_seleccionadas = []
    zonas_seleccionadas = [codigo for codigo, var in zona_checkboxes.items() if var.get() == 1]
    print("Zonas Guardadas Correctamente!!!")
    zonas = zonas_seleccionadas

def cambiar_estado():
    global usar_vpn
    if switch_var.get() == 1:
        switch_var.set(0)
        switch_button.config(bg="red")  # Color cuando está apagado
        usar_vpn = 1
    else:
        switch_var.set(1)
        switch_button.config(bg="green")  # Color cuando está encendido
        usar_vpn = 2

frame_region = tk.Frame(ventana)
frame_region.pack()

frame_zonas = ttk.Frame(ventana)
frame_zonas.pack(pady=5)

zona_checkboxes = {}

regiones = list(zonas_por_region.keys())

opcion_region = tk.StringVar()
opcion_region.set(regiones[0])

region_menu = tk.OptionMenu(frame_region, opcion_region, *regiones, command=lambda x: mostrar_zonas(opcion_region.get()))
region_menu.pack()

boton_guardar = ttk.Button(ventana, text="Guardar Zonas", command=guardar_zonas)
boton_guardar.pack()

switch_button = tk.Button(ventana, text="Usar VPN?", font=("Arial", 12), bg="red", fg="white", command=cambiar_estado)
switch_button.pack(padx=5)

mostrar_zonas(regiones[0])

enviar_boton = ttk.Button(ventana, text="Enviar", command=enviar_formulario)
enviar_boton.pack(padx=10, pady=10)

ventana.mainloop()

# Mostrar los valores en la consola después de cerrar la ventana
print("Iniciando bot con los siguientes valores:")
print("Usuario:", usuario)
print("Contraseña:", password)
print("Fecha Inicial:", f"{diai} {mesi} {anoi}")
print("Fecha Final:", f"{diaf} {mesf} {anof}")
print("Hora Inicial:", f"{horai} : {minutosi}")
print("Hora Final:", f"{horaf} : {minutosf}")
print("Cantidad de Horas Mínima:", TiempoMin)
print("Zonas seleccionadas: ")

for region, zonas_en_region in zonas_por_region.items():
    #print(f"Región: {region}")
    # Recorre las zonas dentro de cada región
    for zona, codigo in zonas_en_region.items():
        # Verifica si el código de la zona está en la lista zonas
        if codigo in zonas:
            print(" ",zona)

#print(zonas)

horainicial = horai+":"+minutosi
horafinal = horaf+":"+minutosf

#Se agregan los limites
TiempoMin1 = int(TiempoMin) + 1
TiempoMin2 = int(TiempoMin) + 2
TiempoMin3 = int(TiempoMin) + 3
TiempoMin4 = int(TiempoMin) + 4
TiempoMin5 = int(TiempoMin) + 5
TiempoMin6 = int(TiempoMin) + 6
TiempoMin7 = int(TiempoMin) + 7

TiempoMin = "("+TiempoMin+"h"
TiempoMin1 = "("+str(TiempoMin1)+"h"
TiempoMin2 = "("+str(TiempoMin2)+"h"
TiempoMin3 = "("+str(TiempoMin3)+"h"
TiempoMin4 = "("+str(TiempoMin4)+"h"
TiempoMin5 = "("+str(TiempoMin5)+"h"
TiempoMin6 = "("+str(TiempoMin6)+"h"
TiempoMin7 = "("+str(TiempoMin7)+"h"

zonas_desicion = 2

if usar_vpn == 1:
    #Inicializamos driver
    #driver_path = 'chromedriver.exe'
    #service = Service(driver_path)
    #driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
elif usar_vpn == 2:
    user_profile = os.path.expanduser('~')
    #print(user_profile)

    # Ruta al directorio de la extensión (donde se encuentra la carpeta de la extensión)
    extension_directory = fr'{user_profile}\AppData\Local\Google\Chrome\User Data\Default\Extensions\dpplabbmogkhghncfbfdeeokoefdjegm\1.10.7_0'

    # Configura las opciones del navegador Chrome para cargar la extensión
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--load-extension={extension_directory}')

    # Inicia el navegador Chrome con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options)

#Tiempo maximo de respuesta
wait = WebDriverWait(driver, 20)

#Define tamaño de ventana
width = 150
height = 640
driver.set_window_size(width, height)

# Definir la posición de la ventana
x = 200
y = 50
driver.set_window_position(x, y)

btn_dia_number = 1
btn_dia_numberi = None
flag_desplazamiento = None
pag_dia = None

def buscar_con_filtros():
    global btn_dia_number
    global btn_dia_numberi
    global zonas_desicion
    global flag_desplazamiento
    global pag_dia

    while True:
        try:
            print("Empezando a buscar con filtros aplicados...")
            wait_busqueda = WebDriverWait(driver, 6)
            archivo = open("agendados.txt", "a")
            c_posis = 0
            while True:
                if diai != diaf: 
                    btn_dia_number = btn_dia_number + 1

                if diai != diaf and pag_dia.text == diaf:
                    btn_dia_number = btn_dia_numberi

                if flag_desplazamiento == 1 and pag_dia.text == diaf:
                    btn_dia.send_keys(Keys.ARROW_LEFT)
                    time.sleep(1)
                    flag_desplazamiento = 0
                    print("Volviendo")

                if flag_desplazamiento == 2 and pag_dia.text == diaf:
                    btn_dia.send_keys(Keys.ARROW_LEFT)
                    time.sleep(1)
                    btn_dia.send_keys(Keys.ARROW_LEFT)
                    time.sleep(1)
                    btn_dia.send_keys(Keys.ARROW_LEFT)
                    flag_desplazamiento = 0
                    print("Volviendo")

                print("Btn_dia_number: ",btn_dia_number)
                pag_dia = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']/div[2]')))
                btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                btn_dia.click()
                print("Dia: "+pag_dia.text+" revisado")

                if (diai == diaf and btn_dia_number == 7) or (diai == diaf and btn_dia_number == 14) or (diai == diaf and btn_dia_number == 21):
                    btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number-1)+']')))
                    btn_dia_sig.click()
                    btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                    btn_dia_actual.click()

                elif btn_dia_number == 7 and pag_dia.text != diaf:
                    btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                    btn_dia.click()
                    btn_dia.send_keys(Keys.ARROW_RIGHT)
                    time.sleep(0.8)
                    flag_desplazamiento = 1
                    print("Desplazandose a semana 2")

                elif btn_dia_number == 14 and pag_dia.text != diaf:
                    btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                    btn_dia.click()
                    btn_dia.send_keys(Keys.ARROW_RIGHT)
                    btn_dia.send_keys(Keys.ARROW_RIGHT)
                    time.sleep(0.8)
                    flag_desplazamiento = 2
                    print("Desplazandose a semana 3")

                elif diai == diaf:
                    btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number+1)+']')))
                    btn_dia_sig.click()
                    btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                    btn_dia_actual.click()

                try:
                    # Agendar
                    btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                    elementos = driver.find_elements(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[3]/div/div[2]/article')
                    c_elementos = len(elementos)
                    print("|-----------------NOTA:-----------------|")
                    print("|Cantidad de horarios disponibles: ", c_elementos," |")
                    print("|Los ",c_elementos," horarios pueden tener cantidad|")
                    print("|de horas inferiores a ", TiempoMin,"            |")
                    print("|---------------------------------------|")
                    for i in range(1, c_elementos+1):
                        txt_turno = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[3]/div/div/article['+str(i)+']/div/div/p')
                        if TiempoMin in txt_turno.text or TiempoMin1 in txt_turno.text or TiempoMin2 in txt_turno.text or TiempoMin3 in txt_turno.text or TiempoMin4 in txt_turno.text or TiempoMin5 in txt_turno.text or TiempoMin6 in txt_turno.text or TiempoMin7 in txt_turno.text:
                            c_posis = c_posis + 1
                            btn_agendar2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[3]/div/div/article['+str(i)+']/div/button')
                            btn_agendar2.click()
                            time.sleep(0.5)
                            print("|Se encontro un horario:|")
                            print("|-----------------------|")
                            try:
                                div_agendado = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[4]/div/aside/div/div[1]')
                                print(div_agendado.text)
                                linea = f"Horario Agendado:\n{div_agendado.text}\n--------------------------\n\n"
                                btn_confirmar = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[4]/div/aside/div/button[1]')
                                btn_confirmar.click()
                                print("Horario "+str(i)+" Agendado!!!")
                                archivo.write(linea)
                            except:
                                div_tomado = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[5]/div/aside/div/div[1]')
                                print(div_tomado.text)
                                linea = f"Horario Tomado:\n{div_tomado.text}\n--------------------------\n\n"
                                btn_tomar = driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[5]/div/aside/div/button[1]')
                                btn_tomar.click()
                                print("Horario "+str(i)+" Tomado!!!")
                                archivo.write(linea)
                            print("|-----------------------|\n")
                    print("Horarios tomados o agendados: ", c_posis)
                except:
                    btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                    print("No hay turnos que coincidan con su filtro")
            archivo.close()
        except:
            driver.back()
            print("Error detectado, volviendo a comenzar")
            cerrar_sesion()
            abrir()

def cerrar_sesion():
    btn_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/header/div/div[1]/button')))
    btn_menu.click()
    btn_cerrar_sesion = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/a[8]')))
    btn_cerrar_sesion.click()

def buscar_sin_filtros():
    global btn_dia_number
    global btn_dia_numberi
    global zonas_desicion
    global flag_desplazamiento
    global pag_dia

    while True:
        try:
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
            div_turnos = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]')))
            txt_no_hay_turnos = "No hay horarios de conexion disponibles para ese día"

            if txt_no_hay_turnos in div_turnos.text:
                print("No hay turnos disponibles")
            else:
                print("Se encontro turnos, aplicando filtros")
                btn_filtros = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div/button[2]')))
                btn_filtros.click()
                input_desde = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/span/div/div[2]/input')))
                input_desde.send_keys(horainicial)
                input_hasta = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/span/div/div[2]/input')))
                input_hasta.send_keys(horafinal)

                if zonas_desicion == 2:
                    for zona in zonas:
                        check_zona = driver.find_element(By.XPATH, '//*[@id="'+zona+'"]')
                        check_zona.click()

                btn_aplicar_filtros = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[2]/div/div[3]/div[1]/button')))
                btn_aplicar_filtros.click()
                buscar_con_filtros()

            if (diai == diaf and btn_dia_number == 7) or (diai == diaf and btn_dia_number == 14) or (diai == diaf and btn_dia_number == 21):
                btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number-1)+']')))
                btn_dia_sig.click()
                btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                btn_dia_actual.click()

            elif btn_dia_number == 7 and pag_dia.text != diaf:
                btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                btn_dia.click()
                btn_dia.send_keys(Keys.ARROW_RIGHT)
                time.sleep(1)
                flag_desplazamiento = 1
                print("Desplazandose a semana 2")

            elif btn_dia_number == 14 and pag_dia.text != diaf:
                btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                btn_dia.click()
                btn_dia.send_keys(Keys.ARROW_RIGHT)
                btn_dia.send_keys(Keys.ARROW_RIGHT)
                time.sleep(1)
                flag_desplazamiento = 2
                print("Desplazandose a semana 3")

            elif diai == diaf:
                btn_dia_sig = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number+1)+']')))
                btn_dia_sig.click()
                btn_dia_actual = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
                btn_dia_actual.click()

            if diai != diaf:
                btn_dia_number = btn_dia_number + 1

            if diai != diaf and pag_dia.text == diaf:
                btn_dia_number = btn_dia_numberi

            if flag_desplazamiento == 1 and pag_dia.text == diaf:
                btn_dia.send_keys(Keys.ARROW_LEFT)
                time.sleep(1)
                flag_desplazamiento = 0
                print("Volviendo")

            if flag_desplazamiento == 2 and pag_dia.text == diaf:
                btn_dia.send_keys(Keys.ARROW_LEFT)
                time.sleep(1)
                btn_dia.send_keys(Keys.ARROW_LEFT)
                time.sleep(1)
                btn_dia.send_keys(Keys.ARROW_LEFT)
                flag_desplazamiento = 0
                print("Volviendo")

            pag_dia = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']/div[2]')))
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
            btn_dia.click()
        except:
            driver.back()
            print("Error detectado, volviendo a comenzar")
            cerrar_sesion()
            abrir()

def ir_a_dia():
    global btn_dia_number
    global btn_dia_numberi
    global pag_dia
    btn_dia_number = 1
    while True:
        pag_dia = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']/div[2]')))
        if pag_dia.text == diai:
            print("Dia inicial correcto")
            break
        elif btn_dia_number == 7:
            #driver.execute_script("arguments[0].scrollLeft = 300;", div_semanas)
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
            btn_dia.click()
            btn_dia.send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)
            print("Desplazandose a semana 2")
            btn_dia_number += 1
        elif btn_dia_number == 14:
            #driver.execute_script("arguments[0].scrollLeft = 600;", div_semanas)
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
            btn_dia.click()
            btn_dia.send_keys(Keys.ARROW_RIGHT)
            btn_dia.send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)
            print("Desplazandose a semana 3")
            btn_dia_number += 1
        else:
            print("Dia inicial incorrecto... Desplazandose a dia ",diai)
            btn_dia_number += 1
            btn_dia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]/button['+str(btn_dia_number)+']')))
            btn_dia.click()

    btn_dia_numberi = btn_dia_number
    buscar_sin_filtros()

def menu_horas():
    btn_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[4]/header/div/div[1]/button')))
    btn_menu.click()
    btn_horas_conexion_disponibles = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div/a[2]')))
    btn_horas_conexion_disponibles.click()
    ir_a_dia()

def iniciar_sesion():
    #Encontramos y mandamos datos de usuario y password
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/form/div/div[1]/input')))
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/form/div/div[2]/input')))
    username_field.send_keys(usuario)
    password_field.send_keys(password)

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/form/button')))
    submit_button.click()
    menu_horas()

#Abrimos la pagina
def abrir():
    if usar_vpn == 2:
        pagina = "https://google.com"
        driver.get(pagina)
        input("Presione Enter cuando configure el Proxy...")
    else:
        pagina = "https://bo.usehurrier.com/app/rooster/web/login"
        driver.get(pagina)

    iniciar_sesion()

abrir()
#Verificar dia
div_semanas = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[1]/div[2]')))

driver.quit()

