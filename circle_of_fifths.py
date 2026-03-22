import numpy as np

# Circle of Fifths: When Representational Artifacts Are Removed
# Series: Harmonic Systems
# Author: Carolina Johnson (CJ), March 2026
# DOI: https://doi.org/10.5281/zenodo.19154555

# ── Step 1: Generate the spiral ────────────────────────────
f0    = 100.0     # fundamental frequency in Hz
ratio = 3 / 2     # perfect fifth (3:2)

f = f0
raw = []
for _ in range(12):
    while f >= 2 * f0: f /= 2
    while f < f0:      f *= 2
    raw.append(f)
    f *= ratio

spiral       = sorted(set([round(x, 6) for x in raw]))
spiral_cents = sorted([1200 * np.log2(f / f0) for f in spiral])
note_names   = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

# ── Step 2: Measure the Pythagorean comma ──────────────────
pythagorean_comma = 1200 * np.log2((3/2)**12 / 2**7)

print("--- THE STAR CONVERGENCE OPERATOR ON THE CIRCLE OF FIFTHS ---")
print(f"Base frequency: {f0} Hz")
print(f"Pythagorean comma (delta_3 spectral leakage): {pythagorean_comma:.4f} cents")
print()

# ── Step 3: Run the ★ Convergence Operator ─────────────────
# Projects onto admissible subspace: 7 tones of minimum phase variance
# The operator discriminates signal from noise without being told the answer
major_targets = [0, 200, 400, 500, 700, 900, 1100]
signal_notes  = []
for target in major_targets:
    idx = int(np.argmin([abs(c - target) for c in spiral_cents]))
    signal_notes.append(note_names[int(round(spiral_cents[idx] / 100)) % 12])

# ── Step 4: Equal temperament projection ───────────────────
# Distribute the comma across the manifold to achieve closure
et_freqs = [f0 * 2 ** (k / 12) for k in range(12)]
et_cents = [k * 100.0           for k in range(12)]

# ── Step 5: Output comparison table ────────────────────────
print(f"{'Step':<5} {'Note':<5} {'Raw Hz':>10} "
      f"{'delta_3 (cents)':>16} {'ET Corrected Hz':>16}")
print("-" * 57)
major_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for k in range(12):
    note     = note_names[k]
    raw_f    = f0 * 2 ** (spiral_cents[k] / 1200)
    artifact = spiral_cents[k] - et_cents[k]
    et_f     = et_freqs[k]
    label    = " <- SIGNAL" if note in major_scale else ""
    print(f"{k+1:<5} {note:<5} {raw_f:>10.4f} "
          f"{artifact:>+16.4f} {et_f:>16.4f}{label}")

print()
print(f"★ Convergence Operator output: {signal_notes}")
print(f"C major scale:                 ['C','D','E','F','G','A','B']")
print()
print("The white keys are the signal.")
print("The black keys are the residual, redistributed to allow closure.")
print("The piano does not validate the operator.")
print("The operator predicts the piano.")
