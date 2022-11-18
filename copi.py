import os

descargasfolder = "D:/DOWNLOAD/"
rarfolder = "D:/DOWNLOAD/RAR/"
fotosfolder = "D:/DOWNLOAD/FOTOS/"
exefolder = "D:/DOWNLOAD/EXE/"
torrentfolder = "D:/DOWNLOAD/TORRENT/"
pdfolder = "D:/DOWNLOAD/PDF/"
otrosfolder = "D:/DOWNLOAD/OTROS/"

if __name__=="__main__":

	for filename in os.listdir(descargasfolder):
		nombre, extension = os.path.splitext(descargasfolder + filename)

		if extension in [".zip", ".rar"]:
			os.rename(descargasfolder + filename,rarfolder + filename)

		if extension in [".jpg",".png"]:
			os.rename(descargasfolder + filename, fotosfolder + filename)

		if extension in [".exe",".msi"]:
			os.rename(descargasfolder + filename, exefolder + filename)

		if extension in [".torrent"]:
			os.rename(descargasfolder + filename, torrentfolder + filename)

		if extension in [".pdf"]:
			os.rename(descargasfolder + filename, pdfolder + filename)

		if descargasfolder+filename in ["D:/DOWNLOAD/RAR","D:/DOWNLOAD/FOTOS", "D:/DOWNLOAD/EXE", "D:/DOWNLOAD/TORRENT", "D:/DOWNLOAD/PDF", "D:/DOWNLOAD/OTROS"]:
			print(descargasfolder+filename)
		else:
			os.rename(descargasfolder + filename, otrosfolder + filename)