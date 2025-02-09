import pandas as pd
import datetime

def collect_dummy_data():
    # Simula datos de tweets y otras redes sociales
    data = [
        {
            "usuario": "usuario1",
            "texto": "Me encantan los cinnamon rolls y los donuts!",
            "fecha": datetime.datetime.now()
        },
        {
            "usuario": "usuario2",
            "texto": "Rollos de canela, dulces y más... ¡delicioso!",
            "fecha": datetime.datetime.now()
        }
    ]
    df = pd.DataFrame(data)
    df.to_csv("tweets_cinnamon.csv", index=False)
    print("Datos simulados guardados en tweets_cinnamon.csv")

if __name__ == '__main__':
    collect_dummy_data()
