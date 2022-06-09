def get_placemarkers(city):

    from zipfile import ZipFile
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    dict_city = {'Anchorage':r'\\ANC-FS\ANC-Projects\Geotech\Red Files\GIS\Anchorage\Anchorage Redfiles 2-19-2020.kmz',
    'Bethel':r'\\ANC-FS\ANC-Projects\Geotech\Red Files\GIS\Bethel\Bethel_redfiles-12-2017.kmz'}
    kmz = ZipFile(dict_city[city], 'r')
    kml = kmz.open('doc.kml', 'r').read()
    soup = bs(kml, features="xml")

    dict_placemarks = {'id':[],'lat':[],'lon':[],'projectname':[],'file':[]}
    for el in soup.findAll('Document'):
        for folder in el.findAll('Folder'):
            for placemark in folder.findAll('Placemark'):
                coords = str(placemark.findAll('Point')[0].findAll('coordinates')[0])
                dict_placemarks['lon'].append(coords[coords.find(' ')+1:coords.find(',')])
                dict_placemarks['lat'].append(coords[coords.find(',')+1:coords.find(',',coords.find(',')+1)])
                
                desc = placemark.findAll('description')[0].get_text()
                dict_placemarks['projectname'].append(desc[desc.find('<td>Project</td>')+len('<td>Project</td>'):desc.find('</tr>',desc.find('<td>Project</td>')+1)][7:-8])
                dict_placemarks['file'].append(desc[desc.find('<td>File</td>')+len('<td>File</td>'):desc.find('</tr>',desc.find('<td>File</td>')+1)][7:-8])

                dict_placemarks['id'].append(placemark.attrs['id'])
    df_placemarks = pd.DataFrame(dict_placemarks)
    return df_placemarks