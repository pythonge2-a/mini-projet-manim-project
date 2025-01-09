import subprocess
import os
import time

# Test des différents ensembles de paramètres, y compris des cas incorrects
test_cases = [
    {'v0': 25, 'theta': 15},  # Paramètres valides
    {'v0': 20, 'theta': 30},  # Paramètres valides
    {'v0': 10, 'theta': 45},  # Paramètres valides
    {'v0': 18, 'theta': 60},  # Paramètres valides
    {'v0': 22, 'theta': 75},  # Paramètres valides
    {'v0': 5, 'theta': 10},   # theta trop faible
    {'v0': 20, 'theta': 100}, # theta trop élevé
    {'v0': 30, 'theta': 15},  # v0 trop élevé
    {'v0': 0, 'theta': 45},   # v0 trop faible
    {'v0': -5, 'theta': 45}   # v0 négatif
]

# Fichiers de référence et de résultats
reference_file = './test_results/test_ref.txt'
results_file = './test_results/test_results.txt'

# Lire les données de référence
def load_reference_data(file_path):
    reference_data = {}
    with open(file_path, 'r') as file:
        current_test = None
        for line in file:
            if line.startswith("Test pour"):
                parts = line.split(',')
                v0 = float(parts[0].split('=')[1].strip().replace('m/s', ''))
                theta = float(parts[1].split('=')[1].strip().replace('°', ''))
                current_test = (v0, theta)
                reference_data[current_test] = {}
            elif line.startswith("Hauteur maximale"):
                reference_data[current_test]['hauteur_max'] = float(line.split(':')[1].strip().replace('m', ''))
            elif line.startswith("Portée"):
                reference_data[current_test]['portee'] = float(line.split(':')[1].strip().replace('m', ''))
            elif line.startswith("Temps de vol total"):
                reference_data[current_test]['temps_vol'] = float(line.split(':')[1].strip().replace('s', ''))
    return reference_data

# Charger les résultats obtenus
def load_results(file_path):
    results_data = {}
    with open(file_path, 'r') as file:
        current_test = None
        for line in file:
            if line.startswith("Test pour"):
                parts = line.split(',')
                v0 = float(parts[0].split('=')[1].strip().replace('m/s', ''))
                theta = float(parts[1].split('=')[1].strip().replace('°', ''))
                current_test = (v0, theta)
                results_data[current_test] = {}
            elif line.startswith("Hauteur maximale"):
                results_data[current_test]['hauteur_max'] = float(line.split(':')[1].strip().replace('m', ''))
            elif line.startswith("Portée"):
                results_data[current_test]['portee'] = float(line.split(':')[1].strip().replace('m', ''))
            elif line.startswith("Temps de vol total"):
                results_data[current_test]['temps_vol'] = float(line.split(':')[1].strip().replace('s', ''))
    return results_data

# Comparer les résultats obtenus avec les références
def compare_results(reference, results):
    errors = []
    for test, values in results.items():
        if test not in reference:
            errors.append(f"Résultats inattendus pour le test {test}")
            continue
        ref_values = reference[test]
        for key in values:
            if abs(values[key] - ref_values[key]) > 1e-2:  # Tolérance de 0.01
                errors.append(f"Différence pour {key} (v0={test[0]}, θ={test[1]}°) : attendu {ref_values[key]}, obtenu {values[key]}")
    return errors

# Fonction pour exécuter un test
def test_trajectory_script(v0, theta):
    command = [
        'python3', 'trajectory.py',
        '--v0', str(v0),
        '--theta', str(theta),
        '--test'
    ]

    print(f"Test en cours pour v0 = {v0} m/s, θ = {theta}°...")
    try:
        subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        print(f"Test terminé pour v0 = {v0}, θ = {theta}.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du test (v0={v0}, θ={theta}) : {e.stderr}")

# Lancer les tests pour les cas valides uniquement
for test_case in test_cases:
    v0, theta = test_case['v0'], test_case['theta']
    if 5 <= v0 <= 25 and 15 <= theta <= 80:
        test_trajectory_script(v0, theta)
    time.sleep(1)

# Charger et comparer les résultats
if os.path.exists(reference_file) and os.path.exists(results_file):
    reference_data = load_reference_data(reference_file)
    results_data = load_results(results_file)
    errors = compare_results(reference_data, results_data)

    if errors:
        print("\nErreurs détectées :")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nTous les tests ont réussi.")
else:
    print("Erreur : Fichiers de référence ou de résultats manquants.")
