# How to approach new data sets

## Orient & Validate - Sanity chec

- what’s in this data set?
- How was it generated? 
- Do I have reasons to be weary?
- How big is it really? What’s the right tool? Excel/Pandas/Python/Cloud. WIll I eventually need Spark?
- Do I need to sample to get started?
- Can I reproduce/do an individual action to test this? E.g., click tracking to add another row

## Initial hypotheses

- Read the shcema and ask what you would expect.
- have some theories- Avoid p-hacking/ex post facto analysis
- Ask someone else

## More sanity - Types, Graph and correlate

- Is the schema deceiving? Is the data sparse? Are the types wrong?
- Explanatory vs Response
- Continuous vs Discrete
- Descriptive stats - Pandas-profiling
- Counts
- Distributions
- Outliers

## Slide and graph

- Slice data along dimensions
- Slice data along time
- Graph the basics
