# Recommender Output Comparison

## High-Energy Pop vs Chill Lofi
High-Energy Pop favored bright pop tracks like "Sunrise City" and "Gym Hero" because the profile asked for pop genre and high energy. Chill Lofi shifted the top results to lofi songs such as "Library Rain" and "Midnight Coding," showing that genre and low energy are strong signals in this system.

## Deep Intense Rock vs Chill Lofi
Deep Intense Rock picked hard rock and intense tracks like "Storm Runner," while Chill Lofi stayed with laid-back lofi songs. This makes sense because rock and intense mood both add strong matching points, whereas chill preferences reward low energy and relaxed mood.

## High-Energy Pop vs Conflict Case
The conflict profile requested pop sad with high energy. The top songs still included pop favorites like "Gym Hero" and "Sunrise City," which means the system is treating energy and genre as stronger than mood in this case. That explains why "Gym Hero" can keep appearing for people who want happy or intense pop.

## Weight Shift Experiment
After changing genre to 1.0 and energy to 2.0, the recommender became more sensitive to energy closeness. The top songs did not change dramatically for clear profiles, but the scores showed higher reward for energy similarity. This confirms that the model is most sensitive to the energy gap when the weight is larger.
