def test_patient_data_format():
    patients = [
        {"id": 1, "name": "John Doe", "age": 34, "condition": "Diabetes"},
        {"id": 2, "name": "Jane Smith", "age": 45, "condition": "Hypertension"},
    ]
    for patient in patients:
        assert isinstance(patient["id"], int)
        assert isinstance(patient["name"], str)
        assert isinstance(patient["age"], int)
        assert isinstance(patient["condition"], str)

if __name__ == "__main__":
    test_patient_data_format()
    print("All patient data tests passed!")