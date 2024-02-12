import logging
from fhirclient import client
settings = {
    'app_id': '3708f01857cc2d7864d6108f690a9e80',
    'api_base': 'https://chatgp-server.fhir.azurehealthcareapis.com/'
}
smart = client.FHIRClient(settings=settings)

# import fhirclient.models.patient as p
# patient = p.Patient.read('hca-pat-1', smart.server)
# birth_date = patient.birthDate.isostring
# # '1963-06-12'
# smart.human_name(patient.name[0])
# # 'Christy Ebert'
