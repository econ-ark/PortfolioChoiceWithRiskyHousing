library(srvyr)


# Summary statistics ----

# Create survey object, and group it.
scf_srvy <- as_survey_design(SCF, weights = "wgt")

# Define groupings
groupings <- list(
  c("Educ", "YEAR", "Age_grp", "hmort"),
  c("YEAR", "Age_grp", "hmort"),
  c("Educ", "Age_grp", "hmort"),
  c("Educ", "YEAR", "hmort"),
  c("Educ", "hmort"),
  c("YEAR", "hmort"),
  c("Age_grp", "hmort"),
  c("hmort"),
  c()
)

# An auxiliary function that finds the quantities of
# interest at any grouping
calcSumStats <- function(survey, grouping) {
  # Find number of observations used for stats
  sumstats <- survey %>%
    group_by_at(grouping) %>%
    srvyr::summarise(
      # Weighted and unweighted number of observations.
      w.obs = survey_total(),
      obs = unweighted(n()),

      # Mean and sd of log(Wealth)
      lnWealth.mean = survey_mean(lnWealth),
      lnWealth.sd = survey_sd(lnWealth),

      # Mean and sd of log(Wealth/Permanent income)
      lnNrmWealth.mean = survey_mean(lnNrmWealth),
      lnNrmWealth.sd = survey_sd(lnNrmWealth),

      # Mean and sd of log(Permanent income)
      lnPermIncome.mean = survey_mean(lnPermIncome),
      lnPermIncome.sd = survey_sd(lnPermIncome),

      # Mean and sd of log(Mortgage)
      lnMortgage.mean = survey_mean(lnMortgage),
      lnMortgage.sd = survey_sd(lnMortgage),

      # Mean and sd of log(NrmMortgage)
      lnNrmMortgage.mean = survey_mean(lnNrmMortgage),
      lnNrmMortgage.sd = survey_sd(lnNrmMortgage)
    ) %>%
    select(-contains("_se"))

  # Find all combinations of factors to construct explicit NAs
  if (length(grouping) > 0) {
    combs <- sumstats %>%
      ungroup() %>%
      select(all_of(grouping)) %>%
      expand(!!!rlang::syms(grouping))

    stats <- combs %>% left_join(sumstats)
  } else {
    stats <- sumstats
  }

  return(stats)
}

# Apply to all groupings and combine into single table.
table <-
  lapply(groupings, function(grp) {
    calcSumStats(scf_srvy, grp)
  }) %>%
  bind_rows()

# Change type of grouping columns before exporting
table <- table %>%
  ungroup() %>%
  mutate(across(all_of(c(
    "Educ", "YEAR", "Age_grp", "hmort"
  )), as.character))

# Change NA's in grouping variables to 'All'
table <- table %>%
  replace_na(list(
    Educ = "All",
    YEAR = "All",
    Age_grp = "All",
    hmort = "All"
  ))

# Finally, add the base year for inflation adjustments
table <- table %>%
  mutate(BASE_YR = base_year) %>%
  drop_na()

# Export result
write_csv(table, "./WealthIncomeStats.csv")
