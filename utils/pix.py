import qrcode

def generate_pix_qr_code():
    pix_link = '00020126700014br.gov.bcb.pix01364491969f-5b26-4fe0-914d-2534127eb32702081 Ticket52040000530398654049.995802BR5924Vitor Antonio da Conceic6008Brasilia62090505dkdph63041159'

    qr = qrcode.make(pix_link)
    return qr
