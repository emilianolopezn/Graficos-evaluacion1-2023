from OpenGL.GL import *
import glfw

def dibujar():
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()

def main():
    #inicia glfw
    if not glfw.init():
        return
    ancho = 500
    alto = 500
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL


 

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)


    while not glfw.window_should_close(window):
        
        #Establece color de borrado
        glClearColor(0.4,0.8,0.1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()