import pandas as pd
import random

def generate_balanced_dataset():
    records = []
    data_types = ["image", "video", "audio", "text"]
    total_records = 300000

    for _ in range(total_records):
        type_data = random.choice(data_types)
        sensitivity = random.randint(1, 5)

        if type_data == "text":
            if sensitivity >= 3:
                data_size = round(random.uniform(0.01, 0.05 if random.random() < 0.5 else 50), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.45, 0.45, 0.1])[0] if data_size > 0.05 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.4, 0.4, 0.2])[0]
            else:
                data_size = round(random.uniform(0.01, 50 if random.random() < 0.5 else 200), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.4, 0.4, 0.2])[0] if data_size > 50 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.3, 0.3, 0.4])[0]

        elif type_data == "image":
            if sensitivity >= 3:
                data_size = round(random.uniform(1, 512 if random.random() < 0.5 else 1024), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.6, 0.3, 0.1])[0] if data_size > 512 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.5, 0.3, 0.2])[0]
            else:
                data_size = round(random.uniform(1, 512 if random.random() < 0.5 else 1024), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.4, 0.4, 0.2])[0] if data_size > 512 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.3, 0.3, 0.4])[0]

        elif type_data == "video":
            if sensitivity >= 3:
                data_size = round(random.uniform(15, 1024 if random.random() < 0.5 else 10240), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.7, 0.3, 0.0])[0] if data_size > 1024 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.5, 0.4, 0.1])[0]
            else:
                data_size = round(random.uniform(15, 1024 if random.random() < 0.5 else 10240), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.5, 0.4, 0.1])[0] if data_size > 1024 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.4, 0.3, 0.3])[0]

        else:  # audio
            if sensitivity >= 3:
                data_size = round(random.uniform(0.1, 512 if random.random() < 0.5 else 1024), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.6, 0.3, 0.1])[0] if data_size > 512 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.5, 0.3, 0.2])[0]
            else:
                data_size = round(random.uniform(0.1, 512 if random.random() < 0.5 else 1024), 2)
                algorithm = random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.4, 0.4, 0.2])[0] if data_size > 512 else random.choices(['AES', 'ChaCha20', 'Blowfish'], weights=[0.3, 0.3, 0.4])[0]

        records.append({
            "Data_Size": data_size,
            "Sensitivity": sensitivity,
            "Data_Type": type_data,
            "Algorithm": algorithm
        })

    random.shuffle(records)
    new_dataset = pd.DataFrame(records)
    new_dataset.to_csv('encrypted_data.csv', index=False)
    return new_dataset

# Generate the dataset and show the first few records
generated_dataset = generate_balanced_dataset()
print(generated_dataset.head())
