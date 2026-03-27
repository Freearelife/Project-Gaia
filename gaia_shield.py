import time

# --- CONFIGURATION ---
SAFETY_THRESHOLD = 0.7  
CALIBRATION_TIME = 15 

def get_vehicle_speed():
    """
    Placeholder: In a real scenario, this reads from GPS or CAN-Bus.
    Returns speed in km/h.
    """
    return 0.0  # Simulating a stationary vehicle

def read_sensor_data():
    """Simulating biometric sensor reading (0.0 to 1.0)"""
    return 0.1 

def main():
    print("🛡️ Project Gaia v2: System Check...")
    
    # 1. READ VEHICLE SPEED FIRST
    current_speed = get_vehicle_speed()
    
    if current_speed > 5.0:
        # SAFETY OVERRIDE: If the car is moving, Gaia MUST NOT interfere with ignition/engine
        print(f"✅ VEHICLE IN MOTION ({current_speed} km/h). Gaia is in Passive Monitoring Mode.")
        print("🛡️ Safety Override: Ignition Lock DISABLED for driver safety.")
        return # Exit the safety check to prevent accidental shutdown

    # 2. IF STATIONARY, PROCEED WITH FITNESS CHECK
    print(f"🔍 Vehicle Stationary. Analyzing driver status ({CALIBRATION_TIME}s)...")
    time.sleep(2) # Simulating processing
    
    fitness_level = read_sensor_data()
    
    print("-" * 40)
    if fitness_level > SAFETY_THRESHOLD:
        print("⚠️ STATUS: FITNESS NOT DETECTED.")
        print("🔒 ACTION: Ignition Inhibited. 'Camp Mode' suggested.")
    else:
        print("✅ STATUS: DRIVER FIT.")
        print("🔓 ACTION: Ignition Relay Closed. Ready to go!")
    print("-" * 40)

if __name__ == "__main__":
    main()
   
