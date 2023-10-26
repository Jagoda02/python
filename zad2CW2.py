import requests

def get_best_structure_data_from_pdbe(accession):
    data = requests.get(f"https://www.ebi.ac.uk/pdbe/graph-api/mappings/best_structures/{accession}").json()
    
    structureN = dict()
    coverageN = 0
    
    if accession in data:
        for structureA in data[accession]:
            if 'coverage' in structureA and 'resolution' in structureA:
                coverageA = structureA['coverage']
                resolution = structureA['resolution']
                
                
                if coverageA > coverageN:
                    structureN = structureA
                    coverageN = coverageA

                elif coverageA == coverageN and resolution < structureN['resolution']:
                    structureN = structureA
                    coverageN = coverageA
        
         
            pdb_id = structureN['pdb_id']
            chain_id = structureN['chain_id']
            unp_start = structureN['unp_start']
            unp_end = structureN['unp_end']
            
            wynik = {pdb_id: {'chain_id': chain_id, 'unp_start': unp_start, 'unp_end': unp_end}}
            return wynik
   

data = get_best_structure_data_from_pdbe("Q9NR28")
print(data)

