# Survey Scoring Template
# This R script provides functions for scoring all survey measures in the study
# Author: Research Team
# Last Updated: 2023-12-20

# Load required packages
library(tidyverse)
library(psych)
library(car)
library(lavaan)

# Helper Functions ----

#' Reverse score items
#' @param x Numeric vector of scores
#' @param max_score Maximum possible score (default = 7)
#' @return Reversed scores
reverse_score <- function(x, max_score = 7) {
  (max_score + 1) - x
}

#' Check for missing data
#' @param data Dataframe of responses
#' @param threshold Maximum acceptable percentage of missing data
#' @return Logical vector indicating rows to keep
check_missing <- function(data, threshold = 0.1) {
  row_missing <- rowMeans(is.na(data))
  row_missing <= threshold
}

#' Calculate reliability
#' @param data Dataframe of items
#' @param items Vector of item names
#' @return List of reliability statistics
calculate_reliability <- function(data, items) {
  subset_data <- data[, items]
  alpha <- psych::alpha(subset_data)
  omega <- psych::omega(subset_data)
  
  list(
    alpha = alpha$total$raw_alpha,
    omega = omega$omega_h,
    item_total = alpha$item.stats
  )
}

# Scoring Functions ----

#' Score FAD-Plus
#' @param data Dataframe containing FAD-Plus responses
#' @return Dataframe with subscale and total scores
score_fad <- function(data) {
  # Define item groups
  free_will <- c("fad1", "fad2", "fad3", "fad4", "fad5", "fad6", "fad7")
  scientific_det <- c("fad8", "fad9", "fad10", "fad11", "fad12", "fad13", "fad14")
  fatalistic_det <- c("fad15", "fad16", "fad17", "fad18", "fad19", "fad20", "fad21")
  unpredictability <- c("fad22", "fad23", "fad24", "fad25", "fad26", "fad27")
  
  # Calculate subscale scores
  results <- data %>%
    mutate(
      free_will_score = rowMeans(select(., all_of(free_will))),
      scientific_det_score = rowMeans(select(., all_of(scientific_det))),
      fatalistic_det_score = rowMeans(select(., all_of(fatalistic_det))),
      unpredictability_score = rowMeans(select(., all_of(unpredictability))),
      total_score = rowMeans(select(., all_of(c(free_will, scientific_det, 
                                               fatalistic_det, unpredictability))))
    )
  
  # Calculate reliability
  reliability <- list(
    free_will = calculate_reliability(data, free_will),
    scientific_det = calculate_reliability(data, scientific_det),
    fatalistic_det = calculate_reliability(data, fatalistic_det),
    unpredictability = calculate_reliability(data, unpredictability)
  )
  
  attr(results, "reliability") <- reliability
  results
}

#' Score CRT
#' @param data Dataframe containing CRT responses
#' @return Dataframe with scores and metrics
score_crt <- function(data) {
  # Define correct answers
  correct_answers <- c(
    crt1 = 5,  # Ball costs 5 cents
    crt2 = 5,  # 5 minutes for widgets
    crt3 = 47, # 47 days for lily pads
    crt4 = 4,  # 4 days for water
    crt5 = 29, # 29 students
    crt6 = 20, # $20 profit
    crt7 = 7000 # $7000 final value
  )
  
  # Score responses
  results <- data %>%
    mutate(
      across(starts_with("crt"), 
             ~ifelse(. == correct_answers[cur_column()], 1, 0),
             .names = "correct_{.col}"),
      total_correct = rowSums(across(starts_with("correct_"))),
      intuitive_answers = rowSums(across(starts_with("crt_intuitive"))),
      reflection_score = total_correct * 2 - intuitive_answers
    )
  
  # Calculate reliability
  reliability <- calculate_reliability(data, names(correct_answers))
  attr(results, "reliability") <- reliability
  
  results
}

