import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
reconhecimento_rosto = mp.solutions.face_detection
reconhecimento = reconhecimento_rosto.FaceDetection()
enquadramento = mp.solutions.drawing_utils

while True:
    resposta, frame = webcam.read()
    if not resposta:
        break
    
    # Reconhece os rostos dentro da imagem
    rostos = reconhecimento.process(frame)

    if rostos.detections:
        for rosto in rostos.detections:
            # Enquadra os rostos na imagem
            enquadramento.draw_detection(frame, rosto)

    cv2.imshow('Detector Aberto!', frame)

    # Apertar ESC fecha o programa
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()