---
title: "Distribution of Income, Wealth, and Mortgage in SCF"
author: "Alan Lujan"
date: "6/14/2021"
output:
  pdf_document: default
  html_document:
    df_print: paged
---


```r
library(ggplot2)
library(ggthemes)
library(haven)
library(tidyverse)

SCF <- read_dta("scf_nb.dta")
```


```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(1, 4)) %>% as_factor(),
  aes(x = lnPermIncome, y = lnNrmWealth)
) +
  geom_density_2d() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-66](figure/unnamed-chunk-66-1.png)



```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(5, 8)) %>% as_factor(),
  aes(x = lnPermIncome, y = lnNrmWealth)
) +
  geom_density_2d() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-67](figure/unnamed-chunk-67-1.png)


```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(9, 12)) %>% as_factor(),
  aes(x = lnPermIncome, y = lnNrmWealth)
) +
  geom_density_2d() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-68](figure/unnamed-chunk-68-1.png)


```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(13, 16)) %>% as_factor(),
  aes(x = lnPermIncome, y = lnNrmWealth)
) +
  geom_density_2d() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-69](figure/unnamed-chunk-69-1.png)



```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(1, 4)) %>% as_factor(),
  aes(x = lnNrmWealth, weight = wgt)
) +
  geom_density() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-70](figure/unnamed-chunk-70-1.png)


```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(5, 8)) %>% as_factor(),
  aes(x = lnNrmWealth, weight = wgt)
) +
  geom_density() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-71](figure/unnamed-chunk-71-1.png)

```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(9, 12)) %>% as_factor(),
  aes(x = lnNrmWealth, weight = wgt)
) +
  geom_density() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-72](figure/unnamed-chunk-72-1.png)

```r
p <- ggplot(
  SCF %>%
    filter(Age_grp %in% seq(13, 16)) %>% as_factor(),
  aes(x = lnNrmWealth, weight = wgt)
) +
  geom_density() +
  facet_grid(Age_grp ~ Educ) +
  theme_bw()
print(p)
```

![plot of chunk unnamed-chunk-73](figure/unnamed-chunk-73-1.png)


```r
p <- ggplot(
  SCF %>% as_factor(),
  aes(y = lnPermIncome, x = age, weight = wgt, group=Educ, color = Educ)
) +
  geom_smooth() +
  theme_bw()
print(p)
```

```
## `geom_smooth()` using method = 'gam' and formula 'y ~ s(x, bs = "cs")'
```

![plot of chunk unnamed-chunk-74](figure/unnamed-chunk-74-1.png)


```r
p <- ggplot(
  SCF %>% as_factor(),
  aes(y = lnNrmWealth, x = age, weight = wgt, group=Educ, color = Educ)
) +
  geom_smooth() +
  theme_bw()
print(p)
```

```
## `geom_smooth()` using method = 'gam' and formula 'y ~ s(x, bs = "cs")'
```

![plot of chunk unnamed-chunk-75](figure/unnamed-chunk-75-1.png)


```r
p <- ggplot(
  SCF %>% as_factor(),
  aes(y = lnMortgage, x = age, weight = wgt, group=Educ, color = Educ)
) +
  geom_smooth() +
  theme_bw()
print(p)
```

```
## `geom_smooth()` using method = 'gam' and formula 'y ~ s(x, bs = "cs")'
```

```
## Warning: Removed 111517 rows containing non-finite values (stat_smooth).
```

![plot of chunk unnamed-chunk-76](figure/unnamed-chunk-76-1.png)
