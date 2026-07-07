class Anime:
    def __init__(self, id, slug , titulo, imagen, sinopsis_corta, sinopsis_larga, video_url):
        self.id = id
        self.slug = slug
        self.titulo = titulo
        self.imagen = imagen
        self.sinopsis_corta = sinopsis_corta
        self.sinopsis_larga = sinopsis_larga
        self.video_url = video_url

    def to_dict(self):
        return self.__dict__