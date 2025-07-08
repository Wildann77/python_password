def generate_strong_password_with_model(model, length=12, max_attempts=100):
    import random
    import string
    from utils.features import extract_features

    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(max_attempts):
        password = ''.join(random.choice(characters) for _ in range(length))
        features = extract_features(password)
        prediction = model.predict(features)[0]

        print(f"[CHECK] {password} => {prediction}")


        if prediction == 'strong':  # Ganti '2' kalau strong-nya beda
            return password

    return None
