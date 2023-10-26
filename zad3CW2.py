import requests

def get_molecule_data_from_pdbe(pdb_id):
    return requests.get(f'https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{pdb_id}').json()


def sekwencja(pdb_id, chain_id):
  data = get_molecule_data_from_pdbe(pdb_id)


  if pdb_id in data:
    dataOkrojone = data[pdb_id]
    molecule = dataOkrojone.get('molecules', [])

    for entity in molecule:
      molecule_type = entity.get('molecule_type',"")
      in_chains = entity.get('in_chains',[])
      sequence = entity.get('sequence',"") 
      dlugosc = entity.get('residue_range', [])

      if entity["molecule_type"] == "polypeptide(L)" and chain_id in entity["in_chains"] :
        start = dlugosc[0]
        end = dlugosc[1]
        wynik = sequence[start - 1:end]
        return sequence

print(sekwencja)