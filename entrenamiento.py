import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Data
X = pd.read_csv('autos_unificados.csv')
y = pd.read_csv('Etiquetas_perfil.csv')

X = X.drop(columns=['Make', 'Model'])

# Para evitar problemas con datos de texto
encoder = LabelEncoder()
columnas_texto = ['Fuel_Type', 'Transmission' ,'Driven_Wheels', 'Vehicle_Size', 'Vehicle_Style']
for col in columnas_texto:
    X[col] = encoder.fit_transform(X[col])

# para comprobar que se hayan cambiando correctamente
# print("--- Primeras 5 filas de X ---")
# print(X.head())

df = pd.concat([X, y], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # Mantener proporciones
)
print(f'Entrenamiento: {X_train.shape[0]} muestras')
print(f'Prueba:        {X_test.shape[0]} muestras')

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

modelo_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced',
    max_depth=10,
    min_samples_leaf=5,
    min_samples_split=10,
    max_features='sqrt'
)
modelo_rf.fit(X_train_scaled, y_train.values.ravel())

importancias = modelo_rf.feature_importances_
nombres_columnas = X.columns

feature_df = pd.DataFrame({'Característica': nombres_columnas, 'Importancia': importancias})
feature_df = feature_df.sort_values(by='Importancia', ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(feature_df['Característica'], feature_df['Importancia'], color='#8da0cb')
plt.xlabel('Importancia')
plt.title('Importancia de las Características', fontsize=13, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
#plt.show()

y_pred = modelo_rf.predict(X_test_scaled)

acc_train = accuracy_score(y_train, modelo_rf.predict(X_train_scaled))
acc_test  = accuracy_score(y_test, y_pred)

print(f'  Precision - Entrenamiento: {acc_train:.4f} ({acc_train*100:.1f}%)')
print(f'  Precision - Prueba:        {acc_test:.4f} ({acc_test*100:.1f}%)')


# --- BLOQUE PARA SCORE ---
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    modelo_rf, X, y.values.ravel(),
    cv=5,              # divide el dataset en 5 partes
    scoring='accuracy'
)

print(f"Scores por fold: {scores.round(4)}")
print(f"Promedio:        {scores.mean():.4f} ({scores.mean()*100:.1f}%)")
print(f"Desviación:      {scores.std():.4f}")



# Guardar modelo
joblib.dump(modelo_rf, 'modelos/modelo_recomendador.pkl')
# Guardar scaler 
joblib.dump(scaler, 'scaler/scaler.pkl')

print("Modelo y scaler exportados")