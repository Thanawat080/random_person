import generate_face


def generate_image():
    FaceGenerator = generate_face.FaceGenerator
    img = FaceGenerator(1)
    img.gen_face()