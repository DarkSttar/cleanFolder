from pathlib import Path
import shutil
import sys
from clean_folder import parser_1
from clean_folder.normilized import normalize

def handle_media(file_name: Path, target_folder:Path):
    target_folder.mkdir(exist_ok=True , parents=True)
    file_name.replace(target_folder / normalize(file_name.name))



def handle_archive(file_name: Path, target_folder:Path):
    target_folder.mkdir(exist_ok=True , parents=True)
    #file_name.replace(target_folder / normalize(file_name.name))
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix,''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()




def main(folder: Path):
    parser_1.scan_directory(folder)
    for item in parser_1.JPEG_IMAGES:
        print(f'FIND JPEG ======> {item}')
    for item in parser_1.JPG_IMAGES:
        print(f'FIND JPG ======> {item}')
    for item in parser_1.PNG_IMAGES:
        print(f'FIND PNG ======> {item}')
    for item in parser_1.SVG_IMAGES:
        print(f'FIND SVG ======> {item}')
    for item in parser_1.AVI_VIDEO:
        print(f'FIND AVI ======> {item}')
    for item in parser_1.MP4_VIDEO:
        print(f'FIND MP4 ======> {item}')
    for item in parser_1.MOV_VIDEO:
        print(f'FIND MOV ======> {item}')
    for item in parser_1.MKV_VIDEO:
        print(f'FIND MKV ======> {item}')
    for item in parser_1.DOC_DOCUMENTS:
        print(f'FIND DOC ======> {item}')
    for item in parser_1.DOCX_DOCUEMENTS:
        print(f'FIND DOCX ======> {item}')
    for item in parser_1.TXT_DOCUMENTS:
        print(f'FIND TXT ======> {item}')
    for item in parser_1.PDF_DOCUMENTS:
        print(f'FIND PDF ======> {item}')
    for item in parser_1.XLSX_DOCUMENTS:
        print(f'FIND XLSX ======> {item}')
    for item in parser_1.PPTX_DOCUMENTS:
        print(f'FIND PPTX ======> {item}')
    for item in parser_1.MP3_AUDIO:
        print(f'FIND MP3 ======> {item}')
    for item in parser_1.WAV_AUDIO:
        print(f'FIND WAV ======> {item}')
    for item in parser_1.OGG_AUDIO:
        print(f'FIND OGG ======> {item}')
    for item in parser_1.AMR_AUDIO:
        print(f'FIND AMR ======> {item}')
    for item in parser_1.OTHER_FILES:
        print(f'FIND OTHER FILES ======> {item}')
    for item in parser_1.ARCHIVES_ZIP:
        print(f'FIND ZIP ======> {item}')
    for item in parser_1.ARCHIVES_GZ:
        print(f'FIND GZ ======> {item}')
    for item in parser_1.ARCHIVES_TAR:
        print(f'FIND TAR ======> {item}')
    
    for file in parser_1.JPEG_IMAGES:
        handle_media(file, folder / 'Images' / 'JPEG')  
    for file in parser_1.JPG_IMAGES:
        handle_media(file, folder / 'Images' / 'JPG')
    for file in parser_1.PNG_IMAGES:
        handle_media(file, folder / 'Images' / 'PNG')
    for file in parser_1.SVG_IMAGES:
        handle_media(file, folder / 'Images' / 'SVG')
    for file in parser_1.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser_1.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser_1.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser_1.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')      
    for file in parser_1.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser_1.DOCX_DOCUEMENTS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser_1.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser_1.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser_1.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser_1.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in parser_1.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser_1.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser_1.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser_1.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
    for file in parser_1.OTHER_FILES:
        handle_media(file, folder / 'other')
    for file in parser_1.ARCHIVES_ZIP:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in parser_1.ARCHIVES_GZ:
        handle_archive(file, folder / 'archives' / 'targz')
    for file in parser_1.ARCHIVES_TAR :
        handle_archive(file, folder / 'archives' / 'TAR')
    

    for folder in parser_1.FOLDERS[::-1]:
        try:
            folder.rmdir()
        except OSError:
            print('Error during remove folder {folder}')

def start():
    if sys.argv[1]:
        folder_process = Path(sys.argv[1])
        main(folder_process)

if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process)