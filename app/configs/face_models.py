from enum import StrEnum


class FaceDetectionModels(StrEnum):
    VGGFace = ("VGG-Face",)
    Facenet = ("Facenet",)
    Facenet512 = ("Facenet512",)
    OpenFace = ("OpenFace",)
    DeepFace = ("DeepFace",)
    DeepID = ("DeepID",)
    ArcFace = ("ArcFace",)
    Dlib = ("Dlib",)
    SFace = ("SFace",)
    GhostFaceNet = "GhostFaceNet"
