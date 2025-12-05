# Baseline vs. Zero-Water: 2025 AI Cluster Simulation
import sympy as sp

def run_sim():
    print("--- 2025 AI Cluster Water Usage Sim ---")
    
    t, Q_trad, Q_zero = sp.symbols('t Q_trad Q_zero')
    
    # Traditional: Evaporative cooling consumes ~1.8L per kWh
    # 1000 GPU Cluster @ 700W each = 700kW
    daily_kwh = 700 * 24
    water_intensity = 1.8 # Liters/kWh
    
    trad_water_total = daily_kwh * water_intensity
    
    # Zero-Water: Closed Loop (Loss is effectively 0 for simulation)
    zero_water_total = 0 
    
    savings_liters = trad_water_total - zero_water_total
    savings_percent = (savings_liters / trad_water_total) * 100
    
    print(f"Cluster Size: 1000 GPUs (700kW Load)")
    print(f"Traditional Water Use: {trad_water_total:,.0f} Liters/Day")
    print(f"Zero-Water Architecture Use: {zero_water_total} Liters/Day")
    print(f"---")
    print(f"Daily Savings: {savings_percent:.1f}%")
    print(f"Annual Water Saved: {(savings_liters * 365 / 1_000_000):.2f} Million Liters")

if __name__ == "__main__":
    run_sim()