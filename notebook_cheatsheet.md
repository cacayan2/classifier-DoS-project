# Final Project Jupyter Notebook Documentation Cheat Sheet
**Please follow this format whenever you add code or results to the notebooks to keep our repo easily readable.**

## 1. Add a Markdown Header Before Every Task
Use this format (copy/paste):

```
## [Date] - [Name] - [Task Title]

**What I worked on: **
- Short description of the task
- Purpose of the task
```

For instance:
```
## [2025-11-26] - [Emil] - [Cheat Sheet]
**What I worked on:**
I created a markdown file that contains a cheat sheet for documentation in our Jupyter notebook.
```

## 2. Add Code Cells 
Keep code readable and follow best practices for formatting/documentation:
* Use meaningful variable names.
* Keep lines under roughly 80 characters if possible.
* Add short inline comments only when needed.

For instance:
```
# generate histograms for selected columns
for col in cols:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df[col], bins=50, kde=False)
    plot.title(f"Histogram of {col}")
    plt.savefig(f"../eda/figures/univariate/{col}_hist.png")
```

## 3. After Running Code Add a Markdown Interpretation Block
Explaining understanding is required especially by Dr. Mohaisen.

Use this template (you can copy/paste this as well):
```
### Interpretation/Notes
- Summary of what the output shows
- Any interesting patterns
- Any weird observations or concerns
- Anything learned that may matter for downstream applications
```

For instance:
```
### Interpretation/Notes
- Many of the features having to do with the flows are severely left-skewed.
- Several features have near-zero variance.
- We will likely have to pay special attention to these and perhaps eliminate them from the dataset. 
```

## 4. Save Figures and Explain Where
If you generate any plots:
```
plt.savefig("../eda/figures/univariate/Flow_duration_hist.png)
```

You need to document where they are saved:
```
(PNG saved to `...eda/figures/univaraite/Flow_duration_hist.png`)
```

## 5. If you Create a File (CSV, JSON, PKL)
Always state:
```
### Files Written
- `data/interim/combined_raw.csv`
- What it contains
- Why it exists
```

This helps Dr. Mohaisen stay on track with what we're doing and also helps me (Emil) write the ADR!

## 6. Try to Keep Things in Chronological Order
When adding new content:
* Scroll to the bottom of the notebook.
* Add your new header, then code block, then notes.
* Do not insert in the middle of someone else's section.
* **Do not commit then push to the GitHub repo if you are not done with a particular section!!!**

That way we can keep the timeline of the notebook easy to follow.

## 7. Keep Sections Short
Avoid long paragraphs and stick to 3-6 bullet points, a few sentences explaining decisions, and clean visuals (not just a bunch of messy plots, which is why ultimately we're subsetting data for EDA). 

## 8. If you make a mistake and then push to GitHub...
Please ensure you delete, replace, and then re-run code so that correct file versions make it to GitHub!

## 9. At the end of a section, add a "Done" Note before pushing to GitHub.
This helps us ensure that we're not accidentally stepping into the middle of your workflow with our code and analysis. If you think someone else forgot, just message in the group chat or teams. 
```
### Done with Task
```

## 10. Here's a copy and paste template you can use!
```
### [Date] — [Name] — [Task Title]

**Purpose:**  
-  

**Code:**  
(put your code below this header)

**Interpretation / Findings:**  
-  

**Files Saved:**  
-  

**Notes for Team:**  
-  

### Done with Task
```

Thanks everyone! Here's to a good final project!!!