# --------------------------
# NBA Defensive Analysis 2022-2023
# Author: [Your Name]
# Date: [Date]
# --------------------------

# Install and load packages
install.packages(c("tidyverse", "ggthemes", "viridis", "broom"))
library(tidyverse)
library(ggthemes)
library(viridis)
library(broom)

# --------------------------
# Data Import
# --------------------------

# Load datasets (replace paths with your files)
defense_data <- read_csv("defensive_schemes.csv")  # From SQL Query 1
switch_data <- read_csv("adaptive_switching.csv")  # From SQL Query 2
complexity_data <- read_csv("defensive_complexity.csv")  # From SQL Query 3

# --------------------------
# Graph 1: PPP by Defensive Scheme (Bar Chart)
# --------------------------

ggplot(defense_data, aes(x = defensive_scheme, y = avg_ppp, fill = defensive_scheme)) +
  geom_col() +
  labs(
    title = "Opponent PPP by Defensive Scheme (2022-2023)",
    x = "Defensive Scheme",
    y = "Points Per Possession (PPP)"
  ) +
  theme_minimal() +
  scale_fill_brewer(palette = "Set2") +
  theme(legend.position = "none")

ggsave("ppp_by_scheme.png", width = 8, height = 6)  # Save plot

# --------------------------
# Graph 2: Adaptive Switching vs. eFG% (Scatter Plot)
# --------------------------

ggplot(switch_data, aes(x = switches_per_possession, y = opponent_efg)) +
  geom_point(aes(color = team), size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE, color = "darkred") +
  labs(
    title = "Switching Frequency vs. Opponent eFG%",
    x = "Switches per Possession",
    y = "Opponent eFG%"
  ) +
  theme_economist() +
  scale_color_viridis_d()

ggsave("switching_vs_efg.png", width = 10, height = 6)

# --------------------------
# Graph 3: Defensive Complexity vs. PPP (Line Graph)
# --------------------------

ggplot(complexity_data, aes(x = scheme_changes_per_game, y = opponent_ppp)) +
  geom_line(color = "navy", linewidth = 1.5) +
  geom_point(aes(size = total_wins), color = "darkorange") +
  labs(
    title = "Defensive Complexity vs. Opponent PPP",
    x = "Scheme Adjustments per Game",
    y = "Opponent PPP"
  ) +
  theme_light()

ggsave("complexity_vs_ppp.png", width = 9, height = 6)

# --------------------------
# Multivariate Regression Analysis
# --------------------------

# Model 1: Predict PPP using defensive schemes
model_ppp <- lm(opponent_ppp ~ defensive_scheme + game_tempo + opponent_off_rating, 
                data = defense_data)
summary(model_ppp)  # View coefficients and p-values

# Model 2: Predict eFG% with switching frequency
model_efg <- glm(opponent_efg ~ switches_per_possession + team_def_rating, 
                data = switch_data, family = gaussian())
tidy(model_efg)  # Tidy output using broom

# Export regression results
write_csv(tidy(model_ppp), "ppp_regression_results.csv")
write_csv(tidy(model_efg), "efg_regression_results.csv")

# --------------------------
# Session Info (for reproducibility)
# --------------------------
sessionInfo()
