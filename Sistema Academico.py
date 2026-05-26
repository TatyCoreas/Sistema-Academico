import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

# =====================================================================
# 1. VENTANA DE ADMINISTRACIÓN
# =====================================================================
def abrir_panel_administracion():
    admin_win = tk.Tk()
    admin_win.title("Panel de Administración - Sistema Académico")
    admin_win.geometry("800x600")
    admin_win.configure(bg="#EAECEE")
    
    # Barra Superior Azul
    barra_sup = tk.Frame(admin_win, bg="#1B4F72", height=40)
    barra_sup.pack(fill="x")
    tk.Label(barra_sup, text="Panel de Administración - Sistema Académico", fg="white", bg="#1B4F72", font=("Segoe UI", 12, "bold")).pack(pady=8)
    
    # Contenedor Principal (Menú Izquierdo + Contenido Derecho)
    cuerpo = tk.Frame(admin_win, bg="#EAECEE")
    cuerpo.pack(fill="both", expand=True)
    
    # Menú Lateral Izquierdo
    menu_lateral = tk.Frame(cuerpo, bg="#F2F4F4", width=200, bd=1, relief="solid")
    menu_lateral.pack(side="left", fill="y", padx=(10,0), pady=10)
    menu_lateral.pack_propagate(False)
    
    tk.Label(menu_lateral, text="Área personal", font=("Segoe UI", 12, "bold"), bg="#F2F4F4").pack(anchor="w", padx=15, pady=15)
    
    opciones = ["Dashboard General", "Gestión de usuarios", "Control de Materias", "Configuración", "Base de datos"]
    for opc in opciones:
        tk.Radiobutton(menu_lateral, text=opc, font=("Segoe UI", 10), bg="#F2F4F4", value=opc, indicatoron=0, bd=0, anchor="w", padx=10).pack(fill="x", pady=2)
    
    tk.Button(menu_lateral, text="Salir", font=("Segoe UI", 10, "bold"), bg="#C0392B", fg="white", bd=0, command=admin_win.destroy).pack(side="bottom", fill="x", pady=15, padx=15)

    # Área de Trabajo Derecha
    zona_trabajo = tk.Frame(cuerpo, bg="#EAECEE")
    zona_trabajo.pack(side="right", fill="both", expand=True, padx=15, pady=10)
    
    # Formulario Registro de Usuario
    frame_registro = tk.LabelFrame(zona_trabajo, text="Registrar Usuario", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", padx=15, pady=15)
    frame_registro.pack(fill="x", pady=(0, 15))
    
    tk.Label(frame_registro, text="Nombre:", bg="#FFFFFF", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
    tk.Entry(frame_registro, font=("Segoe UI", 10), width=35, bd=1, relief="solid").grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(frame_registro, text="Correo:", bg="#FFFFFF", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
    tk.Entry(frame_registro, font=("Segoe UI", 10), width=35, bd=1, relief="solid").grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(frame_registro, text="Rol:", bg="#FFFFFF", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=5)
    combo_reg_rol = ttk.Combobox(frame_registro, values=["Administrador", "Docente", "Estudiante"], state="readonly", width=32)
    combo_reg_rol.set("Docente")
    combo_reg_rol.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Button(frame_registro, text="Registrar Usuario", bg="#2d5f8b", fg="white", font=("Segoe UI", 10, "bold"), bd=0, width=15).grid(row=0, column=2, rowspan=3, padx=20, ipady=15)

    # Tabla de Usuarios (Treeview Nacio de Tkinter)
    columnas = ("id", "nombre", "correo", "rol", "estado")
    tabla = ttk.Treeview(zona_trabajo, columns=columnas, show="headings", height=8)
    tabla.pack(fill="both", expand=True)
    
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre Completo")
    tabla.heading("correo", text="Correo Electrónico")
    tabla.heading("rol", text="Rol Asignado")
    tabla.heading("estado", text="Estado")
    
    tabla.column("id", width=50, anchor="center")
    tabla.column("nombre", width=180)
    tabla.column("correo", width=200)
    tabla.column("rol", width=100, anchor="center")
    tabla.column("estado", width=90, anchor="center")
    
    # Datos de ejemplo basados en tu captura
    tabla.insert("", "end", values=("01", "Isaac Maldonado", "isaac@universidad.edu", "Docente", "Activo"))
    tabla.insert("", "end", values=("02", "Tatiana Martínez", "tatiana@universidad.edu", "Estudiante", "Activo"))
    tabla.insert("", "end", values=("03", "Beatriz Coreas", "beatriz@universidad.edu", "Docente", "Activo"))
    
    # Botones inferiores de acción
    frame_botones = tk.Frame(zona_trabajo, bg="#EAECEE")
    frame_botones.pack(fill="x", pady=10)
    tk.Button(frame_botones, text="Modificar", bg="#2d5f8b", fg="white", font=("Segoe UI", 10), width=15, bd=0).pack(side="left", ipady=5, padx=20)
    tk.Button(frame_botones, text="Dar de baja", bg="#C0392B", fg="white", font=("Segoe UI", 10), width=15, bd=0).pack(side="right", ipady=5, padx=20)

    admin_win.mainloop()

# =====================================================================
# 2. VENTANA DEL DOCENTE
# =====================================================================
def abrir_panel_docente():
    docente_win = tk.Tk()
    docente_win.title("Panel del Docente - Sistema Académico")
    docente_win.geometry("800x600")
    docente_win.configure(bg="#EAECEE")
    
    # Barra Superior
    barra_sup = tk.Frame(docente_win, bg="#1B4F72", height=40)
    barra_sup.pack(fill="x")
    tk.Label(barra_sup, text="Panel del Docente | Usuario: Isaac Maldonado | Año: 2026", fg="white", bg="#1B4F72", font=("Segoe UI", 11, "bold")).pack(pady=8)
    
    cuerpo = tk.Frame(docente_win, bg="#EAECEE")
    cuerpo.pack(fill="both", expand=True)
    
    # Menú Lateral
    menu_lateral = tk.Frame(cuerpo, bg="#F2F4F4", width=200, bd=1, relief="solid")
    menu_lateral.pack(side="left", fill="y", padx=(10,0), pady=10)
    menu_lateral.pack_propagate(False)
    
    tk.Label(menu_lateral, text="Área personal", font=("Segoe UI", 12, "bold"), bg="#F2F4F4").pack(anchor="w", padx=15, pady=15)
    
    opciones = ["Inicio", "Alumnos", "Evaluaciones", "Asistencia", "Reportes"]
    for opc in opciones:
        tk.Radiobutton(menu_lateral, text=opc, font=("Segoe UI", 10), bg="#F2F4F4", value=opc, indicatoron=0, bd=0, anchor="w", padx=10).pack(fill="x", pady=2)
        
    tk.Button(menu_lateral, text="Salir", font=("Segoe UI", 10, "bold"), bg="#C0392B", fg="white", bd=0, command=docente_win.destroy).pack(side="bottom", fill="x", pady=15, padx=15)

    # Área de Trabajo
    zona_trabajo = tk.Frame(cuerpo, bg="#EAECEE")
    zona_trabajo.pack(side="right", fill="both", expand=True, padx=15, pady=10)
    
    # Selector de materia
    frame_materia = tk.Frame(zona_trabajo, bg="#EAECEE")
    frame_materia.pack(fill="x", pady=10)
    tk.Label(frame_materia, text="Seleccione la materia:", font=("Segoe UI", 11), bg="#EAECEE").pack(side="left", padx=10)
    combo_materia = ttk.Combobox(frame_materia, values=["Analisis de Sistemas II", "Programación Orientada a Objetos", "Bases de Datos"], font=("Segoe UI", 10), state="readonly", width=25)
    combo_materia.set("Analisis de Sistemas II")
    combo_materia.pack(side="left", padx=10)
    
    # Botones de Acción Superior
    frame_acciones = tk.Frame(zona_trabajo, bg="#EAECEE")
    frame_acciones.pack(fill="x", pady=10)
    tk.Button(frame_acciones, text="Registrar Notas", bg="#FFFFFF", fg="#2C3E50", font=("Segoe UI", 10), width=15, bd=1, relief="solid").pack(side="left", padx=40, ipady=4)
    tk.Button(frame_acciones, text="Asistencia", bg="#FFFFFF", fg="#2C3E50", font=("Segoe UI", 10), width=15, bd=1, relief="solid").pack(side="right", padx=40, ipady=4)

    # Tabla de Alumnos Calificaciones
    columnas = ("id", "alumno", "nota1", "nota2", "asistencia")
    tabla = ttk.Treeview(zona_trabajo, columns=columnas, show="headings", height=8)
    tabla.pack(fill="both", expand=True, pady=15)
    
    tabla.heading("id", text="ID")
    tabla.heading("alumno", text="Nombre Alumno")
    tabla.heading("nota1", text="Nota 1")
    tabla.heading("nota2", text="Nota 2")
    tabla.heading("asistencia", text="Asistencia")
    
    tabla.column("id", width=50, anchor="center")
    tabla.column("alumno", width=220)
    tabla.column("nota1", width=80, anchor="center")
    tabla.column("nota2", width=80, anchor="center")
    tabla.column("asistencia", width=90, anchor="center")
    
    tabla.insert("", "end", values=("01", "Tatiana Martínez", "9.0", "8.5", "X"))
    tabla.insert("", "end", values=("02", "Isaac Maldonado", "7.5", "9.0", "X"))
    tabla.insert("", "end", values=("03", "Beatriz Coreas", "9", "8.5", "O"))
    
    tk.Button(zona_trabajo, text="Guardar Cambios", bg="#2d5f8b", fg="white", font=("Segoe UI", 11, "bold"), bd=0, width=20).pack(pady=10, ipady=6)

    docente_win.mainloop()

# =====================================================================
# 3. VENTANA DEL ESTUDIANTE
# =====================================================================
def abrir_panel_estudiante():
    estudiante_win = tk.Tk()
    estudiante_win.title("Panel del Estudiante - Sistema Académico")
    estudiante_win.geometry("800x600")
    estudiante_win.configure(bg="#EAECEE")
    
    # Barra Superior
    barra_sup = tk.Frame(estudiante_win, bg="#1B4F72", height=40)
    barra_sup.pack(fill="x")
    tk.Label(barra_sup, text="Panel del Estudiante | Usuario: Tatiana Martínez | Año: 2026", fg="white", bg="#1B4F72", font=("Segoe UI", 11, "bold")).pack(pady=8)
    
    cuerpo = tk.Frame(estudiante_win, bg="#EAECEE")
    cuerpo.pack(fill="both", expand=True)
    
    # Menú Lateral
    menu_lateral = tk.Frame(cuerpo, bg="#F2F4F4", width=200, bd=1, relief="solid")
    menu_lateral.pack(side="left", fill="y", padx=(10,0), pady=10)
    menu_lateral.pack_propagate(False)
    
    tk.Label(menu_lateral, text="Área personal", font=("Segoe UI", 12, "bold"), bg="#F2F4F4").pack(anchor="w", padx=15, pady=15)
    
    opciones = ["Mi Perfil", "Mis calificaciones", "Asistencia", "Mensajes", "Trámites"]
    for opc in opciones:
        tk.Radiobutton(menu_lateral, text=opc, font=("Segoe UI", 10), bg="#F2F4F4", value=opc, indicatoron=0, bd=0, anchor="w", padx=10).pack(fill="x", pady=2)
        
    tk.Button(menu_lateral, text="Salir", font=("Segoe UI", 10, "bold"), bg="#C0392B", fg="white", bd=0, command=estudiante_win.destroy).pack(side="bottom", fill="x", pady=15, padx=15)

    # Área de Trabajo
    zona_trabajo = tk.Frame(cuerpo, bg="#EAECEE")
    zona_trabajo.pack(side="right", fill="both", expand=True, padx=15, pady=10)
    
    # Ficha del Estudiante
    ficha = tk.LabelFrame(zona_trabajo, text="Información del Alumno", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", padx=15, pady=10)
    ficha.pack(fill="x", pady=(0, 15))
    tk.Label(ficha, text="Estudiante: Tatiana Martínez", font=("Segoe UI", 11, "bold"), bg="#FFFFFF", fg="#2C3E50").pack(anchor="w")
    tk.Label(ficha, text="Carnet: MC20008", font=("Segoe UI", 10), bg="#FFFFFF").pack(anchor="w")
    tk.Label(ficha, text="Carrera: Licenciatura en Informática Educativa", font=("Segoe UI", 10), bg="#FFFFFF").pack(anchor="w")

    # Tabla de Calificaciones
    columnas = ("materia", "promedio", "estado")
    tabla = ttk.Treeview(zona_trabajo, columns=columnas, show="headings", height=6)
    tabla.pack(fill="both", expand=True)
    
    tabla.heading("materia", text="Materia")
    tabla.heading("promedio", text="Promedio")
    tabla.heading("estado", text="Estado")
    
    tabla.column("materia", width=300)
    tabla.column("promedio", width=100, anchor="center")
    tabla.column("estado", width=120, anchor="center")
    
    tabla.insert("", "end", values=("Análisis de Sistemas II", "9.0", "Aprobado"))
    tabla.insert("", "end", values=("Programación Orientada a Objetos", "8.5", "Aprobado"))
    tabla.insert("", "end", values=("Bases de Datos", "9.5", "Aprobado"))
    
    # Botón Boleta
    tk.Button(zona_trabajo, text="Descargar boleta", bg="#2d5f8b", fg="white", font=("Segoe UI", 10, "bold"), bd=0, width=18).pack(pady=15, ipady=5)

    estudiante_win.mainloop()

# =====================================================================
# INTERFAZ PRINCIPAL DE LOGIN (Tu diseño actual)
# =====================================================================
def verificar_credenciales():
    usuario = entrada_usuario.get().strip()
    contrasena = entrada_pass.get().strip()
    rol = combo_rol.get()
    
    # Enrutamiento y destrucción controlada de la ventana de login
    if usuario.lower() == "docente" and contrasena == "1234" and rol == "Docente":
        root.destroy() # Cierra la ventana de login
        abrir_panel_docente() # Abre el panel correspondiente
    elif usuario.lower() == "admin" and contrasena == "admin" and rol == "Administrador":
        root.destroy()
        abrir_panel_administracion()
    elif usuario.lower() == "alumno" and contrasena == "1234" and rol == "Estudiante":
        root.destroy()
        abrir_panel_estudiante()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas o rol equivocado.")

def al_entrar(e):
    btn_login.config(bg="#15314d", fg="white") 

def al_salir(e):
    btn_login.config(bg="#FFFFFF", fg="#1B4F72") 

root = tk.Tk()
root.title("Gestion Academica - Login")
root.geometry("450x670")
root.configure(bg="#15314d")
root.resizable(False, False)

card = tk.Frame(root, bg="#2d5f8b", bd=0)
card.place(relx=0.5, rely=0.5, width=360, height=600, anchor="center")

frame_logo = tk.Frame(card, bg="#2d5f8b")
frame_logo.pack(pady=(20, 0))

ruta_logo = "logo2.png"
if os.path.exists(ruta_logo):
    try:
        img_original = tk.PhotoImage(file=ruta_logo)
        img_redimensionada = img_original.subsample(3, 3) 
        lbl_logo = tk.Label(frame_logo, image=img_redimensionada, bg="#2d5f8b")
        lbl_logo.image = img_redimensionada
        lbl_logo.pack()
    except:
        tk.Label(frame_logo, text="🏫", font=("Segoe UI", 40), bg="#2d5f8b", fg="white").pack()
else:
    tk.Label(frame_logo, text="🏫", font=("Segoe UI", 40), bg="#2d5f8b", fg="white").pack()

tk.Label(card, text="Bienvenidos al Sistema UES", font=("Century Gothic", 15, "bold"), bg="#2d5f8b", fg="white").pack(pady=(10, 20))

estilo_entry = {"font": ("Segoe UI", 11), "bg": "white", "bd": 0, "highlightthickness": 0, "width": 24}

tk.Label(card, text="Usuario", font=("Segoe UI", 10, "bold"), bg="#2d5f8b", fg="#dae8f5").pack(pady=(5, 2))
entrada_usuario = tk.Entry(card, **estilo_entry)
entrada_usuario.pack(ipady=7, pady=(0, 12)) 

tk.Label(card, text="Contraseña", font=("Segoe UI", 10, "bold"), bg="#2d5f8b", fg="#dae8f5").pack(pady=(5, 2))
entrada_pass = tk.Entry(card, show="*", **estilo_entry)
entrada_pass.pack(ipady=7, pady=(0, 12))

tk.Label(card, text="Seleccionar Rol", font=("Segoe UI", 10, "bold"), bg="#2d5f8b", fg="#dae8f5").pack(pady=(5, 2))
combo_rol = ttk.Combobox(card, values=["Administrador", "Docente", "Estudiante"], font=("Segoe UI", 10), state="readonly", width=22)
combo_rol.set("Docente")
combo_rol.pack(ipady=4, pady=(0, 25))

btn_login = tk.Button(card, text="INGRESAR", font=("Segoe UI", 11, "bold"), bg="#FFFFFF", fg="#1B4F72", bd=0, width=20, cursor="hand2", command=verificar_credenciales)
btn_login.pack(ipady=7, pady=5)

btn_login.bind("<Enter>", al_entrar)
btn_login.bind("<Leave>", al_salir)

tk.Label(card, text="¿Perdiste tu contraseña?", font=("Segoe UI", 9), bg="#2d5f8b", fg="#dae8f5", cursor="hand2").pack(pady=(15, 0))
tk.Label(card, text="¿No tienes Cuenta? Regístrate", font=("Segoe UI", 9, "bold"), bg="#2d5f8b", fg="white", cursor="hand2").pack(pady=5)


root.mainloop()