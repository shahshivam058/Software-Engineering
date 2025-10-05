"""
You are given:

Initial capital w.
A list of projects, where each project i has:
A pure profit profits[i] (which is added to your capital upon completion).
A minimum capital capital[i] required to start it.
The maximum number of distinct projects you can complete, k.
To start a project, your current capital must be at least the project's required capital. The capital requirement is a threshold, not an expenditure.
The core challenge is that choosing a profitable project increases your capital, which might unlock more projects in subsequent rounds.

- At any step, if you have a choice of several projects you can afford, which one should you choose?
- Since completing a project only increases your capital (profit is always added), the best choice is always the one that offers the maximum 
  pure profit among all currently affordable projects.
- This is because maximizing your capital increase at each step gives you the best chance of affording higher-capital projects later, 
  maximizing the final total.

Min-Heap (CapitalHeap)	Tracks all available projects by capital requirement.	Pairs of (capital[i],profits[i])	Min-Heap (sorted by capital)
Max-Heap (ProfitHeap)	Tracks affordable projects by profit.	profits[i] (often negated for max-heap behavior)	Max-Heap (sorted by profit)

- Preprocessing: Combine the capital and profits arrays into a single list of project pairs (capital,profit). Sort this list primarily by 
  capital requirement in ascending order. This sorted list will act as your CapitalHeap's initial state for projects you cannot yet afford, 
  allowing you to iterate through them efficiently.
- Iteration: Loop k times (for the k projects you can complete):
- Transfer Projects: While there are still projects in your sorted list whose required capital is ≤ your current capital w, move their 
  profits into the ProfitHeap.
- Select Project: If the ProfitHeap is not empty:
- Pop the maximum profit (the root of the Max-Heap). This is your greedy choice.
- Add this profit to your current capital: w=w+profit.
- Break Condition: If the ProfitHeap is empty, it means you cannot afford any remaining projects, so you must stop early.
- Result: After the loop completes or breaks, the final value of w is the maximum maximized capital.




"""