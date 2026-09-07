# Franka evaluation protocol

Status: outcomes and images pending. D1 and D2 name two disturbance TYPES
whose physical definitions remain to be supplied. Do not interpret them as
two displacement magnitudes without confirmation.

## Matrix and fairness

- Four tasks: pick-and-place, block pushing, drawer opening, whiteboard wiping.
- Three methods: pi0, pi0+DUET-Rel (fusion off), pi0+DUET (fusion on).
  The last two share a checkpoint.
- Three conditions: Clean, D1, D2.
- Twenty trials per task/method/condition: 4 x 3 x 3 x 20 = 720 formal trials.
  This replaces the old 480-trial, two-condition plan.
- Success rate is the sole evaluation metric. Keep trial counts as provenance.
- Match successful demonstrations, data splits, inputs, training budget,
  execution rate and time limit. Record checkpoint IDs and unavoidable differences.
- Use the same 20 predefined scenes per task across methods and conditions.
  Randomize order, reset completely, and do not allow human correction.

## Disturbance protocols and success

Finalize D1/D2 definitions, trigger stages, magnitudes and durations before formal
testing. Use separate pilots to verify feasibility and choose settings without
optimizing the DUET-versus-baseline gap. The former 2/4/6 cm displacement pilot
does not define the still-unspecified second disturbance type.

Inject one instance of the designated disturbance per disturbed trial.
Keep failures before injection in the success-rate denominator. Retain scene,
method, condition, injection status, actual intervention, video and final outcome;
these are audit records, not additional evaluation metrics. Do not silently
replace failed or uninjected trials.

Freeze task goals before testing. Success must persist for two seconds:
- Pick-and-place: the released object remains in the target region.
- Pushing: the object remains in the target region.
- Drawer: the calibrated target opening is reached.
- Wiping: the goal is achieved with the tool retained. Existing validated
  criteria take precedence; otherwise require at least 90% stain-area reduction
  in a fixed mask under fixed lighting and a frozen segmentation rule.

Task completion determines success; gate activity or waypoint proximity alone
does not establish recovery. Report task success percentages based on 20 trials,
and equal-weight means across the four tasks. Do not pre-claim equivalence,
statistical significance, or zero-shot transfer across separately trained models.

## Page 6 figures and table

Top, across both columns: exactly FOUR task setup images in one horizontal row,
one for each task. No additional retry-sequence rows.

Left column: one success-rate table. Columns are Method, Clean, D1, D2.
Each task group contains the three methods; the final group reports the
equal-weight task mean for each method and condition. Use percentages only.
Unmeasured values remain dashes.

Right column: exactly SIX images, TWO columns by THREE rows:
- Top row: disturbance-type schematics, D1 left and D2 right.
- Middle row: successful responses, D1 left and D2 right.
- Bottom row: failed responses, D1 left and D2 right.

Keep each disturbance in its own column. Label actual methods and trial IDs in
the photographs. Do not assume all successes belong to DUET or all failures to
the baseline. Use actual outcomes, consistent crops/views, and distinguish
schematic arrows from measured annotations. These examples illustrate the
success-rate results. No mechanism curves are required for this version.

## Acceptance

Keep all ten image placeholders and the success table on page 6, with the
six-image grid in the right column. The table and grid share a wide float
containing two column-width minipages. Total length, including references,
must not exceed eight pages. Preserve Table I/II near Q1 and Table IV near Q3.
Keep real-robot claims pending until measurements are available.
Recompile and visually inspect changed pages for overlap, clipping and legibility.
