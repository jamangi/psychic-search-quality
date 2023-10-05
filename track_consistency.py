from shauntal_tracker.consistency_tracker import calculate_consistency, save_plot
from consistency_data import GARDEVOIR_CONSISTENCY_TUPLES

gardevoir_consistency = calculate_consistency(GARDEVOIR_CONSISTENCY_TUPLES)
save_plot("Gardevoir Consistency Score", gardevoir_consistency, "gardevoir_score_plot.png")
