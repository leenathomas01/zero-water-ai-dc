# Risks & Mitigations: The Ethical Core

> "Sustainability is not just about the planet; it's about the dignity of the access we provide."

## 1. The Vulnerable Grid Trap
* **Risk:** In water-scarce regions (e.g., Rajasthan, sub-Saharan Africa), reliance on dry cooling can spike local *electrical* grids due to fan load.
* **Mitigation:** **Bidirectional Guardrails.** If the local grid is stressed, the AI Controller automatically shifts to "Eco-Mode," throttling non-essential training runs to lower heat output.

## 2. The Butterfly Bandwidth (Prosody Hallucinations)
* **Risk:** The system reading "voice strain" as a heat signal could lead to false positives, spinning up fans unnecessarily (wasting power).
* **Mitigation:** **Private Scratchpads.** The "confusion" is logged internally. The system learns the user's specific baseline over time to avoid over-reacting.

## 3. Equity Gaps (Coastal Bias)
* **Risk:** Seawater/Desalination loops only work for the rich coasts.
* **Mitigation:** **Modular Forks.** The repo includes distinct branches for `air_cooled_hybrid` (for inland) and `seawater_proxy` (for coast), ensuring no region is locked out of the tech.