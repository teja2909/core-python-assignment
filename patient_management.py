class PatientManagement:
    def __init__(self, patients):
        self.patients=patients
    def patient_disease(self,search_disease):
        return list(map(lambda x:x["Name"],filter(lambda x:x["Disease"]==search_disease,self.patients)))
patients = [{"Name": "Alice", "Age": 30, "Disease": "Flu"},
            {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
            {"Name": "Charlie", "Age": 35, "Disease": "Flu"}]
search_disease = input("Enter disease name: ")
obj=PatientManagement(patients)
print(obj.patient_disease(search_disease))