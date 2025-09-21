import uuid
from datetime import datetime, timedelta, time, date
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.call import Call, CallStatus

# Pré-remplir les IDs à utiliser (copie ceux de tes données existantes)
user_ids = [
    "32ce235d-5d4f-4b06-ad91-acd40c9b5bc3",
    "b89003f1-2412-4a36-933a-39cb83803a81",
    "ee28cdba-2547-42a0-b666-e2fb2c3c21aa",
    "2d4136c6-4754-4945-bc12-3efed17a70ee",
    "66bdf39b-b99b-49d8-8109-c4cd5638deb8",
    "a2a37e46-aeb2-4bd1-9bb6-18b4f433db8d",
    "0526f4bf-ee07-4e77-816a-19c1d61f2340"
]
type_of_query_ids = [
    "f4f36898-a7da-4326-8799-02ac457cf413",
    "819b7cab-6395-4079-b77e-153b4c7ab097",
    "d219d60e-af2a-400e-8399-5d4cf696db04",
    "d159d0d1-7f39-45e1-82c4-9a471b1f4eef",
    "1c783f39-6044-49c4-820b-cba5e9b3dcf3",
    "cb7b659b-68f3-4be0-a549-fb143edb030d",
    "5516d2b0-0635-46ab-aa7e-9f7d76fd4bd6"
]
method_of_reply_ids = [
    "8d1330c2-3b3f-4993-afec-1f14ea419df9",
    "dfac9fdc-f6bb-42b5-8434-5e55fdd61cc8",
    "1e86145b-8b23-4dd6-b2da-433726ce569c",
    "a19940c6-2c81-4936-b7e3-9c91ffefc05f"
]
response_status_ids = [
    "edc2992a-417a-42d6-9fad-306f42c17e08",
    "e9699cf3-d76c-4637-8288-001e8bd39f92",
    "7779e0a6-94ca-4b15-a041-7a6a7a72132a",
    "044c9568-9d10-4ee5-a741-bf59de4fa0c9"
]

client_names = [
    "Ahmed Choukri", "Fatima Zahra", "Jean Dupont", "Rania Ben El", "Ali Cissé",
    "Sophia Khalid", "David Cohen", "Samira Makhfi", "Thomas Müller", "Nadine Nassar",
    "Karim Mezni", "Sarah El Haddad", "Lina Tavares", "Elias Berger", "Lydia Chevalier",
    "Samir Gharbi", "Ibrahim Diouf", "Julie Rochat", "Romain Lucas", "Hassan Abbassi",
    "Wassim Outmani", "Amina Benamar", "Omar El Fassi", "Elodie Brun", "Hicham Maati",
    "Nada Amrani", "Adil Ait Ali", "Sophie Marechal", "Zineb Taleb", "Karima Othmani"
]

def seed_calls(db: Session):
    base_date = date(2025, 9, 12)
    base_time = time(8, 0, 0)
    for i in range(30):
        call = Call(
            id=uuid.uuid4(),
            date=base_date,
            time=time((8 + (i % 8)), (i*7)%60, 0),  # Des heures variées
            recieved_from="Ringover" if i % 2 == 0 else "Whatsapp",
            client_name=client_names[i % len(client_names)],
            contact_number="+33 6 {:02d} {:02d} {:02d} {:02d}".format(
                (i+10)%90, (i+20)%90, (i+30)%90, (i+40)%90
            ),
            type_of_query_id=uuid.UUID(type_of_query_ids[i % len(type_of_query_ids)]),
            reason_of_call=["Demande info", "Réservation", "Modification", "Annulation"][i % 4],
            answered_by=["Mohamed", "Omar", "Ferdaousse", "Rosi", "Youssef", "test2"][i % 6],
            replied_to_id=uuid.UUID(response_status_ids[i % len(response_status_ids)]),
            replied_method_id=uuid.UUID(method_of_reply_ids[i % len(method_of_reply_ids)]),
            replied_by=["Mohamed", "Omar", "Ferdaousse", "Rosi", "Youssef", "test2"][i % 6],
            assigned_to_id=uuid.UUID(user_ids[i % len(user_ids)]),
            action_to_be_taken_by=["agent", "admin", "service client"][i % 3],
            actions_to_be_taken=["Rappeler", "Envoyer devis", "Annuler billet", "Traiter remboursement"][i % 4],
            action_taken=["Par email", "Appel ok", "Traitement en attente", "Action faite"][i % 4],
            other_comments=["RAS", "À suivre", "Client mécontent", "Client satisfait"][i % 4],
            status=[CallStatus.pending, CallStatus.closed, CallStatus.open][i % 3]
        )
        db.add(call)
    db.commit()
    print("30 appels insérés avec succès.")

def main():
    db = SessionLocal()
    try:
        seed_calls(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()
