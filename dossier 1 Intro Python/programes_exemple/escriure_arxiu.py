edat=int(input('Digues quants anys fas aquest any?'))
year = 2022-edat
arxiu=open('Dades.txt','wt')
arxiu.write('Vas néixer el ' + str(year))
arxiu.close()