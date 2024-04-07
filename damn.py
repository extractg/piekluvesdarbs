import sys
sys.path.append("C:/Users/777/AppData/Local/Programs/Python/Python39/Lib/site-packages")
import speedtest

def run_speedtest():
    # Izveidojiet Speedtest objektu
    st = speedtest.Speedtest()
    
    # Veiciet testu, lai noteiktu pašreizējo interneta ātrumu
    print("Veic interneta ātruma testu...")
    download_speed_before = st.download() / 1024 / 1024  # pārvēršam baitos megabaitos
    upload_speed_before = st.upload() / 1024 / 1024
    
    # Izvada pašreizējo interneta ātrumu
    print(f"Pašreizējais lejupielādes ātrums: {download_speed_before:.2f} Mbps")
    print(f"Pašreizējais augšupielādes ātrums: {upload_speed_before:.2f} Mbps")
    
    # Šeit jūs varētu pievienot kodu, kas veic potenciālos uzlabojumus interneta ātrumam
    
    # Atkārtoti veiciet testu, lai pārbaudītu izmaiņas
    print("\nPēc potenciālā uzlabojuma testēšanas...")
    download_speed_after = st.download() / 1024 / 1024
    upload_speed_after = st.upload() / 1024 / 1024
    
    # Izvada jauno interneta ātrumu
    print(f"Jaunais lejupielādes ātrums: {download_speed_after:.2f} Mbps")
    print(f"Jaunais augšupielādes ātrums: {upload_speed_after:.2f} Mbps")

if __name__ == "__main__":
    run_speedtest()