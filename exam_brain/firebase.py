from firebase_admin import db

def insert_data_to_firebase():
    ref = db.reference('email')  
    data = {
        encode_key("janesmitssh@example.com"): {
            "age": 30,
            "exam_1": 92,
            "exam_2": 88,
            "exam_3": 79,
            "exam_4": 85
        }
    }
    for key, value in data.items():
        ref.child(key).set(value)
    print("Data inserted successfully.")

def encode_key(key):
    return key.replace('.', ',').replace('$', '_').replace('#', '_').replace('[', '_').replace(']', '_').replace('/', '_')