from time import sleep
import os

def create_path():
    
    global current_dir
    global output_folder
    global path
    global create_folders

    create_folders = False

    if not os.path.exists('COMPROVANTES'):
        os.mkdir('COMPROVANTES')
        create_folders = True    

    current_dir = f'{os.getcwd()}/COMPROVANTES'
    
    if not os.path.exists(f'{current_dir}/TED'):
        os.mkdir(f'{current_dir}/TED')

    if os.path.exists(f'{current_dir}/TED/dump'):
        for item in os.listdir(f'{current_dir}/TED/dump'):
            os.remove(f'{current_dir}/TED/dump/{item}')
        os.rmdir(f'{current_dir}/TED/dump')
        os.mkdir(f'{current_dir}/TED/dump')
    else:
        os.mkdir(f'{current_dir}/TED/dump')

    if not os.path.exists(f'{current_dir}/PIX'):
        os.mkdir(f'{current_dir}/PIX')

    if os.path.exists(f'{current_dir}/PIX/dump'):
        for item in os.listdir(f'{current_dir}/PIX/dump'):
            os.remove(f'{current_dir}/PIX/dump/{item}')
        os.rmdir(f'{current_dir}/PIX/dump')
        os.mkdir(f'{current_dir}/PIX/dump')
    else:    
        os.mkdir(f'{current_dir}/PIX/dump')

    if not os.path.exists(f'{current_dir}/BOLETO'):
        os.mkdir(f'{current_dir}/BOLETO')

    if os.path.exists(f'{current_dir}/BOLETO/dump'):
        for item in os.listdir(f'{current_dir}/BOLETO/dump'):
            os.remove(f'{current_dir}/BOLETO/dump/{item}')
        os.rmdir(f'{current_dir}/BOLETO/dump')
        os.mkdir(f'{current_dir}/BOLETO/dump')
    else:    
        os.mkdir(f'{current_dir}/BOLETO/dump')

    if not os.path.exists(f'{current_dir}/SEPARADOS'):
        os.mkdir(f'{current_dir}/SEPARADOS')

    output_folder = f'{current_dir}/SEPARADOS'

    path = f'{current_dir}/COMPROVANTES'

    if create_folders:
        print('Bem-vindo ao nosso programa. Criando as pastas necessárias...')
        sleep(1)
        print('...')
        sleep(2)
        print('...')
        sleep(3)
        print('As pastas necessárias foram criadas. Insira os arquivos com a lista de comprovantes na pasta COMPROVANTES em seu respectivo tipo de pagamento e execute o programa novamente.')
        exit()
    
if __name__ == '__main__':
    create_path()
    
    import src.ted
    import src.pix
    import src.boleto

