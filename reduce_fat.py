from PIL import Image

list = [
  'agenda.png',
  'counter.png',
  'papapabit.png',
  's4htb.png',
  'trofeos.png',
  'badges.png',
  'cv-classic-mode.png',
  'keepwebsimple.png',
  'particle.png',
  'sale.png',
  'blog.png',
  'eleveNmaps.png',
  'matrix.png',
  'portfolio-personal.png',
  'text-trail.png',
  'coffe-website-dos.jpg',
  'igallery.jpg',
  'matrix2.png',
  'proffesional.png', 
  'the-substance.png',
  'coffe-website-uno.png',
  'igallery.png',
  'nft-landing.png',
  'responsive-portfolio.png',
  'todo.png',
]

def _reduce_fat(name: str) -> None:
  imagen = Image.open(name)
  imagen = imagen.convert('RGB')
  imagen.save(f'new/{name}.jpg', quality=30)


def main():
  for i in range(len(list)):
    _reduce_fat(list[i])

if __name__ == '__main__':
  main()
