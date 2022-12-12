# importa as bibliotecas necessárias
import PyPDF2
import re

# Abre o arquivo pdf
# lembre-se que para o windows você deve usar essa barra -> /
# lembre-se também que você precisa colocar o caminho absoluto
pdf_file = open('pdf/ameaca.pdf', 'rb')

# Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()

n = 0

info = {}

for nPage in range(number_of_pages):

    # lê a primeira página completa
    page = read_pdf.getPage(nPage)

    # extrai apenas o texto
    page_content = page.extractText()

    # faz a junção das linhas
    parsed = ''.join(page_content).strip()

    arr = parsed.split('\n')
    """
      print("\n\n ########## Sem eliminar as quebras de linha ##########\n\n")
      print(parsed)

      # remove as quebras de linha
      parsed = re.sub('n', '', parsed).strip()
      print("\n\n########## Após eliminar as quebras ##########\n\n")
      print(parsed)

      print("\n\n########## Pegando apenas as 20 primeiras posições ##########\n\n")
      novastring = parsed[0:200]
      print(novastring)

      print("\n\n########## Pegando apenas as 20 primeiras posições ##########\n\n")
      """
    for x in arr:
        num = str(n).zfill(5)

        info[n] = x.strip()

        print(num + ') ' + x.strip())
        n = n + 1
