import speedtest
import sqlite3
import time

class SpeedTestManager:
    def __init__(self, db_file='speedtest_results.db'):
        self.db_file = db_file
        self.conn = None

    def connect_to_database(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            return True
        except sqlite3.Error as e:
            print("Neizdevās izveidot savienojumu ar datubāzi:", e)
            return False

    def create_table_if_not_exists(self):
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS speed_results 
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                              download_speed REAL, 
                              upload_speed REAL, 
                              test_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
                self.conn.commit()
            except sqlite3.Error as e:
                print("Neizdevās izveidot tabulu:", e)

    def run_speedtest_and_save_results(self):
        if self.conn is not None:
            try:
                st = speedtest.Speedtest()
                download_speed = st.download() / 1024 / 1024
                upload_speed = st.upload() / 1024 / 1024
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO speed_results (download_speed, upload_speed) VALUES (?, ?)", (download_speed, upload_speed))
                self.conn.commit()
                print("SpeedTest izpildīts un rezultāti saglabāti datubāzē.")
            except sqlite3.Error as e:
                print("Neizdevās saglabāt rezultātus datubāzē:", e)

    def run_speedtest_every_10_minutes(self):
        if self.connect_to_database():
            self.create_table_if_not_exists()
            while True:
                self.run_speedtest_and_save_results()
                time.sleep(600)

if __name__ == "__main__":
    manager = SpeedTestManager()
    manager.run_speedtest_every_10_minutes()
