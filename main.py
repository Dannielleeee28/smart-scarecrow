# main.py
from detect_rice import load_model, detect_rice_stage
from sms_sender import send_sms
from sound_loop import play_sound
import threading
import time

def main():
    threading.Thread(target=play_sound, daemon=True).start()
    model = load_model()

    while True:
        stage, maturity = detect_rice_stage(model)
        print(f"Detected: {stage} ({maturity}%)")
        if stage == "Ripe":
            send_sms(f"Ready for harvest! Maturity %: {maturity}")
            time.sleep(3600)  # Wait an hour before next alert
        time.sleep(10)

if __name__ == "__main__":
    main()
