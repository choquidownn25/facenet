import cv2
from serpapi import GoogleSearch
import os
import webbrowser
import urllib.parse

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
    buscar_foto_en_internet(nombre_archivo)


def buscar_foto_en_internet(ruta_imagen):
    # Configuración de la búsqueda inversa
    params = {
        "engine": "google_lens",
        "url": "https://api.imgbb.com",  # Google Lens requiere una URL pública
        "api_key": "7de8ce6e88719c0d33ea0931b92fd6711961272d"
    }

    # Si no tienes URL y quieres subir el archivo local directamente:
    # Nota: Algunos servicios requieren que la imagen esté en la nube (S3, Imgur, etc.)

    search = GoogleSearch(params)
    results = search.get_dict()

    # Extraer resultados visuales
    if "visual_matches" in results:
        print("--- Resultados encontrados en la web ---")
        for match in results["visual_matches"][:5]:  # Mostrar los primeros 5
            print(f"Título: {match.get('title')}")
            print(f"Enlace: {match.get('link')}")
            print("-" * 20)
    else:
        print("No se encontraron coincidencias exactas.")


# Ejecutar búsqueda
# buscar_foto_en_internet("foto_capturada.jpg")

def abrir_busqueda_visual(ruta_local):
    # Google Images permite buscar por URL.
    # Para archivos locales, lo más fácil es usar la función de "Subir" de Bing o Google.
    print("Abriendo navegador para búsqueda inversa...")
    url_base = "https://www.google.com"
    # Nota: Esto funciona mejor si la imagen ya está en internet.
    webbrowser.open(f"https://lens.google.com")

if __name__ == "__main__":
    capturar_foto()