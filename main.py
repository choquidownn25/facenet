import cv2
def capturar_foto(nombre_archivo="mama1.jpg"):
    # 1. Iniciar la cámara (0 es la cámara por defecto)
    camara = cv2.VideoCapture(0)

    if not camara.isOpened():
        print("No se pudo acceder a la cámara")
        return

    print("Presiona 's' para capturar la foto o 'q' para salir.")

    while True:
        # Leer el frame de la cámara
        ret, frame = camara.read()

        if not ret:
            break

        # Mostrar el video en una ventana
        cv2.imshow("Captura de Rostro - FaceNet", frame)

        # Esperar a que el usuario presione una tecla
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Guardar la imagen en el disco
            cv2.imwrite(nombre_archivo, frame)
            print(f"¡Foto guardada como {nombre_archivo}!")
            break
        elif key == ord('q'):
            print("Captura cancelada.")
            break

    # Liberar recursos
    camara.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capturar_foto()