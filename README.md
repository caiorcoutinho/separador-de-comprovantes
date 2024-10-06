# separador-de-comprovantes
 Separa e nomeia comprovantes de pagamento via TED, PIX e BOLETO do banco Bradesco através de reconhecimento óptico de caracteres (OCR) e visão computacional.

# COMO USAR
 Execute o programa pela primeira vez. Ele irá criar as pastas necessárias e orientar as pastas onde inserir os PDFs com os comprovantes e executar novamente.
 Insira os comprovantes nas pastas COMPROVANTES/TED, COMPROVANTES/PIX e COMPROVANTES/BOLETO. Os arquivos precisam estar em formato PDF.
 Ao executar o programa, os comprovantes serão convertidos e separados um a um, nomeados no seguinte formato:
 TED_NOME DO BENEFICIÁRIO_VALOR.pdf
 PIX_NOME DO BENEFICIÁRIO_VALOR_DESCRIÇÃO.pdf
 BOLETO_NOME DO BENEFICIÁRIO_VALOR_DESCRIÇÃO.pdf

# DEPENDÊNCIAS
 O programa precisa da instalação do Tesseract na pasta C:/ProgramFiles/Tesseract-OCR/Tesseract.exe
 Também usa o poppler, mas este já está iserido na pasta SRC

# COMO FUNCIONA
 Ao ser executado, o programa transforma PDFs com várias páginas de comprovantes de pagamento em comprovantes individuais, localizados na pasta COMPROVANTES/SEPARADOS.
 Para realizar esse processo, inicialmente separa as páginas do PDF e salva como imagem JPG nas pastas "dump" dentro do diretório de cada tipo de pagamento. A cada execução do programa os arquivos presentes nessas pastas são apagados antes da nova separação.
 Após isso, o programa realiza a leitura dos campos de nome do destinatário/beneficiário, valor e descrição (se houver), e usa para nomear os arquivos e salvar na pasta de destino.

 # AUTOR
  Caio Ricardo B. C. Santos
  Salvador/BA
 
