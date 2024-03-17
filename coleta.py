import requests
import os
import zipfile
import shutil


lista_nomes = {#'3913' : 'JEANDRO ALMEIDA',
# '3809' : 'ERINALDO SOARES DOS SANTOS',
# '3914' : 'CESAR HENRIQUE NUNES',
'3808' : 'ROBERTO CARVALHO DA SILVA',
# '6063' : 'LEANDRO PEREIRA BARBOSA',
# '4951' : 'OTAVIO SILVA',
# '4439' : 'RONALDO TAVARES BARROS',
# '3915' : 'ELIAS MARCELINO DE SOUZA',
# '2560' : 'ROSANGELA RODRIGUES NUNES',
# '6064' : 'DENISTOCRES DOS ANJOS CORREA',
# '3810' : 'MARCELO ROBERTO DA SILVA',
# '2282' : 'CELSO LUIZ PERO GONCALVES DA MOTTA',
# '2281' : 'EUZENI PEREIRA NAVERO DA SILVA',
'483' : 'VAGNER DA SILVA BRITO',
# '2950' : 'EDGAR GUTIERREZ',
# '1307' : 'RICARDO DOS SANTOS',
'484' : 'KLEBER VIEIRA',
# '1306' : 'ANA CAROLINA SILVEIRA FALCO',
'3370' : 'GABRIEL DA SILVA LOPES SOUSA',
'1308' : 'ADAM FABRICIO SILVEIRA SILVA',
# '2986' : 'PAULO CESAR GUARENGHI',
# '883' : 'MARILUCIA DOS SANTOS MOTTA',
# '2559' : 'JOAO SEVERIANO DA NOVA',
# '620' : 'SOLANGE MOREIRA DE CARVALHO'
}

if not os.path.exists(os.path.join('fotos')):
  os.mkdir(os.path.join('fotos'))

for id, nome in lista_nomes.items():
  print(f'Buscando {nome}')
  response = requests.get(f'https://fotop.com.br/fotos/eventos/busca/id/{id}/evento/85467/busca/numero')

  lista_fotos = []

  if response.status_code == 200:
    for line in response.text.splitlines():
      if 'img class="fotoDarkBlur"' in line:
        lista_fotos.append(line.split()[2][4:].replace('"',''))
  else:
    print('Error:', response.status_code)

  print(f'{len(lista_fotos)} fotos')

  if not os.path.exists(os.path.join('fotos', f'{id}_{nome.split()[0]}')):
    os.mkdir(os.path.join('fotos', f'{id}_{nome.split()[0]}'))

  for id_foto, foto in enumerate(lista_fotos[:2], 1):
      req = requests.get(foto)
      with open(os.path.join('fotos',
                             f'{id}_{nome.split()[0]}',
                             str(id_foto)+'.jpeg'),'wb') as file:
          file.write(req.content)

  shutil.make_archive(os.path.join('fotos', f'{id}_{nome.split()[0]}'), 
                      'zip', 
                      os.path.join('fotos', f'{id}_{nome.split()[0]}'))