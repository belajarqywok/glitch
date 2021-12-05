import os
import sys
import imageio
import glitchart

class create_jpg :

    def __init__(self, filename, stock, asset, output) -> None :

        os.system(f"mkdir {asset}")

        self.asset     = asset
        self.stock     = stock
        self.output    = output
        self.filename  = filename

    def generate_glitch_image(self) -> bool :

        size       = 0
        percentage = 0

        for index_jpg in range(self.stock) :

            glitchart.jpeg(f"{self.filename}")

            os.system(f"mv {self.filename[0:len(self.filename)-4]}_glitch.jpg {index_jpg+1}.jpg")
            os.system(f"mv {index_jpg+1}.jpg {self.asset}")

            size += os.path.getsize(f"{self.asset}/{index_jpg+1}.jpg")

            percentage += 1

            print(f"generate [ \033[94m{index_jpg + 1} / {self.stock}\033[0m ] [ \033[96m{int((percentage/self.stock)*100)} %\033[0m ] ..................... [ total size : \33[33m{size/1024000} MB\033[0m ]")
            
        return True

    def generate_image_to_gif(self) -> None :

        os.system('cls')

        images     = []
        filenames  = os.listdir(self.asset)

        for filename in filenames:

            images.append(imageio.imread(f"{self.asset}/{filename}"))

            print(f"images initialization [ \033[94m{len(images)} / {len(filenames)}\033[0m ] ............................... [ \33[33m{int((len(images)/len(filenames))*100)} %\033[0m ]")

        os.system('cls')

        print(f"[ PLEASE WAIT ........................ ]")

        imageio.mimsave(f"{self.output}", images)

        os.system(f"rm -irf {self.asset}")

        os.system('cls')
        
        print(f"\n[ generate \033[94m{self.output}\033[0m ] ................... \033[92msuccess\033[0m [ size : {os.path.getsize(self.output)/1024000} MB ]\n")

if __name__ == "__main__" :

    create = create_jpg(

        filename = sys.argv[1],
        stock    = int(sys.argv[2]),
        asset    = sys.argv[3],
        output   = sys.argv[4]

    )

    if create.generate_glitch_image() :

            create.generate_image_to_gif()

# python glitch.py blabla.jpg 50 asset blabla.mp4