#' Score Need for Cognition Scale
#' @param data Dataframe containing NCS responses
#' @return Dataframe with scores and factors
score_ncs <- function(data) {
  # Define reverse scored items
  reverse_items <- c("ncs3", "ncs4", "ncs5", "ncs7", "ncs8", "ncs9", 
                    "ncs12", "ncs16", "ncs17")
  
  # Reverse score items
  results <- data %>%
    mutate(across(all_of(reverse_items), ~reverse_score(., 5))) %>%
    mutate(
      total_score = rowMeans(select(., starts_with("ncs"))),
      complexity_score = rowMeans(select(., c("ncs1", "ncs2", "ncs6", "ncs10", 
                                            "ncs11", "ncs13", "ncs14", "ncs15"))),
      persistence_score = rowMeans(select(., c("ncs3", "ncs4", "ncs5", "ncs7", 
                                             "ncs8", "ncs9"))),
      abstract_score = rowMeans(select(., c("ncs12", "ncs16", "ncs17", "ncs18")))
    )
  
  # Calculate reliability
  reliability <- calculate_reliability(data, names(select(data, starts_with("ncs"))))
  attr(results, "reliability") <- reliability
  
  results
}

#' Score Actively Open-minded Thinking Scale
#' @param data Dataframe containing AOT responses
#' @return Dataframe with scores and subscales
score_aot <- function(data) {
  # Define reverse scored items
  reverse_items <- c("aot3", "aot4", "aot5", "aot6", "aot7", "aot11", "aot12",
                    "aot15", "aot16", "aot17", "aot19", "aot20", "aot21",
                    "aot24", "aot25", "aot26", "aot27")
  
  # Define subscales
  flexible <- paste0("aot", 1:7)
  openness <- paste0("aot", 8:14)
  dogmatism <- paste0("aot", 15:21)
  truth_seeking <- paste0("aot", 22:28)
  
  # Score the scale
  results <- data %>%
    mutate(across(all_of(reverse_items), ~reverse_score(., 7))) %>%
    mutate(
      flexible_thinking = rowMeans(select(., all_of(flexible))),
      openness_values = rowMeans(select(., all_of(openness))),
      dogmatism_score = rowMeans(select(., all_of(dogmatism))),
      truth_seeking_score = rowMeans(select(., all_of(truth_seeking))),
      total_score = rowMeans(select(., starts_with("aot")))
    )
  
  # Calculate reliability
  reliability <- list(
    flexible = calculate_reliability(data, flexible),
    openness = calculate_reliability(data, openness),
    dogmatism = calculate_reliability(data, dogmatism),
    truth_seeking = calculate_reliability(data, truth_seeking),
    total = calculate_reliability(data, names(select(data, starts_with("aot"))))
  )
  
  attr(results, "reliability") <- reliability
  results
}

# Quality Control Functions ----

#' Check for attention check failures
#' @param data Dataframe containing responses
#' @return Logical vector indicating valid responses
check_attention <- function(data) {
  # Implement attention check logic
  attention_checks <- data %>%
    mutate(
      check1 = attention1 == expected_value1,
      check2 = attention2 == expected_value2,
      check3 = attention3 == expected_value3
    )
  
  rowSums(attention_checks) >= 2  # Pass if at least 2 checks are correct
}

#' Check for suspicious response patterns
#' @param data Dataframe containing responses
#' @return Logical vector indicating valid responses
check_patterns <- function(data) {
  # Calculate standard deviation of responses per participant
  response_sd <- apply(select(data, -c(id, timestamp)), 1, sd, na.rm = TRUE)
  
  # Flag suspicious patterns (e.g., straight-lining)
  response_sd > 0.5  # Adjust threshold as needed
}

# Main Scoring Function ----

#' Score all survey measures
#' @param data Dataframe containing all survey responses
#' @return List of scored results
score_surveys <- function(data) {
  # Quality control
  valid_responses <- data %>%
    filter(
      check_missing(.),
      check_attention(.),
      check_patterns(.)
    )
  
  # Score individual measures
  results <- list(
    fad = score_fad(valid_responses),
    crt = score_crt(valid_responses),
    ncs = score_ncs(valid_responses),
    aot = score_aot(valid_responses)
  )
  
  # Add metadata
  attr(results, "n_original") <- nrow(data)
  attr(results, "n_valid") <- nrow(valid_responses)
  attr(results, "timestamp") <- Sys.time()
  
  results
}

# Example Usage ----
if (FALSE) {
  # Load data
  data <- read_csv("survey_responses.csv")
  
  # Score all measures
  results <- score_surveys(data)
  
  # Access individual measure results
  fad_scores <- results$fad
  crt_scores <- results$crt
  
  # Access reliability information
  fad_reliability <- attr(results$fad, "reliability")
  
  # Save results
  write_csv(bind_rows(results), "scored_results.csv")
} 