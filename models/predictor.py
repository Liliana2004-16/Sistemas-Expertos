import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

class TiempoViajePredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.encoders = {}

    def entrenar(self, dataset_path):
        df = pd.read_csv(dataset_path)
        df = self._preprocesar(df)
        
        X = df[['Origen', 'Destino', 'Distancia', 'Hora', 'Dia', 'Clima', 'Evento']]
        y = df['Tiempo']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        print("MAE:", mean_absolute_error(y_test, y_pred))
        print("R² Score:", r2_score(y_test, y_pred))

    def predecir(self, muestra_dict):
        df = pd.DataFrame([muestra_dict])
        df = self._preprocesar(df, train=False)
        return self.model.predict(df)[0]

    def _preprocesar(self, df, train=True):
        rename_cols = {
            'Dia de la semana': 'Dia',
            'Clima': 'Clima',
            'Evento': 'Evento'
        }
        df.rename(columns=rename_cols, inplace=True)
        
        for col in ['Origen', 'Destino', 'Dia', 'Clima', 'Evento']:
            if train:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.encoders[col] = le
            else:
                le = self.encoders[col]
                df[col] = le.transform(df[col].astype(str))
        
        return df
